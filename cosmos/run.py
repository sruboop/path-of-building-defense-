"""Drop the agent into a sequence of universes and watch what carries over."""
import argparse

from agent import Agent
from universe import Universe

UNIVERSES = [  # (size, walls) — buttons are rewired in every universe
    (6, 2), (7, 3), (8, 4), (9, 5), (10, 6),
]


def journey(seed, carry, verbose=False):
    agent = Agent(seed)
    steps = []
    for i, (size, walls) in enumerate(UNIVERSES):
        if not carry:
            agent = Agent(seed * 100 + i)
        u = Universe(seed * 1000 + i, size=size, n_walls=walls)
        if verbose:
            print(f"\n== universe {i + 1}: {size}x{size}, {walls} walls, "
                  f"{len(agent.book.laws)} laws carried in")
        steps.append(agent.live(u, verbose=verbose))
        if verbose:
            b = agent.book
            print(f"  won in {steps[-1]} presses | strings tried {b.strings_tried} | "
                  f"laws now {len(b.laws)} | born {b.laws_born} | falsified {b.laws_falsified}")
    return agent, steps


def show_mind(agent):
    print("\nStrongest laws:")
    laws = sorted(agent.book.laws.values(), key=lambda l: -l.confidence * l.support)
    for law in laws[:12]:
        print("  ", law)
    print("\nConcepts (laws clustered by cosine location):")
    for g, group in enumerate(agent.book.concepts()):
        sample = sorted(group, key=lambda l: -l.support)[:3]
        print(f"  concept {g + 1} ({len(group)} laws)")
        for law in sample:
            print("     ", " —> ".join(law.chain))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    agent, _ = journey(0, carry=True, verbose=not args.quiet)
    if not args.quiet:
        show_mind(agent)

    print("\nPresses needed per universe (mean over seeds):")
    for carry in (False, True):
        runs = [journey(s, carry)[1] for s in range(args.seeds)]
        means = []
        for col in zip(*runs):
            done = [c for c in col if c]
            means.append(f"{sum(done) / len(done):6.0f}" if done else "   n/a")
        fails = sum(c is None for r in runs for c in r)
        label = "with memory of past universes" if carry else "fresh mind every universe   "
        print(f"  {label}: {' '.join(means)}   (unfinished: {fails})")


if __name__ == "__main__":
    main()
