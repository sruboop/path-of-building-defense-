"""A universe the agent knows nothing about.

The agent only ever sees: a JSON string, a list of button ids, and a scalar
reward after each press. Everything else here is hidden from it.
"""
import json
import random

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]


class Universe:
    def __init__(self, seed, size=7, n_walls=3, goals_to_win=3):
        self.rng = random.Random(seed)
        self.size = size
        self.goals_to_win = goals_to_win
        # Buttons are wired to effects by a hidden, per-universe permutation.
        effects = MOVES[:]
        self.rng.shuffle(effects)
        self.wiring = effects
        self.buttons = list(range(len(effects)))
        cells = [(x, y) for x in range(size) for y in range(size)]
        self.rng.shuffle(cells)
        self.agent = cells.pop()
        self.walls = [cells.pop() for _ in range(n_walls)]
        self.free = cells
        self.goal = self._spawn_goal()
        self.collected = 0
        self.respawn = False
        self.won = False

    def _spawn_goal(self):
        options = [c for c in self.free if c != self.agent]
        return self.rng.choice(options)

    def observe(self):
        return json.dumps({
            "agent": {"x": self.agent[0], "y": self.agent[1]},
            "goal": {"x": self.goal[0], "y": self.goal[1]},
            "walls": [{"x": x, "y": y} for x, y in self.walls],
        })

    def press(self, button):
        """Returns (observation_json, reward, won)."""
        if self.respawn:  # the collected goal reappears one moment later
            self.goal = self._spawn_goal()
            self.respawn = False
        dx, dy = self.wiring[button]
        nx, ny = self.agent[0] + dx, self.agent[1] + dy
        if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in self.walls:
            self.agent = (nx, ny)
        reward = 0
        if self.agent == self.goal:
            reward = 1
            self.collected += 1
            if self.collected >= self.goals_to_win:
                self.won = True
            else:
                self.respawn = True
        return self.observe(), reward, self.won
