"""Strings and laws.

A *string* is a random chain of chunks: antecedent chunks -> consequence.
Most strings are noise. A string becomes a *law* only when experience backs
it: it fired often enough (support) and was right often enough (confidence).
All laws are strings; most strings never become laws.

Two kinds of strings:
  temporal  chunks of a moment (+ the button pressed) -> a change that follows
  sync      chunks of a moment -> another chunk of that same moment (reward)
"""
import math

from space import cosine

REWARD = "reward=1"
RULES = {  # kind: (min support, min confidence)
    "temporal": (4, 0.8),
    "sync": (2, 0.95),
}
PRIOR_CAP = 4  # inherited laws count as at most this many past observations


class Law:
    def __init__(self, kind, antecedent, consequence):
        self.kind = kind
        self.antecedent = tuple(sorted(antecedent))
        self.consequence = consequence
        self.hits = self.n = 0
        self.prior_hits = self.prior_n = 0.0
        self.vector = None

    @property
    def key(self):
        return (self.kind, self.antecedent, self.consequence)

    @property
    def chain(self):
        return self.antecedent + (self.consequence,)

    @property
    def confidence(self):
        n = self.n + self.prior_n
        return (self.hits + self.prior_hits) / n if n else 0.0

    @property
    def support(self):
        return self.n + self.prior_n

    def __str__(self):
        return " —> ".join(self.chain) + f"   [conf {self.confidence:.2f}, n {self.support:.0f}]"


class Memory:
    """Experience of the current universe with inverted indexes for fast testing."""

    def __init__(self):
        self.size = 0
        self.rewarded = []
        self.index = {"temporal": ({}, {}), "sync": ({}, {})}
        self.vocabulary = set()

    def _add(self, kind, side, tokens, tid):
        table = self.index[kind][side]
        for t in tokens:
            table.setdefault(t, set()).add(tid)

    def record(self, pre, action, post, delta, reward):
        tid = self.size
        self.size += 1
        self._add("temporal", 0, pre | {action}, tid)
        self._add("temporal", 1, delta, tid)
        self._add("sync", 0, post, tid)
        if reward:
            self._add("sync", 1, {REWARD}, tid)
            self.rewarded.append(tid)
        self.vocabulary |= pre | post | delta | {action}
        return tid

    def measure(self, law):
        ante, cons = self.index[law.kind]
        ids = None
        for t in law.antecedent:
            s = ante.get(t, set())
            ids = s if ids is None else ids & s
            if not ids:
                return 0, 0
        if ids is None:
            ids = set(range(self.size))
        return len(ids & cons.get(law.consequence, set())), len(ids)


class LawBook:
    def __init__(self, space, rng):
        self.space = space
        self.rng = rng
        self.laws = {}
        self.strings_tried = 0
        self.laws_born = 0
        self.laws_falsified = 0

    # -- forming strings -------------------------------------------------
    def random_string(self, mem, moments):
        rng = self.rng
        if rng.random() < 0.15:  # a pure shot in the dark between any chunks
            vocab = sorted(mem.vocabulary)
            ante = rng.sample(vocab, rng.randint(1, 2))
            return Law("temporal", ante, rng.choice(vocab))
        if mem.rewarded and rng.random() < 0.35:
            pre, act, post, delta = moments[rng.choice(mem.rewarded)]
            pool = sorted(post - {REWARD})
            return Law("sync", rng.sample(pool, rng.randint(1, 2)), REWARD)
        pre, act, post, delta = moments[rng.randrange(len(moments))]
        if not delta:
            return None
        ante = rng.sample(sorted(pre), rng.choice([0, 0, 1, 1, 2]))
        if rng.random() < 0.85:
            ante.append(act)
        return Law("temporal", ante, rng.choice(sorted(delta)))

    def _redundant(self, law):
        for other in self.laws.values():
            if (other.kind == law.kind and other.consequence == law.consequence
                    and set(other.antecedent) < set(law.antecedent)
                    and other.confidence >= law.confidence - 0.05):
                return True
        return False

    def _lawful(self, law):
        support, conf = RULES[law.kind]
        return law.support >= support and law.confidence >= conf

    def _enshrine(self, law):
        self.laws[law.key] = law
        law.vector = self.space.string_vector(law.chain)
        self.space.attract(law.chain)
        self.laws_born += 1
        # Occam: a simpler law that explains as well retires the complex ones.
        for k, other in list(self.laws.items()):
            if (other is not law and other.kind == law.kind
                    and other.consequence == law.consequence
                    and set(law.antecedent) < set(other.antecedent)
                    and law.confidence >= other.confidence - 0.05):
                del self.laws[k]

    def explore(self, mem, moments, tries):
        for _ in range(tries):
            law = self.random_string(mem, moments)
            if law is None or law.key in self.laws:
                continue
            self.strings_tried += 1
            law.hits, law.n = mem.measure(law)
            if self._lawful(law) and not self._redundant(law):
                self._enshrine(law)

    def retest(self, mem):
        """Science: every law is re-measured; the ones experience contradicts die."""
        for k, law in list(self.laws.items()):
            law.hits, law.n = mem.measure(law)
            support, conf = RULES[law.kind]
            if law.support >= support and law.confidence < conf - 0.15:
                del self.laws[k]
                self.laws_falsified += 1

    def carry_over(self):
        """Entering a new universe: past evidence becomes a capped prior."""
        for law in self.laws.values():
            n = law.n + law.prior_n
            if n:
                scale = min(1.0, PRIOR_CAP / n)
                law.prior_hits = (law.hits + law.prior_hits) * scale
                law.prior_n = n * scale
            law.hits = law.n = 0

    # -- thought -----------------------------------------------------------
    def applicable(self, tokens):
        return [l for l in self.laws.values() if set(l.antecedent) <= tokens]

    def thought(self, tokens, k=5):
        """Laws whose location is nearest the present moment, weighted by belief."""
        here = self.space.bag_vector(tokens)
        scored = [(cosine(here, l.vector) * l.confidence, l) for l in self.applicable(tokens)]
        scored.sort(key=lambda s: -s[0])
        return [l for _, l in scored[:k]]

    def concepts(self, k=None, iters=10):
        """Cluster laws by cosine: groups of nearby laws are the agent's concepts."""
        laws = list(self.laws.values())
        if not laws:
            return []
        k = k or max(1, min(6, int((len(laws) / 2) ** 0.5)))
        centres = [l.vector for l in self.rng.sample(laws, k)]
        groups = []
        for _ in range(iters):
            groups = [[] for _ in centres]
            for l in laws:
                groups[max(range(k), key=lambda i: cosine(l.vector, centres[i]))].append(l)
            centres = [(_mean([l.vector for l in g]) if g else None) or centres[i]
                       for i, g in enumerate(groups)]
        return [g for g in groups if g]


def _mean(vectors):
    m = [sum(col) / len(vectors) for col in zip(*vectors)]
    n = math.sqrt(sum(a * a for a in m))
    return [a / n for a in m] if n else None
