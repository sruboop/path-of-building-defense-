# Review of P1, P2 and P3

Read BRIEF, INSPIRATION, CURRENT_SKILLS and all three proposals in full. Scores are 1-10.

## Score table

| Criterion | P1 | P2 | P3 |
|---|---|---|---|
| 1. Inventiveness | 8 | 7 | 8 |
| 2. ARPG play loop | 8 | 7 | 7 |
| 3. Simplicity | 7 | 5 | 7 |
| 4. Fusion quality | 9 | 7 | 8 |
| 5. Scaling and build depth | 8 | 7 | 7 |
| 6. Synergy | 9 | 6 | 7 |
| 7. Baseball and toy-world fit | 8 | 7 | 8 |
| 8. Implementability | 7 | 5 | 7 |
| **Total /80** | **64** | **51** | **59** |

## P1

**Strengths**
- It is the only kit with a shared language. **Set** (solid, shatters on a Barrel, un-set by water) is a new keyword. Foul Tip, Pine Tar and Walk-Up Song all read it, and sprinklers become a toy-world counterplay.
- Strikes now decay, so the Count becomes a rhythm.
- Most skills read as one sentence.
- The "Condensed" lines show the paper's mechanism driving the rule. Three examples:
  - Time Out hits the 7 nearest enemies at any range, and its three contexts come from the Roman Cancel colours.
  - Three-Pitch Mix works only if you release slow to fast, so the sequencing is the skill.
  - Tag Up thickens the path where you cross it twice, so circling an enemy twice before rewinding grows the damage.
- Good ARPG coverage. It has a gap-closer, a retreat, a boss shield-break loop (Full Count) and a defence set.
- The synergy web is dense. Everything feeds Set or the Barrel.

**Weaknesses**
- Ping Pad is Stardew sprinkler tiling with a reskin. Its "in tune" +30% is a flat buff.
- Hang Time's lensing is only "land four times", and it carries a second system (the rocket).
- Several skills hold two or three clauses:
  - Full Count: channel, then a shield burn, then a 2nd-hit snap, then a 5th-hit finisher.
  - Walk-Up Song needs a second timing layer, the beat.
  - Chase the Fly stacks a lock cone, momentum carry and a smash.
- Pine Tar and Foul Tip both feel like "Set generators" and overlap.
- Hidden Ball Trick's regrowth and Enforcer exception add rules.
- Some citations are flagged as unverified, but it says so honestly.

## P2

**Strengths**
- Interesting paper picks: Cook's Rule 110 gliders, Edwards' Lévy re-analysis (long hops are rare and capped), and Wang's tensegrity stiffness-from-prestress.
- Rain Delay as "cycling" (refund cooldowns in proportion to time spent under the tarp) is genuinely fresh.
- The Wave (7 nearest, ignores spacing) is a clean pack-clear idea that is independent of area.
- Hot Corner's nudge, tilt and multiball is a bold pinball translation.
- Rosin Bag is a moving stealth cloud.

**Weaknesses**
- It is the least simple kit. Many skills carry three or more mechanics:
  - Cutoff Man: a lens, a four-way split, a grapple and a two-lens swing.
  - Benches Clear: three unit types, a weapon triangle, a Break state, and a kill-window dispatch.
  - Hard Slide: jam, a lock-on circle and decaying i-frames.
  - Called Strike: a wide-to-narrow cone, Gooey marks and ricochets that scale with fall height.
- Movement is crowded. Hard Slide, Pinch Runner and Base Path are three dashes, and Cutoff Man adds a grapple.
- The basic attack is an unlisted "Plain Swing", and 4 of the 16 skills are labelled generators with no clear main-hand loop.
- Some sloppiness: "Backstop mud" refers to nothing in the kit, and the Hot Corner fountain depends on a pull the text never fully defines.
- Several skills are the game skill re-skinned:
  - Pinch Runner is Dishonored Blink plus a 50% damage cut.
  - Backstop is Stardew tiles plus "projectiles drop dead", which is the old Bunt.
  - Stomp-Stomp-Clap is a Hi-Fi Rush buff aura.
- Spitball repeats the Slay the Spire orb queue, which P1 used better.
- The tardigrade (Dsup) link to Pinch Runner is thin.
- Hardest to implement: the Gooey, Jammed, Hidden and Tilt states plus the grapple physics.

## P3

**Strengths**
- Highest peaks, and the most honest source checking.
- Rain Delay: become a sealed tun, soak damage, then blink out and splash back for all of it. It is a damage bank that reads at a glance and is new to ARPGs.
- Hidden Ball Trick: a Life glider of boxes walks itself and the pack follows in a conga line. This is the most original use of a paper in any kit.
- On Deck: Suspend as a meta-skill. Queue any skill, pay no cost, and it grows +20% per second. It is deep and unusual.
- Instant Replay: a Barrel replayed from four sides with delayed ghosts, plus an Observer-style chain on kill.
- Mine!: interrupt on the final 0.3 s of a wind-up and turn the projectile around (Portal momentum).
- Dead Hands: parry strength scales with hit strength, so you want the boss's biggest blow.
- Pine Tar: a thickening, learning trap.
- Baseball fit is excellent: replay review, on-deck, a hidden ball trick, a Cracker Jack ant trail.

**Weaknesses**
- The core systems are thinner. "Touches" is written by only two skills, so the Count is effectively gone.
- Several games are loosely used:
  - Celeste's dash refill is bolted onto Pine Tar and Steal Home.
  - Resident Evil herbs became orange slices and a sports drink on Tag Out, which is odd and off-theme.
  - Metal: Hellsinger Fury on Paper Fielders is a generic multiplier.
- Pepper Flock is "seven homing balls" and is the least fresh skill.
- Spitball (merge slug plus Slick doubling) and Superball (never-slowing bouncing ball) are the safest skills.
- Steal Home's random hop length is a risk for a core movement skill. A telegraphed next hop mitigates it, but it still hurts precision.
- Rally Ants' "carries your buffs" is vague.
- Four skills are reactive guards (Dead Hands, Mine!, Rain Delay, Backstop Scarecrow), so the kit leans defensive.
- On Deck at zero cost can break balance: queue Rally Ants or Instant Replay for free.
- Synergies are named, but they connect less tightly than P1's.

## Five most inventive skills (all proposals)

1. **P3 Rain Delay** (tarp blink): sit invulnerable as a sealed tun and soak damage, then blink out and splash it all back.
2. **P3 Hidden Ball Trick**: a Game-of-Life glider of decoy boxes that walks itself and leads the pack in a conga line.
3. **P1 Tag Up**: a Braid-style rewind along your own slime-mould path, where doubled-back routes thicken into harder-hitting tubes.
4. **P1 Time Out**: a Roman Cancel that sends a slow wave to the 7 nearest enemies at any range, and adapts to a hit, a whiff or an incoming blow.
5. **P3 On Deck**: Suspend turned into a meta-skill. Any skill waits for free and grows stronger the longer it waits.

## Three worst skills

1. **P2 Pinch Runner**: a Blink plus a flat damage-reduction buff. It is a generic dodge with a tardigrade name and no new rule.
2. **P1 Ping Pad**: Stardew sprinkler tiling with a flat +30% buff. The other skills in that kit are far more original.
3. **P3 Pepper Flock**: seven homing balls cancelled out of a hit. It is the "nearest enemy" homing every ARPG already has.

(Near misses: P2 Benches Clear, overcomplicated and not really about ants; P3 Spitball, a safe projectile.)

## Verdict

1. **P1** is the best. It has the tightest system design and the best fusion logic, with Set and decaying Strikes tying the kit together. The skills read quickly.
2. **P3** is second. It has equal or higher peaks (Rain Delay, Hidden Ball Trick, Instant Replay, On Deck), but it is less consistent and its core framework is thinner.
3. **P2** is last. It has strong single ideas (Rain Delay cycling, The Wave, Rosin Bag) but it is the hardest to read and implement, its movement set is redundant, and several skills are plain re-skins.

**Margins:** P1 beats P3 *slightly*. P3 beats P2 *clearly*, and P1 beats P2 *clearly* too.
