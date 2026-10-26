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

# Worded unlike the code on purpose: few of these words appear in the answer.
PARAPHRASED = {
    "email": [
        ("pick a random separator that does not clash with the body text", {"generator.py"}),
        ("turn a point in time into the textual form used in mail headers", {"utils.py"}),
        ("go through every nested piece of a mail, depth first", {"iterators.py", "message.py"}),
        ("convert =XX style escaped text back to raw bytes", {"quoprimime.py"}),
        ("split a header line that is too wide over several lines", {"_header_value_parser.py", "header.py", "policy.py", "_policybase.py"}),
        ("record problems found while reading a broken mail", {"errors.py", "feedparser.py"}),
        ("read mail incrementally as data arrives in pieces", {"feedparser.py"}),
        ("who is the mail addressed to: names and mailboxes", {"_parseaddr.py", "utils.py", "headerregistry.py", "_header_value_parser.py"}),
    ],
    "asyncio": [
        ("stop waiting after some seconds and give up", {"timeouts.py", "tasks.py"}),
        ("limit how many coroutines run at the same time", {"locks.py"}),
        ("producer consumer buffer between coroutines", {"queues.py"}),
        ("start an external program without blocking", {"subprocess.py", "base_subprocess.py", "unix_events.py"}),
        ("encrypted connection setup", {"sslproto.py"}),
        ("run several coroutines concurrently and collect what they return", {"tasks.py"}),
        ("placeholder for a value that will be available later", {"futures.py"}),
        ("if one child job crashes, abort its siblings", {"taskgroups.py"}),
    ],
}

from .graph import Graph


def _files(g, query, k, hops):
    return [g.chunks[h["id"]]["path"] for h in g.search(query, k=k, hops=hops)]


def main(ks=(1, 3, 5)):
    for package, cases in SUITES.items():
        src = os.path.join(sysconfig.get_paths()["stdlib"], package)
        with tempfile.TemporaryDirectory() as tmp:
            root = os.path.join(tmp, package)
            shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__"))
            base = {q: keyword_baseline(root, q, max(ks)) for q, _ in cases + PARAPHRASED[package]}
            g = Graph(root).build()
            print(f"\n{package}: {len(g.chunks)} chunks, "
                  f"{sum(len(v) for v in g.edges.values()) // 2} associations")
            for title, qs in (("questions", cases), ("paraphrased", PARAPHRASED[package])):
                print(f"  {title} ({len(qs)})".ljust(30) + "  ".join(f"k={k}" for k in ks))
                rows = {"keywords": lambda q, k: base[q][:k],
                        "chunks": lambda q, k: _files(g, q, k, 0),
                        "chunks+assoc": lambda q, k: _files(g, q, k, 2)}
                for label, fn in rows.items():
                    cells = [sum(bool(want & set(fn(q, k))) for q, want in qs) for k in ks]
                    print(f"    {label:<24}" + "  ".join(f"{c:3d}" for c in cells))


if __name__ == "__main__":
    main()
