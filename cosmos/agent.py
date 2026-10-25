"""The agent: chunk, place, string, test, keep laws, think, act.

Its only built-in drive is the scalar reward. It does not know what any
button does or what any JSON field means.
"""
import random
from collections import Counter

from chunks import deltas, parse, perceive
from laws import REWARD, LawBook, Memory
from space import Space


class Agent:
    def __init__(self, seed=0, learn_every=5, tries=400):
        self.rng = random.Random(seed)
        self.space = Space(seed)
        self.book = LawBook(self.space, self.rng)
        self.learn_every = learn_every
        self.tries = tries

    # -- entering a universe ---------------------------------------------
    def enter(self, buttons):
        self.buttons = [f"act=b{b}" for b in buttons]
        self.book.carry_over()
        self.mem = Memory()
        self.moments = []
        self.attempts = Counter()  # (moment signature, button) -> presses

    # -- deciding ------------------------------------------------------------
    def _targets(self):
        """What the world looks like when reward comes, according to the laws."""
        best, targets = 0.0, {}
        for law in self.book.laws.values():
            if law.kind == "sync" and law.consequence == REWARD:
                weight = law.confidence * law.support
                parsed = dict(parse(t) for t in law.antecedent)
                if weight > best and all(isinstance(v, int) for v in parsed.values()):
                    best, targets = weight, parsed
        return targets

    def _predicted_gain(self, tokens, numeric, button, targets):
        gain = 0.0
        laws = [l for l in self.book.applicable(tokens | {button})
                if l.kind == "temporal" and button in l.antecedent]
        for key, goal in targets.items():
            if key not in numeric:
                continue
            best = None
            for l in laws:
                ckey, d = parse(l.consequence)
                if ckey == f"Δ{key}" and (best is None or l.confidence > best[0]):
                    best = (l.confidence, d)
            if best:
                conf, d = best
                now = numeric[key]
                gain += conf * (abs(now - goal) - abs(now + d - goal))
        return gain, len(laws)

    def choose(self, tokens, numeric):
        sig = frozenset(tokens)
        targets = self._targets()
        scores = {}
        for b in self.buttons:
            gain, known = self._predicted_gain(tokens, numeric, b, targets)
            tried = self.attempts[(sig, b)]
            curiosity = 0.3 / (1 + known)  # prefer buttons we have few laws about
            scores[b] = gain + curiosity - 0.4 * tried + self.rng.random() * 0.1
        return max(scores, key=scores.get)

    # -- living --------------------------------------------------------------
    def live(self, universe, max_steps=3000, verbose=False):
        self.enter(universe.buttons)
        obs = universe.observe()
        tokens, numeric = perceive(obs)
        for step in range(1, max_steps + 1):
            button = self.choose(tokens, numeric)
            self.attempts[(frozenset(tokens), button)] += 1
            obs, reward, won = universe.press(int(button[5:]))
            post, post_num = perceive(obs)
            # reward is perceived *in* the moment it arrives
            post_seen = post | ({REWARD} if reward else set())
            delta = deltas(numeric, post_num)
            self.mem.record(tokens, button, post_seen, delta, reward)
            self.moments.append((tokens, button, post_seen, delta))
            if reward:
                self.attempts.clear()
            if step % self.learn_every == 0 or reward:
                self.book.explore(self.mem, self.moments, self.tries)
            if step % 10 == 0:
                self.book.retest(self.mem)
            if verbose and reward:
                print(f"    step {step:4d}: reward  ({len(self.book.laws)} laws)")
            tokens, numeric = post, post_num
            if won:
                self.book.retest(self.mem)
                return step
        self.book.retest(self.mem)
        return None
