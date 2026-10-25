"""Tokens are black holes: fixed points in a mathematical space.

Every token in the repository gets a random location (a unit vector seeded
by the token itself). Locations never move. What gives tokens meaning is
not where they sit but which strings pass through them.

Associations between pairs of tokens come from the repository alone: two
tokens are associated when they appear on the same or adjacent lines. The
strength is normalised so that tokens appearing everywhere do not swallow
every association.
"""
import math
import os
import random
import re
from collections import Counter
from itertools import combinations

DIM = 64
NEIGHBOURS = 24        # strongest associations kept per token
OCCURRENCES = 16       # lines remembered per token per file
TOKENS_PER_LINE = 40
WINDOW = 10            # lines per window of text that can be handed out as context
MAX_FILE_BYTES = 1_000_000
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".stringspace", "venv",
             ".venv", "dist", "build", ".mypy_cache", ".pytest_cache"}
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip", ".gz",
              ".tar", ".whl", ".so", ".dll", ".exe", ".pyc", ".woff", ".woff2",
              ".ttf", ".mp4", ".mp3", ".lock", ".bin", ".db", ".sqlite"}
STOP = set("""
a an and are as at be but by do does for from has have if in into is it its
of on or not no so than that the their then there these this those to was
were will with you your we our can may should would could also just only
def class return self none true false import pass else elif while try except
finally raise with lambda yield async await var let const function new null
undefined end local nil end begin public private static void int str string
how what why where when which who whom does did done want need make
""".split())

WORD = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
CAMEL = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|\d+")


def tokens_of(text):
    """Words, split on snake_case and camelCase; compound names kept whole too."""
    out = []
    for word in WORD.findall(text):
        parts = [p.lower() for piece in word.split("_") for p in CAMEL.findall(piece)]
        if len(parts) > 1:
            parts.append(word.lower())
        out += [t for t in parts if len(t) > 1 and t not in STOP and not t.isdigit()]
    return out


def location(token, seed=0):
    rng = random.Random(f"{seed}:{token}")
    v = [rng.gauss(0, 1) for _ in range(DIM)]
    n = math.sqrt(sum(a * a for a in v))
    return [a / n for a in v]


def unit(v):
    n = math.sqrt(sum(a * a for a in v)) or 1.0
    return [a / n for a in v]


def cosine(u, v):
    return sum(a * b for a, b in zip(u, v))


def bag(tokens, weights=None):
    acc = [0.0] * DIM
    for t in tokens:
        w = weights.get(t, 1.0) if weights else 1.0
        for i, a in enumerate(location(t)):
            acc[i] += w * a
    return unit(acc)


def repository_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            if os.path.splitext(name)[1].lower() in BINARY_EXT:
                continue
            try:
                if os.path.getsize(path) > MAX_FILE_BYTES:
                    continue
                with open(path, encoding="utf-8") as f:
                    yield os.path.relpath(path, root), f.read().splitlines()
            except (UnicodeDecodeError, OSError):
                continue


class Space:
    def __init__(self):
        self.root = None
        self.files = []        # file id -> relative path
        self.occ = {}          # token -> [[file id, line], ...]
        self.df = Counter()    # token -> number of lines it appears on
        self.neighbours = {}   # token -> [[token, strength], ...]
        self.windows = []      # window id -> [file id, first line]
        self.postings = {}     # token -> [[window id, count], ...]

    def build(self, root):
        self.root = os.path.abspath(root)
        pairs = Counter()
        for fid, (path, lines) in enumerate(repository_files(self.root)):
            self.files.append(path)
            prev = set()
            for ln, text in enumerate(lines, 1):
                if (ln - 1) % WINDOW == 0:
                    wid = len(self.windows)
                    self.windows.append([fid, ln])
                    counts = Counter()
                    self._index_window(wid, counts, lines[ln - 1:ln - 1 + WINDOW])
                cur = set(tokens_of(text)[:TOKENS_PER_LINE]) | set(tokens_of(path)[:4] if ln == 1 else [])
                for t in cur:
                    self.df[t] += 1
                    spots = self.occ.setdefault(t, [])
                    if sum(1 for f, _ in spots[-OCCURRENCES:] if f == fid) < OCCURRENCES:
                        spots.append([fid, ln])
                for a, b in combinations(sorted(cur), 2):
                    pairs[(a, b)] += 1
                for a in cur:
                    for b in prev - cur:
                        pairs[(a, b) if a < b else (b, a)] += 1
                prev = cur
        table = {}
        for (a, b), w in pairs.items():
            s = w / math.sqrt(self.df[a] * self.df[b])
            table.setdefault(a, []).append((s, b))
            table.setdefault(b, []).append((s, a))
        self.neighbours = {t: [[b, round(s, 4)] for s, b in sorted(ns, reverse=True)[:NEIGHBOURS]]
                           for t, ns in table.items()}
        return self

    def _index_window(self, wid, counts, lines):
        for text in lines:
            counts.update(tokens_of(text))
        for t, c in counts.items():
            self.postings.setdefault(t, []).append([wid, c])

    def window_of(self, fid, ln):
        return fid, (ln - 1) // WINDOW * WINDOW + 1

    def evidence(self, a, b, limit=12):
        """Where in the repository a and b sit together: [[file id, line], ...],
        spread across files (one spot per file before a second one)."""
        spots_b = {}
        for fid, ln in self.occ.get(b, []):
            spots_b.setdefault(fid, set()).add(ln)
        per_file = {}
        for fid, ln in self.occ.get(a, []):
            lines = spots_b.get(fid)
            if lines and (ln in lines or ln - 1 in lines or ln + 1 in lines):
                per_file.setdefault(fid, []).append(ln)
        out, depth = [], 0
        while len(out) < limit and any(len(v) > depth for v in per_file.values()):
            for fid, lns in per_file.items():
                if len(lns) > depth and len(out) < limit:
                    out.append([fid, lns[depth]])
            depth += 1
        if not out:
            spots = self.occ.get(a) or self.occ.get(b)
            out = [list(spots[0])] if spots else []
        return out

    def to_json(self):
        return {"root": self.root, "files": self.files, "occ": self.occ,
                "df": dict(self.df), "neighbours": self.neighbours,
                "windows": self.windows, "postings": self.postings}

    @classmethod
    def from_json(cls, d):
        s = cls()
        s.root, s.files, s.occ = d["root"], d["files"], d["occ"]
        s.df, s.neighbours = Counter(d["df"]), d["neighbours"]
        s.windows, s.postings = d["windows"], d["postings"]
        return s
