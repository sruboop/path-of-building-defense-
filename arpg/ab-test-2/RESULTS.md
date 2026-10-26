# A/B/C test 2: inventive skills from random papers and other genres

**Task:** the first kit (`../SKILLS_v1.md`) was judged not inventive enough.
Each of 16 new skills had to fuse three things into one simple POE2-style
skill:
- a real research paper;
- a real skill from another game genre;
- baseball.

The field and genre for each skill were drawn at random by a script
(`INSPIRATION.md`), and all three sides got the same 16 pairs. Every run is
Claude Code in a fresh session.

| Side | Process | Cost | Turns |
|---|---|---|---|
| **A: codegraph** | research (web results saved into the graph by hooks, 50 notes) → associations with the `associate` tool (116 links) → design from the graph only | $2.15 | 203 |
| **C: same three steps, plain files** | research into `RESEARCH.md` → associations into `ASSOCIATIONS.md` (232 links) → design from the files only | $2.32 | 61 |
| **B: plain Claude** | one session: research + design | $1.39 | 54 |

**Judging:** three blind reviewers. The order was rotated so each proposal
appeared once in each position (P1, P2, P3).

| | Review 1 | Review 2 | Review 3 | Total /240 | Placed |
|---|---|---|---|---|---|
| **C: files** | 61 | 64 | 62 | **187** | 1st in all three |
| **B: plain** | 56 | 59 | 58 | **173** | 2nd in all three |
| **A: codegraph** | 53 | 51 | 55 | **159** | 3rd in all three |

## Honest reading

1. **The method works.** Research, then associations, then design from
   them, beat a single session in every review (C over B by 14 points).
   That is the "chunks and associations as context" idea, and it made the
   AI more inventive.
2. **The graph tool made it worse.** A followed the same three steps as C
   and came last every time. Its kits were marked down for overloaded
   skills (simplicity 5/10) and implementability. The likely causes:
   - **Context.** The design session saw the research in search-result
     slices, while C read all 4,600 words and all 232 links at once. When
     the knowledge fits in context, reading it all beats retrieving pieces.
   - **Fewer associations.** One `associate` call per link made the step
     slow (125 turns), so A recorded half as many. `associate` now takes a
     batch.
3. **Where a graph should win is untested here:** knowledge too big to fit
   in context, such as a large codebase or months of accumulated research.
   This test does not show that.
4. **Small sample:** one run per side, with the same model as both judge
   and designer.

The winning kit (C) is now `../SKILLS.md`.
