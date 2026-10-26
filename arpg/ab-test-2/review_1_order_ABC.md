# Review of P1, P2, P3 (The Slugger, take 2)

All three honour the 16 inspiration pairs. Each skill uses the right field and genre, and each names a real paper, a real game skill and a baseball idea. The question is how much of each source reaches the mechanic.

## Scores (1-10)

| Criterion | P1 | P2 | P3 |
|---|---|---|---|
| 1. Inventiveness | 7 | 7 | 8 |
| 2. Fun ARPG loop | 7 | 7 | 8 |
| 3. Simplicity | 5 | 8 | 6 |
| 4. Fusion quality | 8 | 7 | 8 |
| 5. Scaling / build depth | 7 | 6 | 8 |
| 6. Synergy | 7 | 7 | 8 |
| 7. Baseball / toy-world fit | 7 | 7 | 8 |
| 8. Implementability | 5 | 7 | 6 |
| **Total /80** | **53** | **56** | **61** |

## P1: strong paper fidelity, but too many ideas per skill

**Strengths**
- It takes the most literal rule from each paper. Examples: impact speed grows the jam front (Hard Slide), the sonar beam narrows from wide to ±3° (Called Strike), stiffness is proportional to prestress (Foul Lines), the Miura cell flip stiffens the whole sheet (Stomp-Stomp-Clap), and each starling tracks its nearest 7 neighbours (The Wave).
- The Runner generator/spender split is clean, and there is a clear role map.
- Several skills are fresh. Rosin Bag is a travelling stealth cloud (a cellular-automaton glider), The Wave clears scattered packs by nearest-7 links, Foul Lines is a tension dial, and Pitch Clock is a closing ring with a Lévy-hopping ball.

**Weaknesses**
- It breaks "one clear idea per skill" repeatedly:
  - Hard Slide has the speed-dependent jam, slabs that slide as a block, and decaying i-frames.
  - Foul Tip has a two-touch trap, Charges, Tape durability and a 5-Charge Digest.
  - Called Strike has a sonar cone, a lock, Gooey marks and a ricochet.
  - Cutoff Man is a lens that splits projectiles into a cross, plus a grapple, plus two-lens swinging.
  - Hot Corner has a pull, a fountain, pinball hits, Tilt and multiball.
- Several skills are genre skills with a coat of paint:
  - Pinch Runner is a Dishonored blink plus armour.
  - Base Path is a Celeste dash.
  - Backstop is a Stardew sprinkler grid.
- It adds an extra system (the Beat) on top of the Barrel.
- Implementability is the worst of the three, because many skills need several interacting subsystems at once.
- Rain Delay refunds cooldowns for time spent under the tarp, which is a possible infinite-loop exploit.

## P2: simplest and cleanest, but the fusions are thinner

**Strengths**
- Its sourcing is honest: every paper is tagged verified or from memory, and a weak-links section lists the gaps.
- Most skills read in one sentence.
- Several ideas are fresh and well shaped:
  - Rain Delay: you become an immobile tun that soaks hits, then blinks away and splashes back the damage you soaked.
  - Instant Replay: your last Barrel is replayed from four sides with delays, and a replay that kills triggers another.
  - Hidden Ball Trick: a decoy shape that walks itself like a glider.
  - Mine!: a reflect that only works in the final 0.3 s of a wind-up, taken straight from the bat-jamming paper.
  - On Deck: Suspend-style queued skills that grow stronger the longer they wait.
- It is the most implementable of the three.

**Weaknesses**
- Some fusions are mostly the game skill with a flavour line:
  - Dead Hands is a Souls parry and riposte. "Harder hit means longer freeze" is the only oobleck content.
  - Tag Out is a basic jab with a flytrap count and herb-merge pickups tacked on.
  - Paper Fielders has a weak baseball link (the infield shift and a fold-out chart).
  - Backstop Scarecrow is a projectile deleter.
- Steal Home is a randomised dash length. That hurts a movement skill, even with the next length shown on the HUD.
- There is no strong stat or support hook for most skills.
- Build depth is lower than in P3 because there is no shared mechanic that skills fight over. The Touches system is nearly unused.

## P3: best fusion of ideas into a system

**Strengths**
- It builds an interlocking keyword. **Set** (a hardened enemy that a Barrel shatters, undone by water) is fed by Foul Tip and Pine Tar, consumed by every Barrel, and made dangerous or useful by the toy world's sprinklers and puddles.
- Several skills are genuinely new for an ARPG:
  - Chase the Fly curves in on a constant bearing, which is the real McBeath outfielder rule plus the bat's 3° gaze lock.
  - Benches Clear is nine ants on a Final Fantasy Tactics-style charge-time bar, driven by an excitable-system feedback loop. It self-snowballs and self-settles.
  - Tag Up is a Braid-style rewind along your own thickening gel path.
  - Time Out is a Roman Cancel that hits the nearest seven enemies, whatever the distance.
  - Fungo is a Lévy hop under a shrinking Storm circle, so the pack is dragged together before the pop.
  - Backstop is a Taut or Slack net with shared tension that collapses into a blast.
- The kit covers a main melee attack (Walk-Up Song), a ranged basic (Fungo), shield-stripping for bosses (Full Count), three movement options, two defences, two zone tools and an ultimate.
- The scaling hooks are specific. Crit lengthens Fungo's long-hop odds, projectile count adds Hang Time echoes, and attack speed is literally the ants' charge speed.
- Its baseball and toy-world anchors are the best of the three: full count, Time!, tag up, fungo bat, pine tar, walk-up song.

**Weaknesses**
- It stacks four rule layers (Runners, Barrel, Count with decay, Set), and the Beat appears in Walk-Up Song.
- Hang Time is overloaded (leap, bottle rocket, four echoes).
- Ping Pad is the weakest skill: a Stardew sprinkler grid that deletes projectiles.
- Several citations are flagged as recalled from memory or unconfirmed, though it says so itself.
- Set is a very strong keyword, so its balance would need the most tuning.

## Five most inventive skills (all proposals)

1. **P3 Chase the Fly**: a 3° gaze-lock dash that curves in on a constant bearing like an outfielder, and hits harder the faster you were running.
2. **P3 Benches Clear**: nine ants with visible charge-time bars that fill from your hits, so the swarm snowballs and then settles.
3. **P2 Rain Delay**: you become an immobile tun that soaks hits, then blink to a marker and splash back all the damage you took.
4. **P2 Instant Replay**: your last Barrel is replayed from four sides with delays, and a replay that kills triggers another.
5. **P3 Tag Up**: rewind along your own gel trail at triple speed, damaging everything you cross. Repeated crossings thicken it into harder-hitting tubes.

Close misses: P1 Rosin Bag (a moving stealth cloud), P3 Time Out, P2 Hidden Ball Trick (a self-walking glider decoy).

## Three worst skills

1. **P1 Pinch Runner**: a Dishonored blink with a damage-reduction buff and a decoy. It is the least changed from a stock ARPG blink, and the tardigrade link adds almost nothing to how it plays.
2. **P2 Tag Out**: a basic jab with a flytrap count and herb-merge pickups bolted on. The pickup merge is a gimmick that doesn't change how the skill is used.
3. **P3 Ping Pad**: a Stardew sprinkler grid that deletes projectiles. It is the same as P1's Backstop and P2's Backstop Scarecrow, and the metamaterial adds only a tile pattern.

## Final verdict

| Rank | Proposal | Total | Margin |
|---|---|---|---|
| 1st | **P3** | 61 | **Clearly** ahead of P2 |
| 2nd | **P2** | 56 | **Slightly** ahead of P1 |
| 3rd | **P1** | 53 | |

P3 wins because its fusions become shared systems with real interplay (Set + Barrel + toy-world water, scaling that ties to specific stats) and its signature skills are both new and baseball-true. P2 and P1 are close. P2 is cleaner and easier to build, but its fusions are thinner. P1 is more faithful to the papers and has the better economy, but it is the most overloaded and the hardest to implement. P2 edges it because the brief says "not too complicated".
