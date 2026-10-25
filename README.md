# cosmos — an agent that learns universes from strings and laws

An agent is dropped into a dark universe. All it gets is a JSON
observation, a set of unlabeled buttons, and a reward number after each
press. There is no LLM and no domain knowledge. It wins a universe by
collecting the reward 3 times, then moves on to the next one, keeping
only what it has learned.

```
python3 cosmos/run.py            # narrated journey + comparison over 5 seeds
python3 cosmos/run.py --quiet    # comparison only
```

Pure Python 3, no dependencies.

## How the idea maps to the code

| Idea | Code |
|---|---|
| **Universe**: unknown world, unknown buttons | `universe.py`: a grid with walls and a goal; buttons are rewired at random in every universe, and one button does nothing |
| **Chunks**: split the JSON into the smallest pieces | `chunks.py`: every leaf becomes `path=value`. The only math allowed is generic arithmetic: differences between same-named numbers (`x(agent-goal)=-2`) and change over time (`Δagent.x=+1`) |
| **Location in the space** (cosine) | `space.py`: each chunk is a unit vector, random at first. Chunks that keep showing up together in laws are pulled closer, so cosine similarity starts to mean something |
| **Strings**: randomly connect chunks | `LawBook.random_string`: a random chain `chunk → chunk → … → consequence`. Some are complete shots in the dark across the whole vocabulary |
| **Laws**: the strings that actually hold | A string is promoted only with enough support (times it applied) and confidence (times it was right). Occam's razor drops complex laws that a simpler one already explains. Every law is re-tested all the time, and the ones experience contradicts are falsified |
| **Associative cosine of a law** | `Space.string_vector`: a sum of the chain's chunk vectors, each bound to its position in the chain |
| **Laws near each other → thought** | `LawBook.thought`: the applicable laws closest to the present moment's location. `LawBook.concepts`: laws clustered by cosine |
| **Learn from the last universe** | `LawBook.carry_over`: old evidence turns into a capped prior. Laws that still hold survive; laws about the old button wiring are quickly falsified |

The agent acts by chaining laws. A reward law (`x(agent-goal)=0 —>
y(agent-goal)=0 —> reward=1`) says what to aim for. Button laws
(`act=b2 —> Δx(agent-goal)=+1`) say which press moves it closer. Before it
has any laws, it presses whatever it knows least about.

## Results (`run.py`, mean presses to win over 5 seeds)

```
universe:                        1     2     3     4     5   (grid gets bigger, more walls)
fresh mind every universe   :  131   398   334   525   860
with memory of past universes:  174    84   103    85   125
```

The reward law is discovered once, in universe 1, and carries over. In
each new universe only the button wiring has to be relearned, which takes
a few dozen presses.
