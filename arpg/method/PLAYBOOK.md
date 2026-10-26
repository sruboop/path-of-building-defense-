# Playbook: inventive ARPG skills by research → associations → design

Instructions for the next agent. Follow them in order. Everything here was
tested in this repo except where it says **untested**.

## Why this method

Measured in `../ab-test-2/RESULTS.md` with three blind judges and rotated
order:

| Method | Score /240 | Rank |
|---|---|---|
| Research → associations → design, three fresh sessions, **plain files** | **187** | 1st in all three reviews |
| One normal session doing everything | 173 | 2nd |
| The same three steps through the codegraph MCP tool | 159 | 3rd |

What makes it work:
1. **Separate sessions for separate jobs.** Research, associations and
   design each start fresh, so each job gets full attention and a clean
   context.
2. **Random, distant inputs.** A script, not the AI, draws a research field
   and a game genre from outside ARPGs for every skill. This forces
   combinations the AI would never pick itself, which is where the
   inventiveness comes from.
3. **An explicit associations step.** Hundreds of `A <-> B: why` links
   between papers, game mechanics, theme ideas and ARPG mechanics are
   written down before designing. Cross-pair links matter most.
4. **The designer reads everything at once.** Plain files beat search when
   the knowledge fits in context (~10–20k words). Don't use a retrieval tool
   for this.

## Steps

### 0. Set up a workspace
```bash
W=arpg/<class-name>            # e.g. arpg/drums
mkdir -p $W
cp arpg/method/BRIEF_TEMPLATE.md $W/BRIEF.md   # then fill in every <...>
```
- The brief must contain the world, the weapon, the **research topics for
  the theme**, and the **role split**.
- To improve an existing kit, copy it in as `$W/CURRENT_SKILLS.md`. The
  design prompt picks it up.

### 1. Draw the random pairs (never let the AI choose them)
```bash
python3 arpg/method/draw.py "melee:4,ranged:4,caster:4,movement:1,defence:1,utility:1,ultimate:1" > $W/INSPIRATION.md
```
- Use the same role split as the brief.
- Do not redraw because a pair looks hard. Hard pairs produce the freshest
  skills (oobleck × souls-like became the best-liked Foul Tip).
- To compare methods fairly, give every side the **same** INSPIRATION.md
  (`--seed`).

### 2. Run the pipeline
```bash
bash arpg/method/run.sh $W            # research, associations, design, revise
```
Or run the prompts in `prompts/` by hand. Each step **must** be a fresh
session (`claude -p ...`). Don't continue one session through all the
steps.

| Step | Prompt | Tools | Output | Tested cost |
|---|---|---|---|---|
| Research | `1_research.md` | Read, Write, Edit, WebSearch, WebFetch | `RESEARCH.md` (~6k words) | ~$0.95 |
| Associations | `2_associations.md` | Read, Write, Edit (no web) | `ASSOCIATIONS.md` (150–430 links) | ~$0.65 |
| Design | `3_design.md` | Read, Write, Edit (no web) | `SKILLS.md` | ~$1.10 |
| Revise (**untested**) | `4_revise.md` | Read, Write, Edit | rewrites `SKILLS.md`, keeps `SKILLS_draft.md` | ~$0.50 est. |

The revise step was added because every judge marked kits down for the same
things: overloaded skills, reskins and repeated theme ideas. It has not been
measured yet. Keep the draft and compare (step 4) before trusting it.

### 3. Check the output yourself before handing it over
- [ ] Every skill uses its own pair, in its fixed role.
- [ ] "What it does" is at most 3 sentences, with one idea.
- [ ] No theme idea is used twice. (The guitar kit used tremolo picking
      twice and patch cables twice. Fix that kind of thing.)
- [ ] Generators, spenders, pack clear, single target, movement, defence and
      an ultimate are all covered.
- [ ] Citations marked (!) are unverified. Say so to the user and never
      present them as fact.

### 4. When it matters, judge blind
- Put each candidate in a fresh folder as `P1.md`, `P2.md`, ... alongside
  `BRIEF.md` and `INSPIRATION.md`.
- Run `prompts/5_judge.md` in **one fresh session per ordering**. With 3
  candidates, use orders ABC, CAB and BCA, so each candidate sits in each
  position once.
- Map the scores back yourself, and report totals and margins honestly,
  including when your favourite loses.

## Rules learned the hard way
- **Never let the AI choose the inspiration.** It picks safe, familiar
  combinations.
- **No web in the design step.** It should design from the files, not
  wander off researching again.
- **Fresh sessions in non-interactive mode** need tools passed with
  `--allowedTools`, or they stall on permission prompts.
- **WebFetch may be blocked** by the environment's network policy. WebSearch
  snippets were enough in every run.
- **One run is one sample.** Margins of a few points out of 80 can flip on a
  rerun. Run several before claiming a method is better.
- **The same model is both designer and judge.** Treat blind scores as a
  signal, not proof. Your own read and the user's playtest decide.
- **codegraph** (`/codegraph`) is for large codebases, where the AI can't read
  everything at once. For a design task whose research fits in context, it
  made results worse.

## Files
| File | Purpose |
|---|---|
| `PLAYBOOK.md` | this guide |
| `BRIEF_TEMPLATE.md` | the brief to fill in for a new class |
| `draw.py` | random field × genre pairs per role slot |
| `prompts/1_research.md` … `prompts/5_judge.md` | the exact prompts |
| `run.sh` | runs steps 1–4 in a workspace |
| `../guitar/` | a full worked example (brief, pairs, research, associations, skills) |
| `../ab-test-2/` | the evidence for the method |
