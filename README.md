# stringspace — repository context from tokens, hops, strings and laws

A request comes in. Its words are found as tokens in the repository, the
system hops outward from them along associations, and the strings it forms
decide which pieces of the repository are handed back as context.

```
python3 -m stringspace build [ROOT]               # place tokens, associate, seed strings, mine laws
python3 -m stringspace ask "request" [ROOT] -k 6  # hop from the request, print context snippets
python3 -m stringspace ask "request" --strings    # ...and show the strings that were used
python3 -m stringspace stats [ROOT]               # densest black holes and strongest laws
python3 -m stringspace.bench                      # measure it against plain keyword search
```

Pure Python 3, no dependencies. State lives in `ROOT/.stringspace/state.json`
and grows with every request.

## The pieces

| Idea | Code |
|---|---|
| **Tokens = black holes** | `blackholes.py`: every word in the repo, split on `snake_case` and `camelCase`, gets a random location that never moves (a unit vector seeded by the token) |
| **Associations between pairs** | two tokens are associated when they sit on the same or adjacent lines; strength is normalised so that tokens appearing everywhere don't swallow everything |
| **Hops** | `strings.hop`: a walk from a token along its associations, picking stronger ones more often |
| **Bridges** | `strings.bridge`: every *pair* of request tokens is connected by the strongest chains of at most 3 hops |
| **Strings** | each hop chain is a string. Its location is the sum of the locations it passes through, each bound to its position in the chain (the oscillation). A string formed again is reinforced, and strings sharing a black hole touch |
| **Laws** | `laws.py`: a run of hops that turns up inside many different strings becomes a law. Laws act as shortcuts for later walks (a walk can take a whole law in one jump) and add weight to the strings that contain them |
| **Context** | `context.py`: strings touching the request are scored by closeness to the request's location, how many request tokens they connect, reinforcement and laws. The top strings spread weight over the tokens they pass through, and the 10-line windows of the repo that carry the most weight come back as context |

## How well it works (honest numbers)

`python3 -m stringspace.bench` asks 12 questions about Python's `email`
package and 12 about `asyncio`. `asyncio` was held out and never used for
tuning. It counts how often the right file is in the top 3 snippets.

```
                           email   asyncio
keyword search (no hops)   10/12   10/12
strings                    10/12   10/12   (same on every seed)
```

So far, strings **match keyword search but do not beat it**. What the
experiments showed:

- If the exact lines individual strings hopped through are used directly,
  the context gets worse (down to 6–7 of 12). Random walks are noisy
  evidence one at a time.
- Hop tokens help only when they are weighted lightly next to the request's
  own words (0.1×). At 0.2× and above, results drop.
- Early on, letting strings and laws pile up across requests made results
  *worse*: popular paths got reinforced and crowded out each request's own
  strings. Reinforcement is now capped.

The questions where hops should earn their place are the ones whose words
never appear in the answer: asking about "generated" when the code says
`_make_boundary`. This benchmark has few of those. A benchmark built from
such questions is the next thing to try.
