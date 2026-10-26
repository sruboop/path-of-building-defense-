"""Right file in the top results? Same questions as stringspace.bench
(email used during tuning, asyncio held out), three ways:

  keywords      TF-IDF over 10-line windows (no chunks, no associations)
  chunks        BM25 over meaningful chunks, no associations
  chunks+assoc  BM25, then scores flow 2 hops along the associations

    python3 -m codegraph.bench
"""
import os
import shutil
import sysconfig
import tempfile

from stringspace.bench import SUITES, keyword_baseline

from .graph import Graph


def _files(g, query, k, hops):
    return [g.chunks[h["id"]]["path"] for h in g.search(query, k=k, hops=hops)]


def main(ks=(1, 3, 5)):
    for package, cases in SUITES.items():
        src = os.path.join(sysconfig.get_paths()["stdlib"], package)
        with tempfile.TemporaryDirectory() as tmp:
            root = os.path.join(tmp, package)
            shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__"))
            g = Graph(root).build()
            print(f"\n{package}: {len(g.chunks)} chunks, "
                  f"{sum(len(v) for v in g.edges.values()) // 2} associations")
            print("  top-k            " + "  ".join(f"k={k}" for k in ks))
            rows = {
                "keywords    ": lambda q, k: keyword_baseline(root, q, k),
                "chunks      ": lambda q, k: _files(g, q, k, 0),
                "chunks+assoc": lambda q, k: _files(g, q, k, 2),
            }
            for label, fn in rows.items():
                cells = [sum(bool(want & set(fn(q, k))) for q, want in cases) for k in ks]
                print(f"  {label}     " + "  ".join(f"{c:2d}/{len(cases)}" for c in cells))


if __name__ == "__main__":
    main()
