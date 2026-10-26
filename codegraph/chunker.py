"""Split a repository into meaningful chunks.

Python is split with the AST: one chunk per function, method and class
header, plus a module chunk for imports and top-level code. Other code is
split at function/class-looking lines, Markdown at headings, and anything
else into paragraphs. Every chunk records the names it defines and the
identifiers it uses; those are what associations are built from.
"""
import ast
import hashlib
import os
import re

MAX_FILE_BYTES = 1_000_000
MAX_CHUNK_LINES = 120
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".codegraph", ".stringspace",
             "venv", ".venv", "dist", "build", ".mypy_cache", ".pytest_cache",
             ".tox", ".next", "target", "vendor"}
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip", ".gz", ".tar",
              ".whl", ".so", ".dll", ".exe", ".pyc", ".woff", ".woff2", ".ttf", ".mp4",
              ".mp3", ".lock", ".bin", ".db", ".sqlite", ".svg", ".min.js", ".map"}
CODE_EXT = {".js", ".jsx", ".ts", ".tsx", ".go", ".java", ".kt", ".c", ".h", ".cc",
            ".cpp", ".hpp", ".cs", ".rs", ".swift", ".php", ".rb", ".lua", ".scala", ".sh"}
IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
DEF_LINE = re.compile(
    r"^\s*(?:export\s+)?(?:default\s+)?(?:public|private|protected|static|async|final|override|\s)*"
    r"(?:function\*?|func|fn|def|class|struct|interface|enum|trait|impl|type|module|local\s+function)"
    r"\s+([A-Za-z_][A-Za-z0-9_.:]*)"
    r"|^\s*(?:export\s+)?(?:const|let|var)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?:async\s*)?(?:\(|function)")


def repository_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".") or d == ".github")
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            if any(name.lower().endswith(e) for e in BINARY_EXT):
                continue
            try:
                if os.path.getsize(path) > MAX_FILE_BYTES:
                    continue
            except OSError:
                continue
            yield os.path.relpath(path, root).replace(os.sep, "/")


def read(root, rel):
    try:
        with open(os.path.join(root, rel), encoding="utf-8") as f:
            return f.read()
    except (UnicodeDecodeError, OSError):
        return None


def _chunk(path, kind, name, lines, start, end, defines=()):
    text = "\n".join(lines[start - 1:end])
    return {
        "id": f"{path}::{name}" if name else f"{path}#L{start}",
        "path": path, "kind": kind, "name": name or "", "start": start, "end": end,
        "text": text, "defines": sorted(set(defines)),
        "uses": sorted(set(IDENT.findall(text)) - set(defines)),
        "hash": hashlib.sha1(text.encode()).hexdigest()[:12],
    }


def _python(path, source, lines):
    tree = ast.parse(source)
    chunks, covered = [], set()

    def visit(node, prefix):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                start = min([d.lineno for d in child.decorator_list] + [child.lineno])
                end = child.end_lineno
                name = f"{prefix}{child.name}"
                if isinstance(child, ast.ClassDef):
                    body_start = child.body[0].lineno if child.body else end
                    methods = [c for c in child.body if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
                    header_end = (min(m.lineno for m in methods) - 1) if methods else end
                    header_end = max(header_end, body_start) if not methods else header_end
                    chunks.append(_chunk(path, "class", name, lines, start, header_end, [child.name]))
                    covered.update(range(start, header_end + 1))
                    visit(child, f"{name}.")
                else:
                    if end - start + 1 > MAX_CHUNK_LINES * 2:
                        end = start + MAX_CHUNK_LINES * 2 - 1
                    chunks.append(_chunk(path, "function" if not prefix else "method",
                                         name, lines, start, child.end_lineno, [child.name]))
                    covered.update(range(start, child.end_lineno + 1))

    visit(tree, "")
    rest = [i for i in range(1, len(lines) + 1) if i not in covered and lines[i - 1].strip()]
    if rest:
        defines = [t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets
                   if isinstance(t, ast.Name)]
        module = _chunk(path, "module", "<module>", lines, 1, len(lines), defines)
        module["text"] = "\n".join(lines[i - 1] for i in rest[:MAX_CHUNK_LINES])
        module["uses"] = sorted(set(IDENT.findall(module["text"])) - set(defines))
        chunks.insert(0, module)
    return chunks


def _split_at(path, kind, lines, starts):
    chunks = []
    bounds = sorted(set([1] + [s for s, _ in starts])) + [len(lines) + 1]
    names = dict(starts)
    for a, b in zip(bounds, bounds[1:]):
        for s in range(a, b, MAX_CHUNK_LINES):
            e = min(b - 1, s + MAX_CHUNK_LINES - 1)
            if any(l.strip() for l in lines[s - 1:e]):
                name = names.get(s) if s == a else None
                chunks.append(_chunk(path, kind if name else "block", name, lines, s, e,
                                     [name.split(".")[-1].split(":")[-1]] if name else []))
    return chunks


def chunk_file(path, source):
    lines = source.splitlines()
    if not lines:
        return []
    ext = os.path.splitext(path)[1].lower()
    if ext == ".py":
        try:
            return _python(path, source, lines)
        except SyntaxError:
            pass
    if ext in CODE_EXT or ext == ".py":
        starts = []
        for i, line in enumerate(lines, 1):
            m = DEF_LINE.match(line)
            if m:
                starts.append((i, m.group(1) or m.group(2)))
        return _split_at(path, "function", lines, starts)
    if ext in {".md", ".rst", ".txt"}:
        starts = [(i, line.lstrip("#").strip()[:60]) for i, line in enumerate(lines, 1)
                  if line.startswith("#")]
        return _split_at(path, "section", lines, starts)
    starts, prev_blank = [], True  # anything else: paragraphs
    for i, line in enumerate(lines, 1):
        if line.strip() and prev_blank:
            starts.append((i, None))
        prev_blank = not line.strip()
    return [c for c in _split_at(path, "block", lines, [(s, None) for s, _ in starts])]
