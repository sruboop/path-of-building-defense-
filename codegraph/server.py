"""MCP server (stdio, JSON-RPC 2.0, no dependencies).

Tools the AI gets:
  search_code   find chunks for a question; matches flow along associations
  read_chunk    the full text of a chunk and what it is associated with
  related       a chunk's strongest associations
  remember      save research, findings or decisions into the graph
  associate     add an association the AI discovered (counts the most)
  pending_annotations  files/chunks the AI has not described yet
  annotate      the AI writes what a file/chunk means: summary + concepts
  graph_stats   size of the graph

Before every search the server re-chunks files that changed on disk, so the
graph keeps up with edits on its own.
"""
import json
import sys

from .graph import Graph

PROTOCOL = "2025-06-18"
SNIPPET_LINES = 40

TOOLS = [
    {"name": "search_code",
     "description": "Search the repository's chunk/association graph. Use this FIRST for any question or "
                    "task about this codebase, and again with different words if results look thin. "
                    "Returns meaningful chunks (functions, classes, sections, saved research notes) with "
                    "why each was associated.",
     "inputSchema": {"type": "object", "properties": {
         "query": {"type": "string", "description": "what you are looking for, in plain words and/or identifiers"},
         "k": {"type": "integer", "description": "how many chunks (default 8)"}},
         "required": ["query"]}},
    {"name": "read_chunk",
     "description": "Full text of one chunk plus its strongest associations (calls, imports, similar, notes...).",
     "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}, "required": ["id"]}},
    {"name": "related",
     "description": "The chunks most strongly associated with a chunk, with the kind of each association.",
     "inputSchema": {"type": "object", "properties": {
         "id": {"type": "string"}, "k": {"type": "integer"}}, "required": ["id"]}},
    {"name": "remember",
     "description": "Save knowledge into the graph so future searches find it: research results, web "
                    "findings, explanations, decisions, gotchas. Link it to chunk ids, file paths or "
                    "symbol names it is about.",
     "inputSchema": {"type": "object", "properties": {
         "title": {"type": "string"}, "content": {"type": "string"},
         "source": {"type": "string", "description": "URL or origin, optional"},
         "links": {"type": "array", "items": {"type": "string"}}},
         "required": ["title", "content"]}},
    {"name": "associate",
     "description": "Record that two things are connected: chunk ids, file paths, note titles, symbol "
                    "names, or plain ideas ('bunt', 'short-range knockback'), which become concept nodes. "
                    "Learned associations weigh the most and are searchable.",
     "inputSchema": {"type": "object", "properties": {
         "a": {"type": "string"}, "b": {"type": "string"}, "why": {"type": "string"}},
         "required": ["a", "b", "why"]}},
    {"name": "pending_annotations",
     "description": "Files (level='file', default) or chunks (level='chunk') that have no annotation yet, "
                    "or whose code changed since. Read the overviews, then call annotate for each.",
     "inputSchema": {"type": "object", "properties": {
         "k": {"type": "integer", "description": "how many (default 5)"},
         "level": {"type": "string", "enum": ["file", "chunk"]}}}},
    {"name": "annotate",
     "description": "Give files or chunks their meaning: a one or two sentence plain-language summary of "
                    "what it does and why, plus concept words a person might use when asking about it "
                    "(synonyms, everyday words, the problem it solves, related standards). Optional links "
                    "to other chunk ids, paths or symbols it works with. Search uses all of this.",
     "inputSchema": {"type": "object", "properties": {"items": {"type": "array", "items": {
         "type": "object", "properties": {
             "target": {"type": "string", "description": "file path or chunk id"},
             "summary": {"type": "string"},
             "concepts": {"type": "array", "items": {"type": "string"}},
             "links": {"type": "array", "items": {"type": "object", "properties": {
                 "to": {"type": "string"}, "why": {"type": "string"}}}}},
         "required": ["target", "summary", "concepts"]}}},
         "required": ["items"]}},
    {"name": "graph_stats", "description": "Counts of chunks, associations, notes and learned links.",
     "inputSchema": {"type": "object", "properties": {}}},
]


def _snippet(chunk, limit=SNIPPET_LINES):
    lines = chunk["text"].splitlines()
    more = f"\n    … {len(lines) - limit} more lines (read_chunk for all)" if len(lines) > limit else ""
    return "\n".join(lines[:limit]) + more


def _where(c):
    return c["path"] if c["kind"] in ("note", "concept") else f"{c['path']}:{c['start']}-{c['end']}"


class Server:
    def __init__(self, root):
        self.root = root
        self._graph = None

    @property
    def graph(self):
        if self._graph is None:
            self._graph = Graph.load(self.root)
        return self._graph

    def call(self, name, args):
        g = self.graph
        g.sync()  # the hooks write from another process
        if name == "search_code":
            changed = g.refresh()
            hits = g.search(args["query"], k=int(args.get("k", 8)))
            if not hits:
                return "No chunk matches those words. Try other words or identifiers."
            out = [f"(re-indexed {len(changed)} changed files)"] if changed else []
            for h in hits:
                c = g.chunks[h["id"]]
                why = "matched the query" if h["matched"] else "; ".join(h["why"])
                if h["matched"] and h["why"]:
                    why += "; also " + "; ".join(h["why"][:2])
                meaning = g.meaning(h["id"])
                meaning = f"meaning: {meaning}\n" if meaning else ""
                out.append(f"## {h['id']}  [{c['kind']}, {_where(c)}, score {h['score']}]\n"
                           f"{meaning}why: {why}\n```\n{_snippet(c)}\n```")
            return "\n\n".join(out)
        if name == "read_chunk":
            c = g.chunks.get(args["id"])
            if not c:
                return f"No chunk {args['id']!r}. Use search_code to find ids."
            rel = "\n".join(f"- {r['id']}  ({', '.join(f'{k}: {v}' for k, v in r['kinds'].items())})"
                            for r in g.related(c["id"], 10))
            return f"## {c['id']}  [{c['kind']}, {_where(c)}]\n```\n{c['text']}\n```\nassociated with:\n{rel}"
        if name == "related":
            rows = g.related(args["id"], int(args.get("k", 12)))
            return "\n".join(f"- {r['id']}  w={r['weight']}  ({', '.join(f'{k}: {v}' for k, v in r['kinds'].items())})"
                             for r in rows) or "No associations."
        if name == "remember":
            nid = g.remember(args["title"], args["content"], args.get("source"), args.get("links", []))
            return f"Saved as {nid} with {len(g.edges.get(nid, {}))} associations."
        if name == "associate":
            ok = g.associate(args["a"], args["b"], args["why"])
            return ("Associated: " + " <-> ".join(", ".join(g._resolve(x)) for x in (args["a"], args["b"]))
                    if ok else "Both ends are needed, and they must differ.")
        if name == "pending_annotations":
            g.refresh()
            level = args.get("level", "file")
            items, remaining = g.pending(int(args.get("k", 5)), level)
            if not items:
                return f"Every {level} is annotated and up to date."
            body = "\n\n".join(f"### {it['target']}\n```\n{it['overview']}\n```" for it in items)
            return f"{remaining} {level}s still need annotations. Next {len(items)}:\n\n{body}"
        if name == "annotate":
            done, missing = g.annotate(args.get("items", []))
            msg = f"Annotated {len(done)}."
            if missing:
                msg += f" Not found: {', '.join(map(str, missing))}."
            left = sum(1 for p in g.files if g.stale(p))
            return msg + f" {left} files still unannotated."
        if name == "graph_stats":
            n_edges = sum(len(v) for v in g.edges.values()) // 2
            annotated = sum(1 for p in g.files if not g.stale(p))
            return (f"{len(g.files)} files, {len(g.chunks)} chunks, {n_edges} associations, "
                    f"{len(g.notes)} notes, {len(g.learned)} learned associations, "
                    f"{annotated}/{len(g.files)} files annotated")
        raise KeyError(name)

    def handle(self, msg):
        method, mid = msg.get("method"), msg.get("id")
        if method == "initialize":
            version = msg.get("params", {}).get("protocolVersion", PROTOCOL)
            result = {"protocolVersion": version, "capabilities": {"tools": {}},
                      "serverInfo": {"name": "codegraph", "version": "0.1.0"},
                      "instructions": "Search this repository's chunk/association graph with search_code "
                                      "before reading files. Save research and findings with remember."}
        elif method == "tools/list":
            result = {"tools": TOOLS}
        elif method == "tools/call":
            p = msg.get("params", {})
            try:
                text, error = self.call(p.get("name"), p.get("arguments") or {}), False
            except KeyError as e:
                text, error = f"Unknown tool or missing argument: {e}", True
            except Exception as e:  # never kill the server over one call
                text, error = f"{type(e).__name__}: {e}", True
            result = {"content": [{"type": "text", "text": text}], "isError": error}
        elif method == "ping":
            result = {}
        elif mid is None:
            return None  # notifications need no answer
        else:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"no method {method}"}}
        return {"jsonrpc": "2.0", "id": mid, "result": result}


def serve(root):
    server = Server(root)
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        reply = server.handle(msg)
        if reply is not None:
            sys.stdout.write(json.dumps(reply) + "\n")
            sys.stdout.flush()
