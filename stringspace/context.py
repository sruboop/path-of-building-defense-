"""Turning a request into context.

1. The request is tokenized; the tokens that exist in the space are seeds.
2. From every seed the system hops, forming fresh strings (this is the
   "create associations, then hop" step). They are stored, so the space
   gets denser with every request.
3. Candidate strings are the ones touching the seeds or touching the fresh
   strings. Each is scored by how close its location is to the request's
   location, how often it has been formed, and whether it contains laws.
4. The repository lines the winning strings hop through become the context.
"""
import math
import os
import random
from collections import defaultdict

from .blackholes import bag, cosine, tokens_of
from itertools import combinations

from .strings import bridge, canonical, hop

HOP_WEIGHT = 0.1   # how much a hop token counts relative to a request token
SPOT_WEIGHT = 0.0  # bonus for the exact lines a top string hopped through (hurt in tests)


def _contains(string_tokens, law):
    n = len(law)
    for direction in (law, law[::-1]):
        for i in range(len(string_tokens) - n + 1):
            if string_tokens[i:i + n] == direction:
                return True
    return False


def grow(state, seeds, rng, walks, avoid=()):
    fresh = []
    for seed in seeds:
        for _ in range(walks):
            path, evidence = hop(state.space, seed, rng, rng.randint(3, 6),
                                 state.laws, avoid=avoid)
            if path:
                fresh.append(state.strings.add(path, evidence))
    return fresh


def ask(state, request, k=6, walks=24, top_strings=20, seed=None,
        hop_weight=HOP_WEIGHT, spot_weight=SPOT_WEIGHT):
    rng = random.Random(seed)
    space = state.space
    words = tokens_of(request)
    seeds = sorted({t for t in words if t in space.neighbours})
    if not seeds:
        return {"seeds": [], "strings": [], "snippets": []}
    # rarer seeds matter more (inverse line frequency)
    total = sum(space.df.values()) or 1
    weight = {t: math.log(1 + total / space.df[t]) for t in seeds}

    fresh = grow(state, seeds, rng, walks)
    for a, b in combinations(seeds, 2):  # every pair of seeds gets connected
        for path, evidence in bridge(space, a, b):
            fresh.append(state.strings.add(path, evidence))
    state.maybe_mine()

    nearby = defaultdict(float)
    for s in fresh:
        for t in s.tokens:
            if t not in weight:
                nearby[t] += 1.0
    top_near = dict(sorted(nearby.items(), key=lambda kv: -kv[1])[:30])
    scale = max(top_near.values(), default=1.0)
    request_weights = dict(weight)
    for t, v in top_near.items():
        request_weights[t] = 0.3 * v / scale
    here = bag(request_weights, request_weights)

    candidates = {canonical(s.tokens): s
                  for s in state.strings.touching(list(seeds) + list(top_near))}
    scored = []
    for s in candidates.values():
        hit = [t for t in set(s.tokens) if t in weight]
        touched = sum(weight[t] for t in hit)
        # only laws that pass through the request count as support
        laws = [l for l in state.laws.through(hit) if _contains(s.tokens, l)]
        # reinforcement is capped: popular paths must not drown the request
        score = (cosine(s.vector(), here) + 0.5 * touched) * (len(hit) or 0.3) \
            * (1 + 0.3 * min(math.log(s.count), 2)) * (1 + 0.25 * len(laws))
        scored.append((score, s, laws))
    scored.sort(key=lambda x: -x[0])
    best = scored[:top_strings]

    # The field: every top string spreads its score over the black holes it
    # passes. Seeds keep their own weight; hop tokens get what strings give them.
    nwin = len(space.windows) or 1
    idf = lambda t: math.log(1 + nwin / max(1, len(space.postings.get(t, ()))))
    field = {t: idf(t) for t in seeds}
    mass = defaultdict(float)
    for score, s, _ in best:
        for t in s.tokens:
            if t not in field:
                mass[t] += score
    top = max(mass.values(), default=1.0)
    for t, m in mass.items():
        field[t] = hop_weight * idf(t) * m / top

    windows = defaultdict(float)
    for t, w in field.items():
        for wid, count in space.postings.get(t, ()):
            windows[wid] += w * (1 + math.log(count))
    if best:
        for score, s, _ in best:  # where the strings themselves were seen
            for spots in s.evidence:
                for fid, ln in spots:
                    wid = _window_id(space, fid, ln)
                    if wid is not None:
                        windows[wid] += spot_weight * score / (len(spots) * best[0][0])

    return {"seeds": seeds, "strings": best, "field": field,
            "snippets": snippets(space, windows, k)}


def _window_id(space, fid, ln):
    lo, hi = 0, len(space.windows)
    while lo < hi:  # windows are stored in (file, line) order
        mid = (lo + hi) // 2
        if space.windows[mid] < [fid, ln]:
            lo = mid + 1
        else:
            hi = mid
    if lo < len(space.windows) and space.windows[lo] == [fid, ln - (ln - 1) % 10]:
        return lo
    return lo - 1 if lo and space.windows[lo - 1][0] == fid else None


def snippets(space, windows, k):
    out = []
    for wid, score in sorted(windows.items(), key=lambda kv: -kv[1])[:k]:
        fid, start = space.windows[wid]
        path = space.files[fid]
        try:
            with open(os.path.join(space.root, path), encoding="utf-8") as f:
                text = f.read().splitlines()[start - 1:start - 1 + 10]
        except OSError:
            text = []
        out.append({"file": path, "start": start, "end": start + len(text) - 1,
                    "score": round(score, 3), "text": text})
    return out
