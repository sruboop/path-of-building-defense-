"""Does hopping find the right file? A small benchmark on Python's own `email`
package, compared with plain keyword search over the same lines.

    python3 -m stringspace.bench
"""
import math
import os
import shutil
import sysconfig
import tempfile
from collections import Counter, defaultdict

from .blackholes import repository_files, tokens_of
from .context import ask
from .state import State

EMAIL = [
    ("how is a multipart message boundary generated", {"generator.py"}),
    ("decode quoted printable body text", {"quoprimime.py"}),
    ("parse a list of email addresses from a header", {"_parseaddr.py", "utils.py", "_header_value_parser.py"}),
    ("base64 encode a header value", {"base64mime.py"}),
    ("which codec converts a charset for header encoding", {"charset.py"}),
    ("set the payload of a message", {"message.py"}),
    ("feed parser receiving incomplete lines", {"feedparser.py"}),
    ("format a date for an rfc 2822 header", {"utils.py"}),
    ("walk over all subparts of a message", {"iterators.py", "message.py"}),
    ("content manager get text content", {"contentmanager.py"}),
    ("folding long headers to max line length", {"_header_value_parser.py", "header.py", "_policybase.py", "policy.py"}),
    ("attach a file to a mime message", {"mime/base.py", "mime/application.py", "mime/multipart.py", "message.py", "contentmanager.py"}),
]

# Held out: never used while tuning.
ASYNCIO = [
    ("create a subprocess and read its output", {"subprocess.py", "base_subprocess.py", "unix_events.py"}),
    ("schedule a callback after a delay on the event loop", {"base_events.py", "events.py"}),
    ("cancel a running task", {"tasks.py"}),
    ("queue with a maximum size where put waits", {"queues.py"}),
    ("acquire and release a semaphore", {"locks.py"}),
    ("open a tcp connection with a stream reader and writer", {"streams.py"}),
    ("ssl handshake over a transport", {"sslproto.py"}),
    ("run a coroutine until complete from synchronous code", {"runners.py", "base_events.py"}),
    ("timeout context manager", {"timeouts.py", "tasks.py"}),
    ("gather the results of several awaitables", {"tasks.py"}),
    ("future set result and run done callbacks", {"futures.py"}),
    ("task group cancels the other tasks when one fails", {"taskgroups.py"}),
]

SUITES = {"email": EMAIL, "asyncio": ASYNCIO}


def keyword_baseline(root, query, k):
    """TF-IDF over 10-line windows: the no-hops reference."""
    windows, df = [], Counter()
    for path, lines in repository_files(root):
        for i in range(0, len(lines), 10):
            toks = Counter(tokens_of("\n".join(lines[i:i + 10])))
            windows.append((path, toks))
            df.update(toks.keys())
    q = set(tokens_of(query))
    n = len(windows)
    scored = []
    for path, toks in windows:
        s = sum((1 + math.log(toks[t])) * math.log(n / df[t]) for t in q if t in toks)
        scored.append((s, path))
    scored.sort(reverse=True)
    return [p for s, p in scored[:k] if s > 0]


def evaluate(package, cases, k=3, seeds=4, hop_weights=(0.0, 0.1)):
    src = os.path.join(sysconfig.get_paths()["stdlib"], package)
    with tempfile.TemporaryDirectory() as tmp:
        root = os.path.join(tmp, package)
        shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__"))
        base = sum(bool(want & set(keyword_baseline(root, q, k))) for q, want in cases)
        print(f"\n{package}: right file in top {k} (of {len(cases)} questions)")
        print(f"  keyword search (no hops)        : {base}")
        for hw in hop_weights:
            runs = []
            for seed in range(seeds):
                state = State.build(root, seed=seed)
                runs.append(sum(bool(want & {s["file"] for s in
                                             ask(state, q, k=k, seed=seed, hop_weight=hw)["snippets"]})
                                for q, want in cases))
            print(f"  strings, hop weight {hw:<4}        : {sum(runs) / seeds:.1f} "
                  f"(seeds: {runs})")


def main():
    for package, cases in SUITES.items():
        evaluate(package, cases)


if __name__ == "__main__":
    main()
