"""Draw random inspiration pairs so the AI can't pick comfortable ones.

    python3 draw.py ROLE_SPEC [--seed N] > INSPIRATION.md
    ROLE_SPEC example: "melee:4,ranged:4,caster:4,movement:1,defence:1,utility:1,ultimate:1"
"""
import random
import sys

FIELDS = [
    "slime mould network growth", "starling murmurations", "tardigrade survival",
    "origami engineering / deployable structures", "ant colony foraging",
    "mantis shrimp strike and cavitation", "bioluminescence", "granular jamming", "sonoluminescence",
    "acoustic metamaterials", "octopus camouflage", "swarm robotics", "gravitational lensing",
    "chaos and the double pendulum", "mycorrhizal fungal networks", "non-Newtonian fluids (oobleck)",
    "coral spawning synchrony", "echolocation in bats", "hummingbird torpor", "Levy flight foraging",
    "cellular automata", "self-healing materials", "superfluid helium", "plant electrical signalling",
    "honeybee waggle dance", "firefly flash synchronisation", "archer fish spitting",
    "magnetotactic bacteria", "pistol shrimp snapping", "tensegrity structures",
    "cymatics (sound shaping matter)", "acoustic levitation", "whale song propagation",
    "stochastic resonance", "frog chorus timing", "elephant infrasound",
    "cricket chirp and temperature", "standing waves and resonance in bridges", "Chladni plates",
    "phase-locked oscillators", "spider silk mechanics", "gecko adhesion", "lightning leader formation",
    "crystal growth and dendrites", "tidal locking", "auxetic materials", "bombardier beetle spray",
    "electric eel discharge", "sand dune migration", "quantum tunnelling",
]
GENRES = [
    "fighting game", "rhythm game", "racing game", "puzzle platformer", "roguelike deckbuilder",
    "real-time strategy", "MOBA", "stealth game", "golf game", "tower defense", "survival horror",
    "metroidvania", "bullet hell shoot-em-up", "trading card game", "city builder", "party game",
    "souls-like", "tactics RPG", "sandbox crafting game", "immersive sim", "physics puzzle game",
    "farming sim", "battle royale", "skateboarding game", "pinball", "grand strategy", "hero shooter",
    "monster-catching RPG", "survival crafting", "extraction shooter", "character action game",
    "match-3 puzzle game", "auto-battler", "walking simulator", "kart racer", "sports manager",
]


def main(argv):
    if not argv:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    seed = None
    if "--seed" in argv:
        seed = int(argv[argv.index("--seed") + 1])
    roles = []
    for part in argv[0].split(","):
        name, _, n = part.partition(":")
        roles += [name.strip()] * int(n or 1)
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    fields, genres = rng.sample(FIELDS, len(roles)), rng.sample(GENRES, len(roles))
    print("# Inspiration pairs (drawn at random by a script, not chosen by the AI)\n")
    print("Skill N must fuse pair N: a real research paper from the field, a real skill or "
          "mechanic from a game of the genre, and the class's theme. The role for each slot is fixed.\n")
    for i, (role, f, g) in enumerate(zip(roles, fields, genres), 1):
        print(f"{i}. role: {role} | field: {f} | genre: {g}")


if __name__ == "__main__":
    main(sys.argv[1:])
