# A/B test: does codegraph make the AI design better?

**Task:** `../BRIEF.md`, 16 baseball-bat skills for an isometric ARPG in an
It Takes Two style world. Both sides got the same brief, the same research
topics and the same output format. Every run is Claude Code from the command
line (`claude -p`), each in a fresh session.

| | A: codegraph | B: plain Claude |
|---|---|---|
| Research | session 1: web search; results saved into the graph by the hooks (12 notes) plus Claude's own `remember` notes (5) | the same session as the design |
| Associations | session 2: Claude linked baseball ideas to ARPG mechanics (84 links, e.g. eephus → slow lob AoE) | none |
| Design | session 3: fresh, no web; context only from the graph (16 searches) | session 1 continued, with its own research in context |
| Cost | $0.42 + $0.39 + $0.49 = **$1.30**, 143 turns | **$0.47**, 15 turns |

**Blind review:** two fresh Claude sessions acting as ARPG designers. Labels
were swapped between them to cancel out position bias.

| Review | A (codegraph) | B (plain) | Verdict |
|---|---|---|---|
| 1 (A shown as X) | 59/80 | 55.5/80 | A slightly better |
| 2 (A shown as Y) | 62/80 | 57/80 | A slightly better |

- **Where A won:** simplicity, synergy and how easy it would be to build.
  One resource, the Runners, ties the kit together.
- **Where B won:** build depth (pitch types as support gems), toy-world
  charm, and more inventive single skills (Rundown, Full Swing's cycle,
  Eephus).
- **What both reviewers said:** the best result would combine A's core
  systems with B's best skills. `../SKILLS.md` is that combination.

## Honest reading

- A won both times, but only **slightly**: 4–5 points out of 80.
- **A also had about 3× the budget and three sessions.** Some or all of the
  gain may come from extra thinking and from starting the design fresh, not
  from the graph itself. This test can't separate the two.
- **The associations did not clearly carry into the design.** Session 2
  linked curveball, knuckleball and eephus to projectile behaviours, yet A's
  design used none of those pitch skills. B, with no graph, did.
- **One run per side.** A different run could flip the result.
- **The hooks worked live** for the first time: every web search was saved
  into the graph automatically.
- **The test found two real bugs, now fixed:** `associate` refused plain
  ideas, and the server could overwrite notes the hooks had just written.

**What would settle it:**
- several runs per side;
- an arm with A's three-session process but no graph, to separate the
  graph from the extra sessions;
- tasks on a large codebase, where the AI can't read everything and
  retrieval matters most.
