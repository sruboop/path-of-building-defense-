"""The association graph and how it is searched and kept up to date.

Kinds of association between chunks:
  contains   file -> its chunks, class -> its methods
  sequence   neighbouring chunks in a file
  calls      a chunk uses a name another chunk defines
  imports    a module imports another module
  similar    the two chunks use the same rare words (TF-IDF cosine)
  cochange   git history: the files keep changing in the same commits
  note       research notes linked to the code they talk about
  learned    associations the AI added itself, which count the most

The AI in the chat also gives the graph its meaning: it reads chunks and
writes a plain-language summary and concept words for each file or chunk
(`annotate`). Those words are searched along with the code, so a question
asked in everyday words finds code named in programmer's words.

Everything lives in ROOT/.codegraph/: chunks.jsonl, associations.jsonl,
notes.jsonl (research and memory), learned.jsonl (AI-made links) and
annotations.jsonl (AI-written meaning).
"""
import json
import math
import os
import re
import subprocess
import time
from collections import Counter, defaultdict

from .chunker import chunk_file, read, repository_files

DIR = ".codegraph"
WEIGHTS = {"contains": 0.3, "sequence": 0.25, "calls": 1.0, "imports": 0.6,
           "similar": 0.8, "cochange": 0.5, "note": 0.9, "learned": 1.5}
SIMILAR_K = 6
COMMON_NAME_LIMIT = 6        # a name defined in more places than this links nothing
STOP = set("""self cls the and for not none true false return if else elif in is of to a an
def class import from as with try except finally raise pass while break continue lambda yield
this that it be or on by at are was were var let const function new null undefined""".split())
WORD = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
CAMEL = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|\d+")
PY_IMPORT = re.compile(r"^\s*(?:from\s+(\.*[\w.]*)\s+import|import\s+([\w.]+))", re.M)
JS_IMPORT = re.compile(r"""(?:from|require\()\s*['"](\.{1,2}/[^'"]+)['"]""")


def terms(text):
    out = []
    for word in WORD.findall(text):
        parts = [p.lower() for piece in word.split("_") for p in CAMEL.findall(piece)]
        if len(parts) > 1:
            parts.append(word.lower())
        out += [p for p in parts if len(p) > 1 and p not in STOP and not p.isdigit()]
    return out


def _stem(t):
    for suffix in ("ing", "ed", "es", "s"):
        if len(t) > len(suffix) + 3 and t.endswith(suffix):
            return t[:-len(suffix)]
    return t


def bag(chunk, annotations=()):
    """Terms of a chunk; its name, path and the AI's annotations count extra."""
    c = Counter(_stem(t) for t in terms(chunk["text"]))
    for t in terms(chunk["name"]) * 3 + terms(chunk["path"]) * 2:
        c[_stem(t)] += 1
    for a, weight in annotations:
        for t in terms(a.get("summary", "")) * weight + terms(" ".join(a.get("concepts", []))) * (weight + 1):
            c[_stem(t)] += 1
    return c


def _file_hash(chunks):
    return "".join(sorted(c["hash"] for c in chunks))[-16:] if chunks else ""


class Graph:
    def __init__(self, root):
        self.root = os.path.abspath(root)
        self.dir = os.path.join(self.root, DIR)
        self.chunks = {}
        self.files = {}           # path -> [mtime, size, [chunk ids]]
        self.notes = []
        self.learned = []
        self.annotations = {}     # chunk id or file path -> {summary, concepts, hash}
        self.edges = defaultdict(dict)   # id -> {id: [weight, {kind: why}]}

    # -- building ----------------------------------------------------------
    def build(self):
        for rel in repository_files(self.root):
            self._chunk_path(rel)
        self._load_memory()
        self._associate()
        self.save()
        return self

    def _chunk_path(self, rel):
        full = os.path.join(self.root, rel)
        source = read(self.root, rel)
        for cid in self.files.get(rel, [0, 0, []])[2]:
            self.chunks.pop(cid, None)
        if source is None:
            self.files.pop(rel, None)
            return
        st = os.stat(full)
        made = chunk_file(rel, source)
        seen = Counter()
        for c in made:
            seen[c["id"]] += 1
            if seen[c["id"]] > 1:
                c["id"] += f"@{c['start']}"
            self.chunks[c["id"]] = c
        self.files[rel] = [st.st_mtime, st.st_size, [c["id"] for c in made]]

    MEMORY = ("notes.jsonl", "learned.jsonl", "annotations.jsonl")

    def _memory_stamp(self):
        stamp = []
        for name in self.MEMORY:
            try:
                st = os.stat(os.path.join(self.dir, name))
                stamp.append((st.st_mtime_ns, st.st_size))
            except FileNotFoundError:
                stamp.append(None)
        return stamp

    def _load_memory(self):
        for cid in [cid for cid, c in self.chunks.items() if c["kind"] in ("note", "concept")]:
            del self.chunks[cid]
        self.notes = _read_jsonl(os.path.join(self.dir, "notes.jsonl"))
        self.learned = _read_jsonl(os.path.join(self.dir, "learned.jsonl"))
        self.annotations = {a["target"]: a for a in _read_jsonl(os.path.join(self.dir, "annotations.jsonl"))}
        for n in self.notes:
            self.chunks[n["id"]] = n
        self._concepts()
        self._stamp = self._memory_stamp()

    def _concepts(self):
        """Ends of learned associations that are not code or notes become concept
        nodes, so the AI can associate ideas ("bunt", "knockback") freely."""
        whys = defaultdict(list)
        for l in self.learned:
            for end, other in ((l["a"], l["b"]), (l["b"], l["a"])):
                if not self._resolve(end, concepts=False):
                    whys[end.strip()].append(f"{other}: {l.get('why', '')}")
        for name, lines in whys.items():
            cid = f"concept:{name.lower()}"
            text = f"{name}\n" + "\n".join(lines)
            self.chunks[cid] = {"id": cid, "path": "concept", "kind": "concept", "name": name,
                                "start": 1, "end": 1, "text": text, "defines": [],
                                "uses": sorted(set(WORD.findall(text))), "hash": ""}

    def sync(self):
        """Pick up notes/links/annotations other processes (the hooks) wrote."""
        if self._memory_stamp() != getattr(self, "_stamp", None):
            self._load_memory()
            self._associate()
            return True
        return False

    def refresh(self):
        """Re-chunk files that changed on disk; returns the paths that changed."""
        changed = []
        current = set(repository_files(self.root))
        for rel in sorted(current | set(self.files)):
            full = os.path.join(self.root, rel)
            old = self.files.get(rel)
            if rel not in current:
                for cid in old[2]:
                    self.chunks.pop(cid, None)
                del self.files[rel]
                changed.append(rel)
                continue
            st = os.stat(full)
            if not old or old[0] != st.st_mtime or old[1] != st.st_size:
                self._chunk_path(rel)
                changed.append(rel)
        if changed:
            self._associate()
            self.save()
        return changed

    def _link(self, a, b, kind, why, weight=None):
        if a == b or a not in self.chunks or b not in self.chunks:
            return
        w = WEIGHTS[kind] if weight is None else weight
        for x, y in ((a, b), (b, a)):
            e = self.edges[x].setdefault(y, [0.0, {}])
            if kind not in e[1]:
                e[0] += w
                e[1][kind] = why

    def _associate(self):
        self.edges = defaultdict(dict)
        chunks = self.chunks
        self.bags = {cid: bag(c, self._annotations_of(c)) for cid, c in chunks.items()}
        self.df = Counter()
        for b in self.bags.values():
            self.df.update(b.keys())
        self.postings = defaultdict(list)
        for cid, b in self.bags.items():
            for t, n in b.items():
                self.postings[t].append((cid, n))
        self.avglen = sum(sum(b.values()) for b in self.bags.values()) / max(1, len(self.bags))

        by_file = defaultdict(list)
        for c in chunks.values():
            by_file[c["path"]].append(c)
        definers = defaultdict(list)
        for c in chunks.values():
            if c["kind"] != "module":
                for name in c["defines"]:
                    definers[name].append(c["id"])

        for path, cs in by_file.items():
            cs.sort(key=lambda c: c["start"])
            module = next((c for c in cs if c["kind"] == "module"), None)
            for prev, cur in zip(cs, cs[1:]):
                self._link(prev["id"], cur["id"], "sequence", "next to each other")
            for c in cs:
                if module and c is not module:
                    self._link(module["id"], c["id"], "contains", f"defined in {path}")
                if c["kind"] == "method":
                    owner = c["id"].rsplit(".", 1)[0]
                    self._link(owner, c["id"], "contains", "method of the class")

        for c in chunks.values():  # calls / references
            for name in c["uses"]:
                where = definers.get(name, ())
                if 0 < len(where) <= COMMON_NAME_LIMIT and len(name) > 2:
                    for d in where:
                        self._link(c["id"], d, "calls", f"{c['name'] or c['path']} uses {name}",
                                   WEIGHTS["calls"] / len(where))

        self._imports(by_file)
        self._similar()
        self._cochange(by_file)
        for n in self.notes:
            for target in n.get("links", []):
                for cid in self._resolve(target):
                    self._link(n["id"], cid, "note", "the note links it")
        for l in self.learned:
            for a in self._resolve(l["a"]):
                for b in self._resolve(l["b"]):
                    self._link(a, b, "learned", l.get("why", "linked by the AI"))

    def _resolve(self, ref, concepts=True):
        """A chunk id, a path (-> its module), a note title, a concept or a symbol name."""
        if not ref or not isinstance(ref, str):
            return []
        if ref in self.chunks and (concepts or self.chunks[ref]["kind"] != "concept"):
            return [ref]
        if ref in self.files:
            ids = self.files[ref][2]
            mods = [i for i in ids if i.endswith("::<module>")]
            return mods or ids[:1]
        low = ref.strip().lower()
        kinds = ("note", "concept") if concepts else ("note",)
        titled = [cid for cid, c in self.chunks.items() if c["kind"] in kinds and
                  (c["name"].lower() == low or (len(low) > 12 and c["name"].lower().startswith(low)))]
        if titled:
            return titled[:1]
        return [cid for cid, c in self.chunks.items() if ref in c["defines"]][:COMMON_NAME_LIMIT]

    def _imports(self, by_file):
        paths = set(self.files)
        for path, cs in by_file.items():
            if path.startswith("note:"):
                continue
            text = "\n".join(c["text"] for c in cs if c["kind"] in ("module", "block"))
            here = os.path.dirname(path)
            targets = set()
            for rel, absolute in PY_IMPORT.findall(text):
                mod = rel or absolute
                dots = len(mod) - len(mod.lstrip("."))
                base = here
                for _ in range(max(0, dots - 1)):
                    base = os.path.dirname(base)
                name = mod.lstrip(".").replace(".", "/")
                stem = os.path.join(base, name) if dots else name
                for cand in (stem + ".py", os.path.join(stem, "__init__.py")):
                    cand = os.path.normpath(cand).replace(os.sep, "/")
                    if cand in paths:
                        targets.add(cand)
                if not dots:  # absolute import inside a package directory
                    for p in paths:
                        if p.endswith("/" + name + ".py"):
                            targets.add(p)
            for rel in JS_IMPORT.findall(text):
                stem = os.path.normpath(os.path.join(here, rel)).replace(os.sep, "/")
                for ext in ("", ".js", ".ts", ".tsx", ".jsx", "/index.js", "/index.ts"):
                    if stem + ext in paths:
                        targets.add(stem + ext)
            src = self._resolve(path)
            for t in targets:
                for a in src:
                    for b in self._resolve(t):
                        self._link(a, b, "imports", f"{path} imports {t}")

    def _similar(self):
        n = len(self.bags) or 1
        idf = {t: math.log(n / d) for t, d in self.df.items()}
        vec, norm = {}, {}
        for cid, b in self.bags.items():
            v = {t: (1 + math.log(c)) * idf[t] for t, c in b.items() if idf[t] > 0.5}
            vec[cid] = v
            norm[cid] = math.sqrt(sum(x * x for x in v.values())) or 1.0
        cap = max(50, n // 20)  # very common terms are skipped for speed
        for cid, v in vec.items():
            acc = defaultdict(float)
            for t, x in v.items():
                plist = self.postings[t]
                if len(plist) > cap:
                    continue
                for other, _ in plist:
                    if other != cid:
                        acc[other] += x * vec[other].get(t, 0.0)
            best = sorted(((s / (norm[cid] * norm[o]), o) for o, s in acc.items()), reverse=True)
            for s, o in best[:SIMILAR_K]:
                if s < 0.2:
                    break
                kind = "note" if cid.startswith("note:") or o.startswith("note:") else "similar"
                self._link(cid, o, kind, f"share rare words (cos {s:.2f})", WEIGHTS[kind] * s)

    def _cochange(self, by_file, commits=500):
        try:
            log = subprocess.run(["git", "-C", self.root, "log", f"-{commits}", "--name-only",
                                  "--pretty=format:@@"], capture_output=True, text=True,
                                 timeout=30).stdout
        except (OSError, subprocess.SubprocessError):
            return
        pairs, touched = Counter(), Counter()
        for commit in log.split("@@"):
            files = sorted({f for f in commit.split() if f in self.files})
            if 1 < len(files) <= 10:
                touched.update(files)
                for i, a in enumerate(files):
                    for b in files[i + 1:]:
                        pairs[(a, b)] += 1
        for (a, b), c in pairs.items():
            if c >= 2:
                j = c / (touched[a] + touched[b] - c)
                for x in self._resolve(a):
                    for y in self._resolve(b):
                        self._link(x, y, "cochange", f"changed together in {c} commits",
                                   WEIGHTS["cochange"] * j)

    # -- meaning: written by the AI in the chat -----------------------------
    def _annotations_of(self, c):
        found = []
        if c["id"] in self.annotations:
            found.append((self.annotations[c["id"]], 2))
        if c["path"] in self.annotations:  # the file's meaning flavours all its chunks
            found.append((self.annotations[c["path"]], 2 if c["kind"] == "module" else 1))
        return found

    def _current_hash(self, target):
        if target in self.chunks:
            return self.chunks[target]["hash"]
        return _file_hash([self.chunks[i] for i in self.files.get(target, [0, 0, []])[2] if i in self.chunks])

    def stale(self, target):
        a = self.annotations.get(target)
        return a is None or a.get("hash") != self._current_hash(target)

    def pending(self, k=5, level="file", lines_per_chunk=4, max_lines=80):
        """Files (or chunks) the AI has not described yet, or whose code changed since."""
        out = []
        if level == "file":
            for path, (_, _, ids) in sorted(self.files.items()):
                if not self.stale(path):
                    continue
                parts = []
                for cid in ids:
                    c = self.chunks.get(cid)
                    if not c:
                        continue
                    body = [l for l in c["text"].splitlines() if l.strip()]
                    take = body[:lines_per_chunk * (4 if c["kind"] == "module" else 1)]
                    parts.append(f"[{cid}] ({c['kind']})\n" + "\n".join(take))
                text = "\n".join(parts).splitlines()[:max_lines]
                out.append({"target": path, "chunks": len(ids), "overview": "\n".join(text)})
                if len(out) >= k:
                    break
        else:
            for cid, c in self.chunks.items():
                if c["kind"] in ("note", "concept", "module") or not self.stale(cid):
                    continue
                out.append({"target": cid, "overview": "\n".join(c["text"].splitlines()[:max_lines // 2])})
                if len(out) >= k:
                    break
        remaining = sum(1 for p in self.files if self.stale(p)) if level == "file" else \
            sum(1 for i, c in self.chunks.items() if c["kind"] not in ("note", "module") and self.stale(i))
        return out, remaining

    def annotate(self, items):
        """items: [{target, summary, concepts: [...], links: [{to, why}]}]"""
        self.sync()
        done, missing = [], []
        for it in items:
            target = it.get("target") or it.get("id")
            if target not in self.chunks and target not in self.files:
                missing.append(target)
                continue
            self.annotations[target] = {
                "target": target, "summary": it.get("summary", ""),
                "concepts": list(it.get("concepts", [])), "hash": self._current_hash(target),
                "time": time.strftime("%Y-%m-%d %H:%M")}
            for link in it.get("links", []):
                to = link.get("to") if isinstance(link, dict) else link
                why = link.get("why", "linked while annotating") if isinstance(link, dict) else "linked while annotating"
                if to:
                    self.learned.append({"a": target, "b": to, "why": why,
                                         "time": time.strftime("%Y-%m-%d %H:%M")})
            done.append(target)
        if done:
            _write_jsonl(os.path.join(self.dir, "annotations.jsonl"), list(self.annotations.values()))
            _write_jsonl(os.path.join(self.dir, "learned.jsonl"), self.learned)
            self._load_memory()
            self._associate()
            self.save()
        return done, missing

    def meaning(self, cid):
        c = self.chunks.get(cid)
        if not c:
            return ""
        a = self.annotations.get(cid) or self.annotations.get(c["path"])
        return a["summary"] if a else ""

    # -- memory: the graph grows from what the AI does ------------------------
    def remember(self, title, content, source=None, links=()):
        self.sync()
        note = {"id": f"note:{len(self.notes) + 1}:{title[:50]}", "path": f"note:{source or 'memory'}",
                "kind": "note", "name": title, "start": 1, "end": content.count("\n") + 1,
                "text": f"{title}\n{content}", "defines": [], "uses": sorted(set(WORD.findall(content))),
                "links": list(links), "source": source, "time": time.strftime("%Y-%m-%d %H:%M")}
        for existing in self.notes:  # same source and title: the newer note replaces it
            if existing.get("source") == source and existing["name"] == title:
                self.chunks.pop(existing["id"], None)
                note["id"] = existing["id"]
                self.notes.remove(existing)
                break
        self.notes.append(note)
        self.chunks[note["id"]] = note
        _write_jsonl(os.path.join(self.dir, "notes.jsonl"), self.notes)
        self._associate()
        self.save()
        return note["id"]

    def associate(self, a, b, why):
        """Link two things. Code, files, notes and symbols are found by id, path,
        title or name; anything else becomes a concept node."""
        return self.associate_many([{"a": a, "b": b, "why": why}]) == 1

    def associate_many(self, links):
        self.sync()
        made = 0
        for l in links:
            a, b = (l.get("a") or "").strip(), (l.get("b") or "").strip()
            if a and b and a != b:
                self.learned.append({"a": a, "b": b, "why": l.get("why", ""),
                                     "time": time.strftime("%Y-%m-%d %H:%M")})
                made += 1
        if made:
            _write_jsonl(os.path.join(self.dir, "learned.jsonl"), self.learned)
            self._load_memory()
            self._associate()
            self.save()
        return made

    # -- searching -----------------------------------------------------------
    def bm25(self, query, k1=1.2, b=0.75):
        n = len(self.bags) or 1
        scores = defaultdict(float)
        for t in set(_stem(t) for t in terms(query)):
            plist = self.postings.get(t, ())
            if not plist:
                continue
            idf = math.log(1 + (n - len(plist) + 0.5) / (len(plist) + 0.5))
            for cid, tf in plist:
                dl = sum(self.bags[cid].values())
                scores[cid] += idf * tf * (k1 + 1) / (tf + k1 * (1 - b + b * dl / self.avglen))
        return scores

    def search(self, query, k=8, hops=2, spread=0.5):
        """Keyword match first, then let the score flow along associations."""
        direct = self.bm25(query)
        if not direct:
            return []
        top = max(direct.values())
        seeds = dict(sorted(direct.items(), key=lambda kv: -kv[1])[:30])
        score = {cid: s / top for cid, s in direct.items()}
        why = defaultdict(list)
        frontier = {cid: s / top for cid, s in seeds.items()}
        for h in range(hops):
            nxt = defaultdict(float)
            for cid, s in frontier.items():
                nbrs = self.edges.get(cid, {})
                total = sum(w for w, _ in nbrs.values()) or 1.0
                for other, (w, kinds) in nbrs.items():
                    gain = spread * s * w / max(total, 1.0)
                    if gain > 0.01:
                        nxt[other] += gain
                        if len(why[other]) < 3:
                            why[other].append(f"{next(iter(kinds.values()))} ← {self.chunks[cid]['name'] or cid}")
            for cid, g in nxt.items():
                score[cid] = score.get(cid, 0.0) + g
            frontier = nxt
        ranked = sorted(score.items(), key=lambda kv: -kv[1])[:k]
        return [{"id": cid, "score": round(s, 3), "matched": cid in direct,
                 "why": why.get(cid, [])} for cid, s in ranked]

    def related(self, cid, k=12):
        nbrs = self.edges.get(cid, {})
        return [{"id": o, "weight": round(w, 3), "kinds": kinds}
                for o, (w, kinds) in sorted(nbrs.items(), key=lambda kv: -kv[1][0])[:k]]

    # -- disk ----------------------------------------------------------------
    def save(self):
        os.makedirs(self.dir, exist_ok=True)
        _write_jsonl(os.path.join(self.dir, "chunks.jsonl"),
                     [c for c in self.chunks.values() if c["kind"] not in ("note", "concept")])
        rows = [{"a": a, "b": b, "weight": round(w, 4), "kinds": kinds}
                for a, nbrs in self.edges.items() for b, (w, kinds) in nbrs.items() if a < b]
        _write_jsonl(os.path.join(self.dir, "associations.jsonl"), rows)
        with open(os.path.join(self.dir, "files.json"), "w") as f:
            json.dump(self.files, f)

    @classmethod
    def load(cls, root):
        g = cls(root)
        try:
            with open(os.path.join(g.dir, "files.json")) as f:
                g.files = json.load(f)
        except FileNotFoundError:
            return g.build()
        for c in _read_jsonl(os.path.join(g.dir, "chunks.jsonl")):
            g.chunks[c["id"]] = c
        g._load_memory()
        g._associate()
        return g


def _read_jsonl(path):
    try:
        with open(path) as f:
            return [json.loads(line) for line in f if line.strip()]
    except FileNotFoundError:
        return []


def _write_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    os.replace(tmp, path)
