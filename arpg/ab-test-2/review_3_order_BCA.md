# Review of P1, P2, P3 (The Slugger, take 2)

## Scores (1-10)

| Criterion | P1 | P2 | P3 |
|---|---|---|---|
| 1. Inventiveness | 9 | 8 | 7 |
| 2. Fun ARPG loop | 7 | 8 | 7 |
| 3. Simplicity | 6 | 6 | 7 |
| 4. Fusion quality | 9 | 8 | 7 |
| 5. Scaling and build depth | 7 | 8 | 7 |
| 6. Synergy | 7 | 9 | 6 |
| 7. Baseball and toy-world fit | 8 | 8 | 7 |
| 8. Implementability | 5 | 7 | 7 |
| **Total /80** | **58** | **62** | **55** |

## P1

**Strengths**
- It has the freshest ideas. The paper's mechanism changes what the skill does, not just its name.
  - *Mine!* works because the bat paper says jamming only works at the exact moment of the feeding buzz. That becomes a "final 0.3 s" reflect, with Portal's speed-in, speed-out for the payoff. It is a counter I haven't seen in an ARPG.
  - *Rain Delay* is a tardigrade tun and a Dishonored blink in one move: soak damage, then blink and splash it back.
  - *Pine Tar* is a slime-mould network that thickens where enemies walk and vanishes where they don't.
  - *Dead Hands* turns the oobleck rule into "the harder the hit, the better the parry reward". That is a real change to how a Souls parry is played.
  - *Hidden Ball Trick* is a glider of decoy boxes that walks itself.
  - *Instant Replay* uses the Einstein cross as four delayed copies of your last Barrel hit, and a kill chains a new replay.
- The sourcing is honest. It marks what was verified and what came from memory.

**Weaknesses**
- Several skills are weak or muddled.
  - *Steal Home*: a random-length dash is a bad movement skill. The HUD preview softens that but doesn't fix it.
  - *On Deck*: a "cast it later, stronger" wrapper that doesn't take much from the hummingbird or Suspend.
  - *Spitball*: "damage rises with distance" is thin.
  - *Backstop Scarecrow* and *Pepper Flock* are fine but ordinary.
- *Rally Ants* has vague buff-carrying rules.
- Implementation cost is highest here.
  - Learning tar networks.
  - A glider decoy on a grid.
  - Ant pheromone.
  - Bistable wall panels with a beat.
  - Cross-skill buff carrying.
- The new Touches system sits beside Runners and Barrel and is used in only a few places. The kit is four ideas deep in places but doesn't share one language.

## P2

**Strengths**
- It is the only proposal with a connecting rule. **Set** (an enemy turned solid that shatters on a Barrel or big hit, dissolved by water) links Foul Tip, Pine Tar, Walk-Up Song, Fungo and Backstop.
  - Water hazards both help and hurt, so the toy world matters.
- The kit has a clear skeleton: two real basic attacks (Walk-Up Song, Fungo), a gap-closer, a retreat, a traversal, and a channelled boss tool (Full Count).
- It also has the strongest fusions.
  - *Chase the Fly*: a constant-bearing curved intercept (bat gaze plus an outfielder's route) that exits at the speed you entered. That is Portal's rule used properly.
  - *Full Count*: Alan Wake's light-burn, then the flytrap's 2 → 5 count, matched to baseball's five-pitch count.
  - *Tag Up*: Braid rewind over a slime-mould path, so circling twice thickens damage.
  - *Fungo*: a Lévy hop with a Fortnite-style shrinking circle that drags enemies in.
  - *Three-Pitch Mix*: a Defect orb queue that releases slow to fast and merges.
  - *Backstop*: taut or slack, with damage shared across the net and released as a blast.
  - *Hidden Ball Trick*: a local-rule distraction wave that stops at Enforcers.
- Scaling is explicit. Examples: crit lengthens Fungo's long hops, projectile count adds Hang Time echoes, and attack speed is literally Benches Clear's charge rate.

**Weaknesses**
- *Time Out* is the most complex skill in the set. It reads three contexts and hits the nearest seven. Players will find it opaque.
- *Foul Tip* has a Sekiro window, a Strike, a Runner, a Set ring and an anti-mash rule. That is too many parts.
- *Knuckleball* (nudge, tilt, whirls and multiball) and *Hang Time* (glide, rocket, four echoes) carry too much.
- *Ping Pad* is a tiling totem and the least inventive entry.
- The paper links are looser for *Benches Clear* and *Ping Pad*.
- Two movement skills (Chase the Fly, Tag Up) overlap a little.
- Some citations are admitted as unverified, which is honest but weaker.

## P3

**Strengths**
- Its skills are the cleanest to read, and the sources are real and well chosen. Citing the Edwards re-analysis of Lévy flights for Pitch Clock is a nice touch.
  - *The Wave* (topological nearest-7 chain over SF6 armour) is the simplest, best-fitted skill in the whole review.
  - *Hot Corner* (superfluid fountain into pinball nudge, tilt and multiball) is strong.
  - *Called Strike* (a sonar cone that narrows from wide to a lock, with a Portal gel ricochet) is good.
  - *Foul Lines* (a tension dial plus policies) and *Stomp-Stomp-Clap* (flipping bistable cells) are good.
- Implementability is decent.

**Weaknesses**
- Several fusions are shallow.
  - *Pinch Runner*: a blink plus 50% damage reduction. The Dsup paper is just flavour.
  - *Backstop*: a passive projectile absorber with ammo. It is Ping Pad again, and the Helmholtz and sprinkler layout puzzle is barely interactive.
  - *Spitball*: a clone of P2's Three-Pitch Mix.
  - *Benches Clear*: a Fire Emblem triangle bolted onto a kill-rate rule.
- The default **Plain Swing** is left "unlisted". For a class whose weapon is the bat, that is a hole.
- Synergies are mostly "X pairs with Y" without a shared rule.
- *Cutoff Man* (a lens that splits projectiles and doubles as a grapple) tries two jobs.
- *Rosin Bag* plus the Hidden status is an invisible-cloud mechanic that is hard to read.

## Five most inventive skills (all proposals)

1. **P1 Mine!** – an interrupt window on enemy wind-ups, taken from the bat-jamming paper, that turns shots around at full speed.
2. **P1 Rain Delay** – a sealed tun that soaks damage and then blinks away and splashes it back.
3. **P1 Pine Tar** – a trap network that learns where the pack walks, thickening used paths and dropping unused ones.
4. **P2 Chase the Fly** – a lock-on dash that curves along a constant bearing and hits for the speed you carried in.
5. **P2 Tag Up** – a rewind along your own thickening path, so circling an enemy twice builds damage.

Honourable mentions: P3 Hot Corner, P1 Hidden Ball Trick (the glider), P2 Full Count.

## Three worst skills

1. **P3 Pinch Runner** – a blink with damage reduction. The tardigrade protein is only a label.
2. **P3 Backstop** – a passive sprinkler-pattern projectile eater. It adds nothing beyond the other proposals' versions.
3. **P1 On Deck** – "cast later for more". Suspend is copied as a gimmick and the hummingbird adds no mechanic.

## Verdict

1. **P2 – slightly ahead of P1.** It is the most complete kit, with a shared Set language and real basic skills. It has the best systemic synergy and good fusions throughout. It loses points for a few overloaded skills.
2. **P1** – the most inventive and the best fusions at the top, but uneven (Steal Home, On Deck, Spitball), the hardest to build, and it lacks a shared rule.
3. **P3 – clearly behind both.** It is clean and readable with a few excellent skills (Wave, Hot Corner, Called Strike). It has the fewest fresh ideas, weaker fusions on the defence and mobility slots, and no named main attack.
