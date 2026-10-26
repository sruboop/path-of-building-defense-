"""Embeddings: every chunk (and note) becomes a vector; closeness = meaning.

Optional, and needs numpy. Pick a backend with `build --embeddings SPEC`
(remembered in .codegraph/config.json) or the CODEGRAPH_EMBEDDINGS variable:

  fastembed[:MODEL]     local ONNX model, `pip install fastembed`
                        (default BAAI/bge-small-en-v1.5; for code try
                        jinaai/jina-embeddings-v2-base-code)
  ollama[:MODEL]        local Ollama server (default nomic-embed-text)
  voyage[:MODEL]        Voyage AI API, VOYAGE_API_KEY (default voyage-code-3)
  openai[:MODEL]        OpenAI API, OPENAI_API_KEY (default text-embedding-3-small)
  lsa[:DIM]             built in, no download: latent semantic analysis learned
                        from the repository itself (weaker; knows only the
                        repo's own words)

Vectors are cached by chunk content hash in .codegraph/vectors.npy, so after
an edit only the changed chunks are embedded again.
"""
import json
import math
import os
import urllib.request

DEFAULTS = {"fastembed": "BAAI/bge-small-en-v1.5", "ollama": "nomic-embed-text",
            "voyage": "voyage-code-3", "openai": "text-embedding-3-small", "lsa": "192"}
MAX_CHARS = 4000
BATCH = 64


def chunk_text(c):
    return f"{c['path']} {c['kind']} {c['name']}\n{c['text'][:MAX_CHARS]}"


def _post(url, payload, headers):
    req = urllib.request.Request(url, json.dumps(payload).encode(),
                                 {"Content-Type": "application/json", **headers})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


class Embedder:
    """Base: subclasses implement _embed(texts, kind) -> list of vectors."""
    corpus_fitted = False   # True when vectors depend on the whole corpus (lsa)

    def __init__(self, spec):
        backend, _, model = spec.partition(":")
        self.backend, self.model = backend, model or DEFAULTS[backend]
        self.spec = f"{self.backend}:{self.model}"

    def embed(self, texts, kind="document"):
        import numpy as np
        out = []
        for i in range(0, len(texts), BATCH):
            out += self._embed(texts[i:i + BATCH], kind)
        m = np.asarray(out, dtype=np.float32).reshape(len(texts), -1)
        return m / np.maximum(np.linalg.norm(m, axis=1, keepdims=True), 1e-9)


class FastEmbed(Embedder):
    def __init__(self, spec):
        super().__init__(spec)
        from fastembed import TextEmbedding
        self.m = TextEmbedding(self.model)

    def _embed(self, texts, kind):
        if kind == "query" and hasattr(self.m, "query_embed"):
            return list(self.m.query_embed(texts))
        return list(self.m.embed(texts))


class Ollama(Embedder):
    def _embed(self, texts, kind):
        host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        return _post(f"{host}/api/embed", {"model": self.model, "input": texts}, {})["embeddings"]


class Voyage(Embedder):
    def _embed(self, texts, kind):
        r = _post("https://api.voyageai.com/v1/embeddings",
                  {"model": self.model, "input": texts, "input_type": kind},
                  {"Authorization": f"Bearer {os.environ['VOYAGE_API_KEY']}"})
        return [d["embedding"] for d in r["data"]]


class OpenAI(Embedder):
    def _embed(self, texts, kind):
        r = _post("https://api.openai.com/v1/embeddings", {"model": self.model, "input": texts},
                  {"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"})
        return [d["embedding"] for d in sorted(r["data"], key=lambda d: d["index"])]


class LSA(Embedder):
    """TF-IDF over the repo's terms, reduced by SVD: words that keep appearing
    in the same chunks end up close, even when a query uses only one of them."""
    corpus_fitted = True
    VOCAB = 6000

    def fit(self, bags):
        import numpy as np
        df = {}
        for b in bags:
            for t in b:
                df[t] = df.get(t, 0) + 1
        n = len(bags)
        vocab = [t for t, d in sorted(df.items(), key=lambda kv: -kv[1]) if 1 < d < 0.5 * n][:self.VOCAB]
        self.index = {t: i for i, t in enumerate(vocab)}
        self.idf = np.array([math.log(n / df[t]) for t in vocab], dtype=np.float32)
        x = self._matrix(bags)
        k = min(int(self.model), max(1, min(x.shape) - 1))
        gram = x.T @ x                    # vocab x vocab, cheaper than a full SVD
        vals, vecs = np.linalg.eigh(gram)
        top = np.argsort(vals)[::-1][:k]
        self.proj = vecs[:, top] / np.sqrt(np.maximum(vals[top], 1e-9))
        return self

    def _matrix(self, bags):
        import numpy as np
        x = np.zeros((len(bags), len(self.index)), dtype=np.float32)
        for r, b in enumerate(bags):
            for t, c in b.items():
                j = self.index.get(t)
                if j is not None:
                    x[r, j] = (1 + math.log(c)) * self.idf[j]
        return x

    def embed_bags(self, bags):
        import numpy as np
        m = self._matrix(bags) @ self.proj
        return m / np.maximum(np.linalg.norm(m, axis=1, keepdims=True), 1e-9)


BACKENDS = {"fastembed": FastEmbed, "ollama": Ollama, "voyage": Voyage, "openai": OpenAI, "lsa": LSA}


def make(spec):
    if not spec:
        return None
    backend = spec.partition(":")[0]
    if backend not in BACKENDS:
        raise ValueError(f"unknown embeddings backend {backend!r}; pick one of {', '.join(BACKENDS)}")
    return BACKENDS[backend](spec)


class VectorStore:
    """chunk id -> unit vector, cached by content hash."""

    def __init__(self, directory, embedder):
        self.dir = directory
        self.embedder = embedder
        self.ids, self.matrix = [], None
        self._cache = {}       # hash -> vector
        self._load()

    def _paths(self):
        return os.path.join(self.dir, "vectors.npy"), os.path.join(self.dir, "vectors.json")

    def _load(self):
        import numpy as np
        npy, meta = self._paths()
        try:
            with open(meta) as f:
                m = json.load(f)
            if m.get("spec") != self.embedder.spec or self.embedder.corpus_fitted:
                return
            vecs = np.load(npy)
            self._cache = dict(zip(m["hashes"], vecs))
        except (FileNotFoundError, ValueError, OSError):
            pass

    def update(self, chunks, bags):
        """Embed whatever is new; returns how many chunks needed embedding."""
        import numpy as np
        self.ids = list(chunks)
        if self.embedder.corpus_fitted:
            self.embedder.fit([bags[i] for i in self.ids])
            self.matrix = self.embedder.embed_bags([bags[i] for i in self.ids])
            return len(self.ids)
        hashes = [_hash(chunks[i]) for i in self.ids]
        todo = [(i, h) for i, h in zip(self.ids, hashes) if h not in self._cache]
        if todo:
            vecs = self.embedder.embed([chunk_text(chunks[i]) for i, _ in todo])
            for (_, h), v in zip(todo, vecs):
                self._cache[h] = v
        self.matrix = np.stack([self._cache[h] for h in hashes]) if hashes else None
        self._cache = {h: self._cache[h] for h in hashes}
        self._save(hashes)
        return len(todo)

    def _save(self, hashes):
        import numpy as np
        npy, meta = self._paths()
        os.makedirs(self.dir, exist_ok=True)
        if self.matrix is not None:
            np.save(npy, self.matrix)
        with open(meta, "w") as f:
            json.dump({"spec": self.embedder.spec, "hashes": hashes}, f)

    def query(self, text, bag=None):
        if self.embedder.corpus_fitted:
            return self.embedder.embed_bags([bag])[0]
        return self.embedder.embed([text], kind="query")[0]

    def neighbours(self, k):
        """Top-k most similar chunks for every chunk: (row, col, cosine)."""
        import numpy as np
        if self.matrix is None or len(self.ids) < 2:
            return
        m = self.matrix
        for start in range(0, len(m), 512):
            sims = m[start:start + 512] @ m.T
            for r in range(sims.shape[0]):
                sims[r, start + r] = -1.0
            top = np.argpartition(-sims, min(k, sims.shape[1] - 1), axis=1)[:, :k]
            for r in range(sims.shape[0]):
                for c in top[r]:
                    yield start + r, int(c), float(sims[r, c])


def _hash(c):
    import hashlib
    return hashlib.sha1(chunk_text(c).encode()).hexdigest()[:16]
