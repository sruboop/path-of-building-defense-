"""Strings: chains of hops between black holes.

A string starts at a token and hops along associations, each hop landing on
another token. The sequence of locations it visits is its oscillation; the
string's own location is the sum of those locations, each bound to its
position in the chain. Strings that keep being formed are reinforced
(their count grows). Strings that share a black hole touch.
"""
import math

from .blackholes import DIM, bag, location


def canonical(tokens):
    """A string is the same whichever end you read it from."""
    tokens = tuple(tokens)
    return min(tokens, tokens[::-1])


def oscillation(tokens):
    acc = [0.0] * DIM
    for i, t in enumerate(tokens):
        loc = location(t)
        k = i % DIM
        rolled = loc[-k:] + loc[:-k] if k else loc
        for j, a in enumerate(rolled):
            acc[j] += a
    n = math.sqrt(sum(a * a for a in acc)) or 1.0
    return [a / n for a in acc]


class String:
    __slots__ = ("tokens", "count", "evidence")

    def __init__(self, tokens, evidence, count=0):
        self.tokens = tokens
        self.evidence = evidence      # per hop: the [file id, line] spots where it happens
        self.count = count

    def vector(self):
        return bag(self.tokens)

    def __str__(self):
        return " ~> ".join(self.tokens)


class Strings:
    def __init__(self):
        self.by_key = {}
        self.through = {}             # black hole -> keys of strings passing it

    def __len__(self):
        return len(self.by_key)

    def add(self, tokens, evidence):
        key = canonical(tokens)
        s = self.by_key.get(key)
        if s is None:
            if key != tuple(tokens):
                evidence = evidence[::-1]
            s = self.by_key[key] = String(key, evidence)
            for t in key:
                self.through.setdefault(t, set()).add(key)
        s.count += 1
        return s

    def touching(self, tokens):
        keys = set()
        for t in tokens:
            keys |= self.through.get(t, set())
        return [self.by_key[k] for k in keys]

    def density(self, token):
        """How many strings pass through a black hole."""
        return len(self.through.get(token, ()))

    def to_json(self):
        return [[list(s.tokens), s.evidence, s.count] for s in self.by_key.values()]

    @classmethod
    def from_json(cls, rows):
        out = cls()
        for tokens, evidence, count in rows:
            key = tuple(tokens)
            out.by_key[key] = String(key, evidence, count)
            for t in key:
                out.through.setdefault(t, set()).add(key)
        return out


def hop(space, start, rng, length, laws=None, avoid=()):
    """Walk from a black hole along associations; laws act as shortcuts."""
    path = [start]
    seen = {start, *avoid}
    while len(path) < length:
        cur = path[-1]
        jump = laws.shortcut(cur, seen, rng) if laws else None
        if jump:
            path += jump
            seen.update(jump)
            continue
        options = [(b, s) for b, s in space.neighbours.get(cur, []) if b not in seen]
        if not options:
            break
        total = sum(s * s for _, s in options)
        r = rng.random() * total
        for b, s in options:
            r -= s * s
            if r <= 0:
                break
        path.append(b)
        seen.add(b)
    if len(path) < 3:
        return None, None
    path = path[:length + 2]
    evidence = [space.evidence(a, b) for a, b in zip(path, path[1:])]
    return path, evidence


def bridge(space, a, b, paths=3):
    """Connect two black holes with short chains of hops (at most 3 hops).

    Every path is scored by the product of its association strengths; the
    strongest few become strings.
    """
    na = dict(space.neighbours.get(a, []))
    nb = dict(space.neighbours.get(b, []))
    found = []
    if b in na:
        found.append((na[b], [a, b]))
    for x, sx in na.items():
        if x in nb and x != b:
            found.append((sx * nb[x], [a, x, b]))
        for y, sy in space.neighbours.get(x, []):
            if y in nb and y not in (a, b, x):
                found.append((sx * sy * nb[y], [a, x, y, b]))
    found.sort(key=lambda f: -f[0])
    out = []
    for _, path in found[:paths]:
        out.append((path, [space.evidence(p, q) for p, q in zip(path, path[1:])]))
    return out
