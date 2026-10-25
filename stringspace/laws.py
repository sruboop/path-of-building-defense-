"""Laws: what many strings agree on.

When the same run of hops shows up inside many different strings, that run
is no longer a coincidence of random walking: it is a law. Laws are used as
shortcuts (a walk that reaches a law's first token can take the whole law in
one jump) and as strong evidence when choosing context.
"""
from collections import Counter

from .strings import canonical

SIZES = (3, 4, 5)


class Laws:
    def __init__(self, min_support=3):
        self.min_support = min_support
        self.support = {}             # law (tuple of tokens) -> distinct strings
        self.starts = {}              # token -> laws readable from it
        self.passing = {}             # token -> laws passing through it

    def __len__(self):
        return len(self.support)

    def mine(self, strings):
        seen = Counter()
        for s in strings.by_key.values():
            subs = set()
            for n in SIZES:
                for i in range(len(s.tokens) - n + 1):
                    subs.add(canonical(s.tokens[i:i + n]))
            seen.update(subs)
        found = {k: c for k, c in seen.items() if c >= self.min_support}
        # Occam: keep a shorter law only if it is backed by more strings than
        # every longer law that contains it.
        for law in sorted(found, key=len, reverse=True):
            if law not in found:
                continue
            for n in range(3, len(law)):
                for i in range(len(law) - n + 1):
                    sub = canonical(law[i:i + n])
                    if sub in found and found[sub] <= found[law]:
                        del found[sub]
        self.support = found
        self._index()
        return self

    def _index(self):
        self.starts, self.passing = {}, {}
        for law in self.support:
            for direction in (law, law[::-1]):
                self.starts.setdefault(direction[0], []).append(direction)
            for t in law:
                self.passing.setdefault(t, []).append(law)

    def shortcut(self, token, seen, rng):
        options = [l for l in self.starts.get(token, ()) if not seen & set(l[1:])]
        if not options or rng.random() < 0.5:
            return None
        law = max(options, key=lambda l: self.support[canonical(l)] + rng.random())
        return list(law[1:])

    def through(self, tokens):
        """Laws passing through any of these black holes."""
        out = set()
        for t in tokens:
            out.update(canonical(l) for l in self.passing.get(t, ()))
        return out

    def to_json(self):
        return [[list(k), v] for k, v in self.support.items()]

    def load(self, rows):
        self.support = {tuple(k): v for k, v in rows}
        self._index()
        return self
