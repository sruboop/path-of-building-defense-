# The Slugger v2: 16 bat skills, each fused from a paper, a game and a baseball idea

Why v1 felt tame: each skill was a baseball term with a damage number. Here each skill is built on a **rule** taken from a real finding (a threshold, a feedback loop, a shape). That rule is the thing the player learns and plays with. The game skill supplies the input or feel, and baseball supplies the fiction and the name. All numbers are playtest starting points.

## Core systems (kept, with two changes)

| System | Rule |
|---|---|
| **Runners** (0–3) | Kept. Generators put runners on base; spenders drive them in. Bases Loaded = 3. |
| **Barrel** | Kept. A late sweet-spot window on every swing, throw or release. Barrel = guaranteed crit, longest hit-stop, +1 Runner from generators. Attack speed doesn't shrink the window. |
| **The Count** | Kept. 3 Strikes = **Strikeout** (stun, +25% damage taken, 4 s). |
| **The Beat** (new) | The ballpark has a steady 90 BPM stomp, shown as a faint ring at your feet. Landing a swing on the beat counts as a Barrel window opening. This is what skill 15 builds on, and any skill can opt in. |
| **Mitt** (new tag) | Skills that absorb or stop things. |

Tags: Attack, Melee, Projectile, AoE, Chain, Movement, Guard, Placed, Aura, Duration, Cooldown, Ultimate, plus damage types (Physical, Fire, Lightning, Cold). Every skill carries a damage type, and supports can convert it.

The default **Plain Swing** (unlisted basic, no cost, tags Attack/Melee/Physical) is the platform for the Barrel and Beat. Skills 2, 8, 11 and 15 are the generators that go beyond it.

**Role map**

| Role | Skills |
|---|---|
| Generators | 2 Foul Tip, 8 Spitball, 11 Base Path, 15 Stomp-Stomp-Clap |
| Spenders | 3 Called Strike, 6 The Wave, 12 Cutoff Man, 13 Hot Corner |
| Pack clear | 6, 10, 13, 16 |
| Single target | 3, 8, 2 (Digest) |
| Movement | 1 Hard Slide, 4 Pinch Runner, 11 Base Path, 12 (grapple) |
| Defence | 1, 2, 4, 9 Rain Delay, 14 Backstop, 7 Foul Lines |
| Control / setup | 5 Rosin Bag, 7, 10 |
| Ultimate | 16 Benches Clear |

---

## 1. Hard Slide
- **Tags:** Movement, Attack, Physical, Cooldown (3 charges, 4 s each).
- **What it does:** Dash into a feet-first slide with 0.5 s of i-frames, steered by the stick; hold the lock-on button and it circles the target. Enemies you hit at speed **jam**: they go rigid as a slab for 1.5 s, and a jammed slab hit by a Home Run or pushed by another jammed enemy slides as one block. Each repeat slide in 3 s loses i-frames (16 → 14 → 10 → 6 frames).
- **Sources:**
  - Paper: Waitukaitis & Jaeger, *Impact-activated solidification of dense suspensions via dynamic jamming fronts*, Nature, 2012. Hitting cornstarch-water fast grows a solid front that advances with impact speed; it's transient, and a slow touch just sinks.
  - Game: Elden Ring, Ash of War *Bloodhound's Step*. A long quickstep with ~16 i-frames that steers around the target, and the patch nerf made repeats decay.
  - Baseball: the slide into a base through infield dirt.
  - Condensed: a dodge whose payoff depends on **speed**. Move fast and the dirt hardens into a slab and enemies jam; slow, you get nothing. The decaying repeats are the cost.
- **Animation and feel:** Stick-lunge, a low crouch, then a long *shhhk* dust cone. Struck enemies freeze mid-pose with a hard-candy shell effect and a *tink*, and a dirt ripple spreads outward from the slide. Hit-stop is short (3 frames) so the slide stays fluid. Jammed enemies melt back to normal with a small "plop".
- **Scaling:** move speed (the jam front is proportional to speed), slide distance, charges, i-frame count, jam duration, Physical damage on the sliding hit, cooldown recovery.
- **Synergies:** Jammed slabs are perfect Home Run/Wave bowling pins. Slide into an attack's wind-up for a free Strike (it replaces v1 Steal Base). Hot Corner's pull stops working on jammed enemies, which makes them predictable fountain targets.

## 2. Foul Tip
- **Tags:** Attack, Guard, Lightning, Mitt, Cooldown (0.5 s). Generator.
- **What it does:** A tight parry. The first successful parry in a window puts **a Charge** on you, and a second within 20 s closes the trap: the attacker is stunned, takes a Strike, and you gain a Runner. Charges decay after 20 s. At 5 Charges your next swing is a **Digest**, a Barrel that releases all stored Charge as lightning damage. Each parry uses one Tape on the bat grip (max 6, refill out of combat or on kills).
- **Sources:**
  - Paper: Hedrich group (Würzburg) with Hasebe lab, Nature Plants, 2020; earlier Böhm et al., *The Venus flytrap Dionaea muscipula counts prey-induced action potentials…*, Current Biology, 2016. One touch isn't enough; a second action potential within ~20–30 s closes the trap, and spikes keep counting up to digestion at about 5.
  - Game: Resident Evil 4 Remake, knife parry. A prompt appears, a perfect parry staggers, and each parry spends knife durability.
  - Baseball: the foul tip, a ball that grazes the bat, is caught, and with two strikes is a strikeout.
  - Condensed: parry is a **counting memory**. One is "just a touch", two within the window is the strike, five is the payoff. Tape is the durability cost that makes each parry a choice.
- **Animation and feel:** Bat edge lifted, a tiny *tick* and a blue spark at the contact point, the first one leaving a small glowing node at your wrist. The second parry does a snapping clamp animation (bat jaws shut) with a loud *CHOMP*, 6-frame stop. The glow count shows pips on the grip.
- **Scaling:** parry window, Charge duration (the 20 s), Tape count, Lightning damage, crit on Digest, Runner gain.
- **Synergies:** The way to give a Runner without swinging; feeds the Strikeout for Called Strike and Hot Corner. Pairs with Rain Delay (Charges are held through the delay). The 5-Charge Digest is a boss single-target spike.

## 3. Called Strike
- **Tags:** Attack, Projectile, Chain, Physical. Spends 1 Runner. Cooldown 3 s.
- **What it does:** Hold to aim a sonar cone: it starts wide and tags up to 6 enemies as **Gooey** (blue gel). Held longer, it narrows to a tight ±3° beam and locks one target, then fires a ball that ricochets among all Gooey enemies in the cone before ending on the locked target for double damage. Gooey enemies bounce projectiles, and the ball's bounce height is proportional to how far it fell.
- **Sources:**
  - Paper: Ghose & Moss, *The sonar beam pattern of a flying bat as it tracks tethered insects*, J. Acoust. Soc. Am., 2003. The bat points its beam axis at the chosen target (σ ≈ 3°), and switches between a wide search mode and a tight attack mode.
  - Game: Portal 2, Repulsion Gel. Painted surfaces make things bounce, and bounce height tracks fall height.
  - Baseball: the umpire's called strike, the catcher framing the zone.
  - Condensed: the **gaze** is the aim. Wide = mark many, narrow = commit to one. The Gooey marks are the repulsion gel that gives the ricochet.
- **Animation and feel:** A cone of dotted blue rings spreads in front of you, and the rings tighten with a rising ping. Release throws a stitched ball with a *bwip*; each bounce on a Gooey enemy is a rubbery *boing* with a squash, the last is a big *thwack*. Camera zooms on the lock.
- **Scaling:** Runner cost reduction, cone width, targets marked, bounce count, projectile damage, crit, Pitch supports (Slider/Screwball bend the final hit).
- **Synergies:** Chain-clears a pack when nothing is locked, single-targets bosses when narrow. Rosin Bag hides *you*, so the first Called Strike from hiding is an Ambush. Cutoff Man lenses split the ricochet.

## 4. Pinch Runner
- **Tags:** Movement, Guard, Cooldown (3 charges, 5 s each).
- **What it does:** Blink up to 10 m to a reticle point, instantly, leaving a toy pinch-runner decoy on the spot you left. On arrival you put on the **Helmet**: 50% less damage from all sources for 2 s, with no healing during that time. A second charge used while Helmeted extends the Helmet and the blink range by +3 m.
- **Sources:**
  - Paper: Hashimoto et al., *Extremotolerant tardigrade genome and improved radiotolerance of human cultured cells by tardigrade-unique protein*, Nature Communications, 2016. The Dsup protein cut X-ray DNA damage roughly in half by shielding DNA rather than repairing it afterward.
  - Game: Dishonored, Blink. An aimed near-instant teleport, cheap enough to chain; Greater Blink adds range.
  - Baseball: the pinch runner, a substitution who takes over the base for you.
  - Condensed: a blink whose arrival is armour, **prevention over cure**. You get to the safe place and get the coating, and the coating is explicitly not healing.
- **Animation and feel:** You tap the bat on the ground; a pop and a puff of chalk. A cutout toy runner sprite appears where you were and takes a bow. You arrive with a clunky plastic batting helmet that visibly dents on each hit, and a soft *bonk* each time it absorbs damage.
- **Scaling:** blink range, charges, Helmet reduction and duration, cooldown recovery, "Helmet" can scale with armour/block.
- **Synergies:** Chains with Hard Slide for an escape and re-engage. The decoy is a taunt target for The Wave and Foul Lines. Pairs with Rain Delay (see 9): both are "shut down to survive" modes.

## 5. Rosin Bag
- **Tags:** Placed, AoE, Duration (8 s), Cooldown (10 s). Control.
- **What it does:** Toss a rosin bag. It puffs a strip of dust that **travels**: each tick, a dust cell becomes dust in the front cell and fades behind, so the band glides forward as a moving cloud (a glider). Anything standing in the dust is Hidden from enemies (they lose aggro), and your first attack from Hidden is an Ambush Barrel.
- **Sources:**
  - Paper: Cook, *Universality in Elementary Cellular Automata*, Complex Systems, 2004. A one-neighbour rule (Rule 110) produces stable gliders that travel and collide, and the collisions compute.
  - Game: Thief, Light Gem. A HUD gem shows how visible you are, so you read risk at a glance.
  - Baseball: the rosin bag the pitcher or batter grips, whose dust puffs up.
  - Condensed: a one-line local rule makes a **moving cloud** you learn to ride, and two clouds that collide spawn a third. The Light Gem is your HUD: it fills with white when you're visible and dims to gold when Hidden.
- **Animation and feel:** The bag *thumps* and bursts; the cloud ripples forward in visible squares (a retro grid look), a soft *fff* as it moves. Hidden enemies look confused, scratching their heads. Colliding clouds pop a "+" shape.
- **Scaling:** cloud length and speed, duration, Ambush damage, crit, number of bags (collisions).
- **Synergies:** Ride the cloud into the pack, then Wave or Hot Corner from stealth. Two bags thrown to meet create a bigger burst of dust. Sonar (3) can lock through the cloud.

## 6. The Wave
- **Tags:** Attack, Melee, AoE, Chain, Physical. Spends 1 Runner (more Runners = more armour and more links).
- **What it does:** A slow, heavy swing with super-armour that absorbs one hit. The target is struck and the shock **passes to its 7 nearest neighbours**, however far away they are, then each of those passes to their own 7 nearest (falloff 30% per hop, 2 hops). Sparse enemies get linked just as well as packed ones.
- **Sources:**
  - Paper: Ballerini et al., *Interaction ruling animal collective behavior depends on topological rather than metric distance*, PNAS, 2008. Each starling tracks a fixed ~6–7 neighbours, not everyone within a radius, which keeps the flock cohesive when density changes.
  - Game: Street Fighter 6, Drive Impact. An armoured slow strike that beats attacks, and loses to throws.
  - Baseball: the stadium wave, passing from fan to fan.
  - Condensed: the Drive Impact armour is the commit; the **topological link** makes it a pack clearer that's immune to enemy spacing.
- **Animation and feel:** Big two-handed overhead wind-up with a visible gold armour shimmer. Impact: a deep *whump*, then a ripple that visibly hops from enemy to enemy as paper-fan arms rise and fall; each hop is a rising crowd *ooooh*.
- **Scaling:** link count (7 → 9, 12), hops, area-independent damage (it ignores area), melee damage, armour, Runners.
- **Synergies:** The best clear when enemies are spread out (kiting packs, dodge-heavy enemies). Jammed slabs from Hard Slide are all neighbours too. Strikeout enemies pass the wave on at +25%.

## 7. Foul Lines
- **Tags:** Placed, Duration (6 s), Cooldown (12 s). Control.
- **What it does:** Plant two foul poles up to 14 m apart; a taut rubber line stretches between them. The farther apart, the stiffer the line: stiffness is proportional to prestress. Enemies that cross it are flung back; a Barrelled ball hitting the line makes it ring and slow everything nearby. Tap to toggle one **policy** per cast: *Speed Bumps* (slow), *Heavy Ban* (big enemies can't cross), or *Pay the Toll* (crossers lose life).
- **Sources:**
  - Paper: Wang et al., *Mechanical behavior in living cells consistent with the tensegrity model*, PNAS, 2001 (Ingber's cellular tensegrity). Stiffness is nearly proportional to prestress, and the load spreads across the whole network.
  - Game: Cities: Skylines II, district policies. Draw a zone and attach tradeoff policies.
  - Baseball: the foul poles, and the foul line, which decides what's fair or foul.
  - Condensed: **tension is a dial**. Pull poles apart for a stiff, short wall; keep them close for a floppy long trap. The policy toggle is the district tradeoff.
- **Animation and feel:** Each pole *thunks* into the ground with a yellow flag. The rubber line hums at a pitch tied to its stiffness; plucking it with a ball gives a deep *twaaang* and a wobble that visibly spreads.
- **Scaling:** pole range, line stiffness, duration, flung distance, policies unlocked by gear, cooldown recovery.
- **Synergies:** Fling enemies back into Hot Corner. Walls in a corridor for Called Strike ricochets. A jammed slab flung by the line hits others.

## 8. Spitball
- **Tags:** Attack, Projectile, Cold (water), Channel. Generator.
- **What it does:** Hold to load water drops into your queue (up to 5, one per 0.3 s, oldest first). On release they fire **slow to fast**, so they catch each other mid-flight and merge into one big blob that lands at a sweet-spot range ring. A merged blob of 5 drops hits like 6× a single drop.
- **Sources:**
  - Paper: Vailati, Zinnato & Cerbino, *How archer fish achieve a powerful impact: hydrodynamic instability of a pulsed jet in* Toxotes jaculatrix, PLoS ONE, 2012. The fish modulates jet speed so the tail overtakes the head and forms one big drop, hitting up to ~6× harder than a steady jet.
  - Game: Slay the Spire, Defect orbs. A queue of channelled orbs, passives fire oldest-first, and cashing out evokes.
  - Baseball: the spitball, the doctored pitch.
  - Condensed: the orb queue is the loading; the velocity ramp is the shot. **Load patiently, merge at the right distance**.
- **Animation and feel:** The bat's barrel drips water into a row of floating beads; a cheeky *ptoo* when released. The beads stream out in a line, bunch up with little *blip-blip-blip*, and land as a big splash with a *SPLOOSH* and wet dust ring. Barrel timing on the release adds a perfect merge.
- **Scaling:** queue size, drop damage, merge multiplier, Cold damage (chill), crit, projectile speed.
- **Synergies:** Splash-chilled targets are easy for Called Strike. Ice slows jam well with Hard Slide. The queue is the reference for Stomp (15) loading.

## 9. Rain Delay
- **Tags:** Guard, Duration (up to 5 s), Cooldown (16 s).
- **What it does:** Pull a tarp over yourself and go torpid: take 85% less damage, but you can't act. When you leave (or are broken out), you **cycle**: skills on cooldown refund seconds equal to your time under the tarp (×0.75), and you gain 1 Runner per 2 s waited. Used above 60% life it refunds more (+50%) than when used in an emergency.
- **Sources:**
  - Paper: Shankar et al. (Cornell), *Hummingbird torpor in context: duration, more than temperature, is the key to nighttime energy savings*, J. Avian Biology, 2020. Torpor is a routine, pre-emptive choice; total savings depend on how long the bout lasts, more than how deep.
  - Game: Magic: The Gathering, Cycling. Discard a dead card at instant speed to draw a fresh one.
  - Baseball: the rain delay, with the tarp across the infield.
  - Condensed: a defensive skill you use **early on purpose**, not at death's door, and the longer you commit the more cycled value you pull out.
- **Animation and feel:** A giant tarp unrolls over you with a rubber *flump*; rain patters; a tiny "zzz" bubble. On exit it whips off in a gust and your skill icons flip like cards with a shuffle sound.
- **Scaling:** damage reduction, max duration, refund ratio, Runner gain, cooldown recovery.
- **Synergies:** Foul Tip Charges persist through the tarp. Used in the lull before a boss phase, it is a full-kit refresh. Pairs with Pinch Runner as the other "shut down to survive" mode.

## 10. Pitch Clock
- **Tags:** Placed, AoE, Duration (5 s), Cooldown (14 s).
- **What it does:** Draws an on-deck circle around the target area that **shrinks** over 5 s. Enemies outside the ring take increasing damage ticks and are pulled inward; each second, a foul ball takes a hop to the nearest straggler outside the ring, in mostly short hops with an occasional long jump. When the ring closes, everything inside takes a hit.
- **Sources:**
  - Paper: Edwards et al., *Revisiting Lévy flight search patterns of wandering albatrosses, bumblebees and deer*, Nature, 2007. Heavy-tailed step lengths (many short, rare long) were claimed optimal for sparse targets; the re-analysis showed the long steps were partly a data artefact.
  - Game: Apex Legends, the Ring. A closing zone that damages outside and forces convergence.
  - Baseball: the pitch clock and the on-deck circle.
  - Condensed: the ring forces the crowd together; the hopping ball is a **truncated Lévy walk** that hunts stragglers. Per Edwards, the long hops are rare and capped, so it behaves, not random chaos.
- **Animation and feel:** A chalk circle snaps down with a ticking clock overlay; the ring tightens with a rising tick-tock. Hopping ball: *bonk-bonk-bonk-WHOOSH*. The final close is a big thud.
- **Scaling:** ring radius, closing speed, tick damage, hop count, long-hop probability, area.
- **Synergies:** Pulls packs in for Wave and Hot Corner. Foul Lines contain the ring's edge. Benches Clear's ants forage the stragglers faster.

## 11. Base Path
- **Tags:** Movement, Attack, Physical, Cooldown (1 dash charge, refilled by landing a hit). Generator.
- **What it does:** Dash in any of 8 directions, and you may dash for 0.15 s after being hit or knocked off a ledge (**coyote time**). The dash scuffs a **dirt path** into the floor; each time you or an ally runs along it, it gets wider and faster, and it fades after 4 s unused. Enemies caught in a worn path take damage, and each hit gives a Runner.
- **Sources:**
  - Paper: Tero et al., *Rules for biologically inspired adaptive network design*, Science, 2010. Slime mould thickens tubes that carry more flow and lets unused ones vanish, ending up with a Tokyo-rail-like network.
  - Game: Celeste, the dash and coyote time. 8-directional air dash, refilled on landing, with a forgiving grace window.
  - Baseball: running the base paths.
  - Condensed: your dash route **becomes** the network: reuse the lines that work, let the rest fade. Coyote time makes it forgiving.
- **Animation and feel:** Crisp 8-direction streak with a one-frame freeze; a brown dirt line draws behind you and glows when worn. Each pass makes it wider with a *scuff-scuff*, and unused sections crumble.
- **Scaling:** dash distance and charges, path width growth, path damage, duration, move speed.
- **Synergies:** Dash through packs to lay a Hot Corner or Wave path. Paths are the lanes for Spitball splashes and Called Strike ricochets.

## 12. Cutoff Man
- **Tags:** Placed, Projectile, Movement, Duration (8 s), Cooldown (10 s). Spends 1 Runner.
- **What it does:** Hit a marble lens that rolls and lodges on the floor. Any projectile (yours or an enemy's) passing through it splits into **four balls in a cross** (the Einstein cross). Press again to grapple to the lens and swing; two lenses let you hang between them and launch.
- **Sources:**
  - Paper: Huchra et al., *Einstein Cross* QSO 2237+0305, Astronomical Journal, 1985. A foreground mass bends light so one quasar appears as four images in a cross, and the lens brightens the source.
  - Game: Terraria, grappling hooks. A chain latches on and pulls you; multi-hooks hang you midway between anchors.
  - Baseball: the cutoff man, who redirects the throw from the outfield.
  - Condensed: **one anchor, two jobs**. It redirects ammo into a cross and redirects you across the room.
- **Animation and feel:** The marble rolls with a glassy hum and sets with a *clink*, casting a small rainbow caustic cross on the floor. Split balls fire in a plus shape with a four-note chime. Grapple: a chain-whip *zing*.
- **Scaling:** lens duration, number of lenses, extra projectiles per split, grapple speed (Terraria hook tiers), projectile damage.
- **Synergies:** Splits Called Strike, Spitball blobs and enemy shots. Backstop mud turns enemy shots into ammo that goes through the lens. Two lenses and Pinch Runner give rapid repositioning.

## 13. Hot Corner
- **Tags:** Placed, AoE, Fire, Duration (5 s), Cooldown (9 s). Spends 1 Runner.
- **What it does:** Third base heats up: a hot patch pulls nearby enemies in with no friction, then spouts them up in a fountain and drops them as pinballs. Each bat hit on a fountaining enemy knocks it into others. Each nudge (a bat tap) adds Tilt; at 3 Tilt the patch fizzles. A third fountain in 3 s starts **multiball**: the airborne enemies all spawn extra bounces.
- **Sources:**
  - Paper: Allen & Jones, *Flow of liquid helium II* (the fountain effect), Nature, 1938. Superfluid flows toward heat with no viscosity and spouts as a fountain (two-fluid model).
  - Game: Pinball FX / Zen Pinball. Nudge, tilt and multiball.
  - Baseball: the hot corner (third base, where the hard-hit balls go).
  - Condensed: heat is the attractor; the nudge/tilt meter is the risk you manage by feel.
- **Animation and feel:** A glowing orange base *hisses*; enemies flow into it like liquid and shoot up with a *whoosh*. Bumper dings on each ricochet, and the multiball is a loud pinball bell and flashing lights.
- **Scaling:** pull radius, fountain height, Fire damage, nudge limit, bounce damage, number of fountains.
- **Synergies:** Foul Lines and Pitch Clock pack enemies for it. Jammed enemies make better pinballs. Called Strike ricochets work on airborne Gooey enemies.

## 14. Backstop
- **Tags:** Placed, Guard, Mitt, Duration (12 s), Cooldown (14 s).
- **What it does:** Plant Helmholtz jugs in a pattern: first a basic 4-tile cross, later a 3×3 and 5×5 block. Every projectile entering a covered tile is **absorbed** and drops as a ball at your feet (ammo). Space the jugs 5 tiles apart for maximum coverage.
- **Sources:**
  - Paper: Fang et al., *Ultrasonic metamaterials with negative modulus*, Nature Materials, 2006. An array of subwavelength Helmholtz resonators makes the effective modulus negative, so sound can't propagate in the band.
  - Game: Stardew Valley, sprinklers. 4 tiles, then 3×3, then 5×5; a layout puzzle.
  - Baseball: the backstop screen behind home plate.
  - Condensed: a resonant array is a **dead zone for one kind of wave**, and the sprinkler tiers are the layout puzzle. Tune to projectile (default) or sonic/sound enemies.
- **Animation and feel:** The jugs hum on setup, the covered tiles light up in a grid. An enemy shot flies in, wobbles, goes *pwoomp* and drops dead. No hit-stop, just a satisfying plop.
- **Scaling:** coverage tier, duration, jug count, projectile conversion into ammo, tuning variants.
- **Synergies:** Ammo feeds Cutoff Man and Called Strike. Pairs with Pitch Clock (enemies stand in the zone). Safer boss arenas for ranged bosses.

## 15. Stomp-Stomp-Clap
- **Tags:** Aura, Attack, Duration (10 s), Cooldown (16 s). Generator.
- **What it does:** Pop-up bleachers unfold under you (Miura-ori fold) and the crowd stomps on the Beat. Each on-beat swing **flips one fold cell** (up to 8); every flipped cell stiffens the whole sheet, adding attack speed and damage. Miss the beat and a cell flips back.
- **Sources:**
  - Paper: Silverberg et al., *Using origami design principles to fold reprogrammable mechanical metamaterials*, Science, 2014. Each Miura-ori cell is bistable, and flipping a cell changes the global stiffness.
  - Game: Hi-Fi Rush. Actions sync to the beat, on-beat hits do extra damage, combos end in a Beat Hit.
  - Baseball: the stadium "We Will Rock You" stomp-stomp-clap.
  - Condensed: the beat is the timing UI; the fold is the **global buff** that grows with each good hit. The 8th cell triggers a clap finisher.
- **Animation and feel:** The cardboard bleachers unfold with a paper *fwip-fwip* and a crowd sprite stands. Every on-beat hit gives a *STOMP* with the flipped panel lighting gold; the clap finisher is an AoE shockwave.
- **Scaling:** duration, cells, buff per cell, Beat window, finisher damage, attack speed.
- **Synergies:** Plain Swing and Spitball release on the beat. Stronger with Hard Slide for repositioning on the beat. The queue idea from Spitball feeds the cells.

## 16. Benches Clear
- **Tags:** Summon, AoE, Ultimate, Duration (12 s), Cooldown (40 s). Needs Bases Loaded.
- **What it does:** The whole toy team charges out: **Runners** (fast), **Pitchers** (ranged), **Fielders** (tanks). Teammates dispatch based on how many kills you've made in the last 3 s, so a drop in kills quiets the sorties for a few seconds before they recover. Each type has an advantage over one enemy class (like a weapon triangle), +30% damage and an extra Break.
- **Sources:**
  - Paper: Gordon, Holmes & Nacu, *The short-term regulation of foraging in harvester ants*, Behavioral Ecology, 2008. An ant leaves the nest based on its recent encounters with returning foragers, with no central control. Removing returners cuts foraging within 2–3 min.
  - Game: Fire Emblem, the weapon triangle. Sword beats axe, axe beats lance, lance beats sword; a favoured hit causes Break.
  - Baseball: the benches-clearing brawl.
  - Condensed: **no commander**: the team goes out as long as kills keep returning, and counters matter. Pitchers beat Runners at range, Runners beat Fielders, Fielders beat Pitchers.
- **Animation and feel:** The dugout doors slam open, a bugle and dust cloud, tiny toy players pour out. Each teammate has a distinct silhouette and colour; a triangle icon floats over each matchup.
- **Scaling:** team size, duration, teammate damage, kill-window length, triangle bonus, cooldown recovery.
- **Synergies:** Pitch Clock and Wave pack enemies for the team; Stomp buffs them. Rain Delay to refresh the cooldown.

---

## Three example builds

**Parry Digest (boss duelist)**
- Skills: Foul Tip, Hard Slide, Called Strike, Rain Delay, Pinch Runner, Benches Clear.
- Scaling: Lightning damage, crit, parry window, Tape.
- Loop: parry twice to Strikeout, build to 5 Charges, Digest for burst; Rain Delay between phases.

**Pinball Pack (area)**
- Skills: Pitch Clock, Hot Corner, The Wave, Foul Lines, Base Path, Stomp-Stomp-Clap.
- Scaling: area, Fire, bounces, link count.
- Loop: dash a path, close the ring, fountain the pack, Wave the stragglers on the beat.

**Lens Battery (projectile)**
- Skills: Spitball, Cutoff Man ×2, Backstop, Called Strike, Rosin Bag.
- Scaling: projectile damage, extra projectiles, Cold.
- Loop: hide in the Rosin cloud, load Spitball, split it through two lenses, absorb enemy shots with Backstop for ammo.
