"""The whole space on disk: black holes, associations, strings, laws."""
import json
import os
import random

from .blackholes import Space
from .context import grow
from .laws import Laws
from .strings import Strings

DIR = ".stringspace"


class State:
    def __init__(self, space, strings=None, laws=None):
        self.space = space
        self.strings = strings or Strings()
        self.laws = laws or Laws()
        self._mined_at = len(self.strings)

    def maybe_mine(self, every=500):
        """Laws are re-mined once enough new strings have appeared."""
        if len(self.strings) - self._mined_at >= every:
            self.laws.mine(self.strings)
            self._mined_at = len(self.strings)

    @classmethod
    def build(cls, root, walks_per_token=2, seed=0):
        state = cls(Space().build(root))
        rng = random.Random(seed)
        tokens = sorted(state.space.neighbours)
        grow(state, tokens, rng, walks_per_token)
        state.laws.mine(state.strings)
        state._mined_at = len(state.strings)
        return state

    def save(self, root):
        os.makedirs(os.path.join(root, DIR), exist_ok=True)
        with open(os.path.join(root, DIR, "state.json"), "w") as f:
            json.dump({"space": self.space.to_json(), "strings": self.strings.to_json(),
                       "laws": self.laws.to_json()}, f)

    @classmethod
    def load(cls, root):
        with open(os.path.join(root, DIR, "state.json")) as f:
            d = json.load(f)
        return cls(Space.from_json(d["space"]), Strings.from_json(d["strings"]),
                   Laws().load(d["laws"]))
