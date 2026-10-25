"""The mathematical space: every chunk has a location (a unit vector).

Locations start random and drift: chunks that keep appearing together in
laws are pulled toward each other, so cosine similarity becomes meaningful
over time.
"""
import math
import random

DIM = 64


def _unit(v):
    n = math.sqrt(sum(a * a for a in v)) or 1.0
    return [a / n for a in v]


def cosine(u, v):
    return sum(a * b for a, b in zip(u, v))


def roll(v, k):
    k %= len(v)
    return v[-k:] + v[:-k] if k else v[:]


class Space:
    def __init__(self, seed=0):
        self.seed = seed
        self.loc = {}

    def place(self, chunk):
        if chunk not in self.loc:
            rng = random.Random(f"{self.seed}:{chunk}")
            self.loc[chunk] = _unit([rng.gauss(0, 1) for _ in range(DIM)])
        return self.loc[chunk]

    def attract(self, chunks, rate=0.05):
        """Pull co-lawful chunks toward their common centre."""
        vecs = [self.place(c) for c in chunks]
        centre = [sum(col) / len(vecs) for col in zip(*vecs)]
        for c, v in zip(chunks, vecs):
            self.loc[c] = _unit([a + rate * (m - a) for a, m in zip(v, centre)])

    def string_vector(self, chain):
        """Associative location of an ordered chain: position-bound sum."""
        acc = [0.0] * DIM
        for i, c in enumerate(chain):
            for j, a in enumerate(roll(self.place(c), i)):
                acc[j] += a
        return _unit(acc)

    def bag_vector(self, chunks):
        acc = [0.0] * DIM
        for c in chunks:
            for j, a in enumerate(self.place(c)):
                acc[j] += a
        return _unit(acc)
