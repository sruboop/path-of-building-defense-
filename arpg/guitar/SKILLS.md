# SKILLS.md: the Guitar Class (16 skills)

All numbers are tuning placeholders. They show the intended size and shape of each skill, not final balance.

---------------------------------------------------------------------
# PART 1: CORE SYSTEMS
---------------------------------------------------------------------

The class has three small systems. Every skill uses at least one of them, and most skills use two.

## 1. Gain (the resource)

- Gain runs from 0 to 100 and is shown as the amp's gain knob next to the hero.
- **Generators** (Tremolo Flurry, Flytrap Pick, Cricket Chirp) give Gain and cost nothing. **Spenders** cost Gain. The Ultimate spends all of it.
- Gain decays at 5/s after 4 s without hitting anything.
- Class passive **Crunch**: 1% more damage per 10 Gain held, up to 10%. This makes holding Gain better than dumping it, which tests every spender.
- Scaling stats: Gain on hit, max Gain, Gain decay, Gain cost.
- The three groups earn Gain differently:
  - Melee earns a lot per hit.
  - Ranged earns a little per projectile.
  - Casters earn per second of casting.

## 2. Beat (the timing mechanic)

- A metronome ring pulses on the floor around the hero at 120 BPM (one pulse every 0.5 s). Metronome enemies in the world tick to the same ring, as a joke.
- A skill is **On Beat** if its press or release lands within ±0.10 s of a pulse. Every skill lists one small On Beat bonus. You never *need* it, but you are rewarded for it.
- Some skills also **pulse on their own on the beat** (Overdrive Bubble, Stompbox Sprinkler, Bumblebee Solo). Those scale with **Tempo**.
- Scaling stats: **Tempo** (+BPM: more pulses per second, so faster auto-pulses and more On Beat chances) and **Beat Window** (a wider ±window).

## 3. Resonance (the stack on enemies)

- Resonance stacks to 10 on an enemy and lasts 5 s. Each hit refreshes it. By itself it only gives +1% damage taken per stack.
- **Applied by:** Generators (+1 per hit): Tremolo Flurry, Flytrap Pick, Cricket Chirp.
- **Read or consumed by:** Resonant Slam (consumes and doubles), Overdrive Bubble (stacks swell it faster), Humbucker Crescendo (damage per stack).
- Resonance is the shared payoff stack. The Generators put it on enemies, and the Slam and the Finale cash it in. This is how the three groups feed each other.

## Tags, damage types, and Pedal supports

- **Tags:** Attack, Spell, Melee, Projectile, Slam, Strike, AoE, Duration, Channelling, Totem (placed), Chaining, Movement, Sound (hits made of noise).
- **Native damage:** Physical (hits), Lightning (electric guitar, cables), Fire (heat, overdrive), Cold (stillness, slow). A skill's native type is listed. Pedals convert it.
- **Pedals are the support gems**, socketed into skills and limited by tags:

| Pedal | Effect |
|---|---|
| Overdrive | 40% of damage converts to Fire, 20% more damage, +25% Gain cost |
| Chorus | A detuned second copy at 60% damage, 0.2 s later and offset to the side |
| Delay | Repeats the skill once, one beat later, at 50% damage |
| Reverb | +25% Area and the effect lingers one beat longer |
| Octave Down | +30% damage and +50% knockback, -15% speed |
| Wah | Converts to Lightning and gives +20% movement speed for 2 s after use |

## How the three damage groups differ

| | **Melee: the Riff** | **Ranged: the Rig** | **Caster: the Pedalboard** |
|---|---|---|---|
| Fantasy | The guitar is a club | Picks, bubbles and goop fired from the guitar | Chords and effects pedals played through the amp |
| Gain source | Big, per hit | Small, per projectile | Steady, per second of casting |
| Shape of play | Stay close, ramp, then cash in with a heavy hit | Place and set up, then trigger | Position and sustain, cast on the move |
| Key stats | Attack speed, crit, stack cap | Projectile count, area, duration | Tempo, cast speed, area, duration |
| Defence | Armour, block, Standby | Distance, Cable Snap | Slows and walls |
| Hit feel | Hit-stop and screen shake | Many small readable pops | Big shapes with delays |

## Coverage table

| # | Skill | Group | Economy | Primary job | Also does |
|---|---|---|---|---|---|
| 1 | Resonant Slam | Melee | Spender | Single-target burst | Sideways knockback |
| 2 | Domino Chord | Melee | Spender | Pack clear (cascade) | Ground control |
| 3 | Tee Off | Melee | Spender | Crowd control and scatter-clear | Opener |
| 4 | Tremolo Flurry | Melee | **Generator** | Single-target ramp | Applies Resonance |
| 5 | Overdrive Bubble | Ranged | Spender | Delayed burst AoE | Kiting tool |
| 6 | Flytrap Pick | Ranged | **Generator** | Root and pull | Damage over time on bosses |
| 7 | Stompbox Sprinkler | Ranged | Spender | Sustained zone | Pattern choice |
| 8 | Jelly Patch | Ranged | Spender | Damage amplifier (spreads damage) | Makes single-target hits clear packs |
| 9 | Bumblebee Solo | Caster | Spender | Roaming pack clear | Finds spread-out enemies |
| 10 | Patch Cables | Caster | Spender (per second) | Channelled bossing | Starts as add-clear |
| 11 | Cricket Chirp | Caster | **Generator** | Cast while moving | Applies Resonance |
| 12 | Loop Trail | Caster | Spender | Slow zone | Funnels enemies |
| 13 | Cable Snap | Utility | Charges | **Movement** | Ambush bonus |
| 14 | Standby | Utility | Free | **Defence** | Gain-decay stop |
| 15 | Chladni Plate | Utility | Cooldown | **Utility**: reshape the floor | Walls and roots |
| 16 | Humbucker Crescendo | Utility | Spends all Gain | **Ultimate** | Line-up pull and burst |

**Coverage by need**

| Need | Skills |
|---|---|
| Generators (one per group) | 4, 6, 11 |
| Pack clear, burst | 2, 3 (landing), 5, 9, 16 |
| Pack clear, sustained zone | 7, 12, 15 |
| Single-target and boss | 1, 4, 6 (DoT), 10, 16 |
| Setup and amplifier | 8, 12, and Resonance from 4, 6, 11 |
| Crowd control | 3, 6, 12, 15 |
| Movement | 13 (and 11 can be cast on the move) |
| Defence | 14 (plus 15 walls and 13 breaking aggro) |
| Ultimate | 16 |

---------------------------------------------------------------------
# PART 2: THE 16 SKILLS
---------------------------------------------------------------------

Source confidence is as in RESEARCH.md. Where the citation or the finding is uncertain or disputed, it is marked with **(!)**.

---------------------------------------------------------------------
## MELEE: THE RIFF
---------------------------------------------------------------------

### 1. Resonant Slam

- **Role:** Melee, spender, single-target burst
- **Tags:** Attack, Melee, Slam, AoE (small), Physical
- **Cost:** 20 Gain, 0.9 s
- **What it does:** Slam the guitar into the target for 300% weapon damage, plus 25% more for each Resonance stack on it. At 5 or more stacks (critical mass) the stacks are doubled first, then all are consumed, and the floor wobbles and shoves nearby enemies sideways.
- **On Beat:** Keeps half of the consumed stacks.
- **Sources**
  - **Paper:** Strogatz, Abrams, McRobie, Eckhardt & Ott, "Crowd synchrony on the Millennium Bridge", *Nature* 438, 43–44, 2005. **(!)** The cause of the wobble is disputed (a *Physics Today* letter). The finding used here is that nothing happens below a critical crowd and everything goes above it.
  - **Game:** *Slay the Spire*, Silent: **Catalyst** (doubles the Poison on an enemy, so you pile up small stacks and one card finishes the job).
  - **Guitar:** Sympathetic string ringing and **palm muting** (the damping hand that kills all the ringing at once).
  - **Condensed:** The bridge gives a hard threshold: 5 stacks is the critical crowd. Catalyst gives the payoff, which doubles the stacks and cashes them in. Palm muting gives the move, because the slam is the heel of the hand damping every ringing string at once.
- **Animation and feel:** A 0.5 s overhead wind-up in which the strings hum, with one extra voice added per stack so the pitch climbs. The target shivers like jelly. Impact is a muted thud with 7 frames of hit-stop. At critical, the planks ripple like a rope bridge, the camera rolls 1.5° for 0.3 s, and enemies skid sideways in a conga line.
- **Scaling:** Weapon damage, Physical, Melee, crit (high-stack slams are the crit window), the "25% more per stack" figure, stack cap (10, raised by passives), Resonance duration, wobble area. Octave Down suits it.
- **Synergies:**
  - Stacks come from Tremolo Flurry, Flytrap Pick and Cricket Chirp.
  - Jelly Patch copies the huge critical hit onto the whole pack.
  - Chladni walls hold enemies for the sideways shove.
  - Humbucker Crescendo also reads stacks.

### 2. Domino Chord

- **Role:** Melee, spender, pack clear
- **Tags:** Attack, Melee, AoE, Duration (delayed), Chaining, Physical
- **Cost:** 15 Gain, 0.7 s
- **What it does:** Chop the floor to light a three-tile power-chord shape in front of you: root, fifth and octave. After 0.8 s the tiles collapse for 200% weapon damage to enemies standing on them. A tile that kills an enemy lights the next tile along, which collapses 0.3 s later (up to 8 tiles), so dense packs cascade.
- **On Beat:** Collapses on the next beat and the cascade limit is +4.
- **Sources**
  - **Paper:** Bak, Chen & Creutz, "Self-organized criticality in the 'Game of Life'", *Nature* 342, 780–782, 1989 (authors and pages from memory, per RESEARCH.md). Local rules lead to avalanches of change whose sizes follow a power law, with many small events and rare huge ones.
  - **Game:** *Fall Guys*, **Hex-A-Gone** (floor tiles that vanish after being touched).
  - **Guitar:** A **power chord** is one three-note shape that moves as a unit on the fretboard grid, a "glider".
  - **Condensed:** The power-chord shape sets the footprint. Hex-A-Gone gives the tiles that fall away. The Life avalanche gives the rule that a kill lights the neighbour, so the cascade size depends on how dense the crowd is.
- **Animation and feel:** A low E5 chug hits the floor. Three foam-mat tiles pop up glowing, like Lite-Brite pegs, and tick for 0.8 s. They fall tile by tile like dominoes, each with a rising marimba "clack". A kill sends a pop of confetti to light the next tile. Short hit-stop on each tile.
- **Scaling:** Area (tile size), Melee Physical, cascade length, kill speed (kills are what pass the chain), Chaining supports. Chorus doubles the shape.
- **Synergies:**
  - Tee Off lands a launched enemy on the tiles.
  - Flytrap Pick's clack pulls the pack onto the shape.
  - Loop Trail slows enemies onto it.

### 3. Tee Off

- **Role:** Melee, spender, crowd control and scatter-clear
- **Tags:** Attack, Melee, Strike, AoE (landing), Knockback, Physical
- **Cost:** 20 Gain, hold up to 1.5 s
- **What it does:** Hold to spin the guitar in windmill circles. Three ticks, one per beat, charge the swing, and releasing smashes the enemy in front like a golf ball. A landing ring appears the instant it is struck, and where it lands it deals 150%, 250% or 400% weapon damage (by ticks charged) and knocks down everything in the ring.
- **On Beat:** Releasing exactly on the third tick is a Perfect Drive: +40% distance and a shockwave at the landing.
- **Boss rule:** Bosses cannot be launched. They are shoved 3 m and the ring forms on them.
- **Sources**
  - **Paper:** Schlegel & Schuster, "Small circuits for large tasks: high-speed decision-making in archerfish", *Science* 319, 104–106, 2008. **(!)** Author order should be rechecked. The fish knocks prey down with a jet and, from the first instants, turns to where it will land, before it lands.
  - **Game:** The **three-click swing** of golf games such as *Hot Shots Golf* / *Everybody's Golf* (start, power, accuracy). **(!)** From memory, not searched.
  - **Guitar:** The Townshend **windmill strum**, which has a backswing, a strike and a follow-through.
  - **Condensed:** The archerfish gives the knock-down and the predicted landing ring, shown the moment of impact. Golf gives a charge you time to a sweet spot. The windmill gives the animation that carries the three ticks.
- **Animation and feel:** The windmill arm circles, and each tick is a golf-tee clink with a pulsing ring. Release has a crack with 8 frames of hit-stop. The enemy spins away in a dotted arc with a "FORE!" bubble. It lands like a bowling ball with a camera pop-in.
- **Scaling:** Weapon damage, knockback distance (the "carry" bonus is +1% damage per metre), landing area, crit on Perfect Drive, bounce count with supports.
- **Synergies:**
  - Land the enemy on Domino tiles or in Chladni walls.
  - A launched Resonance carrier brings its stacks to the landing.
  - Jelly puddles copy the landing damage.

### 4. Tremolo Flurry

- **Role:** Melee, **generator**, single-target ramp
- **Tags:** Attack, Melee, Strike, Physical (applies Resonance)
- **Cost:** none; gives +3 Gain and +1 Resonance per hit
- **What it does:** Hold to jab the target with the headstock. The rate rises through three phases while you stay on the same target: Search (2 hits/s), Approach (4/s, from hit 4) and Buzz (8/s, from hit 8). In Buzz every hit spawns a free Echo hit at 40% damage 0.1 s later, and switching target resets to Search.
- **On Beat:** Start in Approach.
- **Per hit:** 55% weapon damage.
- **Sources**
  - **Paper:** Kalko & Schnitzler (1989), echolocation and hunting behaviour of Daubenton's bat, *Behavioral Ecology and Sociobiology*. **(!)** The exact title and authors are not confirmed (the weakest citation). The phase structure goes back to Griffin, Webster & Michael, *Animal Behaviour* 8, 141–154, 1960. Bats go from search, to approach, to a rapid terminal buzz as the target gets closer.
  - **Game:** *Hearthstone*, **Echo** (Witchwood): a card can be played again the same turn until the limit.
  - **Guitar:** **Tremolo picking**, a rate that escalates until it is a buzz.
  - **Condensed:** The bat gives the three-phase speed-up on one target. Echo gives the free repeat once the buzz starts. Tremolo picking gives the action itself and the sound, a pitch that keeps rising.
- **Animation and feel:** Fast fencer-style neck jabs. A metronome tick starts it. The first phase is slow pings, drawn as thin sonar rings from the headstock. Buzz is a buzzsaw whir with 2 frames of hit-stop per hit, a bigger one every 4th hit, and the Echoes are ghost images. The final hit has a 100 ms silence and then a crunch (the "capture").
- **Scaling:** Attack speed (the phases count hits, so faster hits ramp faster), Echo damage, Gain and Resonance per hit, Delay pedal (repeats the Echo).
- **Synergies:**
  - Feeds Resonant Slam and Humbucker with stacks and fills the Gain for every melee spender.
  - After a Tee Off, ramp on the survivors.
  - Flurry on a Flytrap-rooted target skips Search.

---------------------------------------------------------------------
## RANGED: THE RIG
---------------------------------------------------------------------

### 5. Overdrive Bubble

- **Role:** Ranged, spender, delayed burst AoE
- **Tags:** Attack, Projectile, AoE, Duration, Fire, Sound
- **Cost:** 20 Gain, 0.6 s
- **What it does:** Fire a slow soap bubble that settles at the target spot and swells one pulse per beat, up to four, plus one extra pulse per beat for each enemy inside that has Resonance. It collapses at four pulses, or when you press the skill again, in a white-hot flash. The flash deals 120%, 200%, 300% or 450% weapon damage as Fire, by pulses held.
- **On Beat:** Starts with one pulse.
- **Sources**
  - **Paper:** Gaitan, Crum, Church & Roy, "Sonoluminescence and bubble dynamics for a single, stable, cavitation bubble", *J. Acoust. Soc. Am.* 91, 3166–3183, 1992 (page range from memory). A sound-driven bubble swells and crushes once per acoustic cycle and flashes at the collapse.
  - **Game:** *Civilization VI*, **Eureka boost** (a small preparatory act earns most of a big payoff). **(!)** From memory.
  - **Guitar:** The **volume swell**, and an overdriven tube amp that glows because it is driven hard.
  - **Condensed:** Sonoluminescence gives the pulse-swell-collapse-flash cycle. Eureka gives the prep reward: Resonance on the enemies is the preparatory act and swells the bubble faster. The volume swell gives the build-up of sound.
- **Animation and feel:** A hard strum blows a shimmering bubble out of the output jack. A filament inside glows orange like a vacuum tube, and it breathes bigger with a low "wub" each beat. Before the collapse the sound is sucked out for one frame. Then: a white flash, a flashbulb "pop-FWOOM", 10 frames of hit-stop, a scorch ring and afterimage outlines on enemies.
- **Scaling:** Tempo (more pulses per second), Fire, Area, Projectile count (several bubbles that pulse independently), Overdrive pedal, enemies with Resonance.
- **Synergies:**
  - Flytrap Pick's clack herds the pack in.
  - Resonance from any Generator makes it fill faster.
  - Domino tiles under the bubble collapse into the flash.
  - Jelly Patch copies the flash.

### 6. Flytrap Pick

- **Role:** Ranged, **generator**, root and pull, single-target DoT
- **Tags:** Attack, Projectile, Duration (DoT), Physical
- **Cost:** none; gives +5 Gain and +1 Resonance per pick
- **What it does:** Throw a pick for 90% weapon damage that sticks in the enemy. A lone pick is silent and does not pull the pack, but a second pick in the same enemy within 3 s snaps the trap shut: the enemy is rooted for 1.5 s and the loud CLACK makes enemies within 5 m shuffle toward it. The fifth pick starts digestion, 150% weapon damage as damage over time across 6 s.
- **On Beat:** Counts as two picks.
- **Sources**
  - **Paper:** Böhm, Scherzer, Krol, Kreuzer, Larisch, Becker, Al-Rasheid, Federle & Hedrich, "The Venus flytrap *Dionaea muscipula* counts prey-induced action potentials to induce sodium uptake", *Current Biology* 26, 286–295, 2016. **(!)** Not confirmed by search. The trap closes on the second touch and starts digesting after about five. Burri et al., *PLOS Biology* 2020, found that one touch can sometimes be enough, which is the On Beat rule.
  - **Game:** *Escape from Tarkov* (sound as currency: quiet is safe, noise gives you away).
  - **Guitar:** The **noise gate** (silence until a deliberate hit) and the "touch, don't press" **natural harmonic**.
  - **Condensed:** The flytrap gives the count: 2 snaps, 5 digests, inside a time window. Tarkov gives the sound rule: a lone pick is silent, the snap is loud. The gate gives the audio moment, since everything cuts to silence just before the CLACK.
- **Animation and feel:** The first pick lands with a tiny "tink" and sticks like a trigger hair. On the second, the audio ducks for 80 ms (the gate slamming shut), then a loud CLACK as toy plastic Venus-flytrap jaws snap closed around the enemy. Digestion is bubbling green with a gurgle.
- **Scaling:** Attack speed, Projectile count (a volley can hit several enemies), Pierce, the 3 s window, DoT damage, Resonance per pick.
- **Synergies:**
  - The clack gathers the pack for Overdrive Bubble, Domino Chord and Bumblebee Solo.
  - The root holds a boss still for Resonant Slam.
  - Fast Resonance supply.

### 7. Stompbox Sprinkler

- **Role:** Ranged, spender, sustained zone
- **Tags:** Attack, Projectile, Totem (placed), AoE, Duration, Lightning
- **Cost:** 30 Gain, 0.5 s; lasts 8 beats; up to 2 out at once
- **What it does:** Toss a stompbox that stomps on every beat for 8 beats, in a pattern you pick by tapping the skill before it lands: **Clean** (a steady disc, 70% damage, slows 15%), **Chorus** (six random spots, 60% each) or **Fuzz** (a hard-edged ring with a cross, 140%, knocks inward). All damage is Lightning.
- **On Beat:** The first stomp lands instantly.
- **Sources**
  - **Paper:** Hanlon, Chiao, Mäthger, Barbosa, Buresch & Chubb, "Cephalopod dynamic camouflage: bridging the continuum between background matching and disruptive coloration", *Phil. Trans. R. Soc. B* 364, 429–437, 2009 (authors and pages from memory). The animal chooses among three recipes (uniform, mottle, disruptive) by what the background looks like.
  - **Game:** *Stardew Valley*, **sprinklers** (a cross, then 3×3, then 5×5, placed on a grid).
  - **Guitar:** The **pedalboard** and three tone families: clean, chorus and fuzz.
  - **Condensed:** The octopus gives three patterns, each a different look. Stardew gives the tile-footprint ladder and the placement. The pedalboard gives the names, the LED colours and the thing you place: a stompbox.
- **Animation and feel:** The pedal is thrown like a frisbee and lands with a click. Its LED shows the mode, and the floor patch shimmers in that pattern like skin colour. It stomps in time with the metronome ring, with a bass-drum thump.
- **Scaling:** Tempo (stomps per second), Area (the footprint grows through a cross, then 3×3, then 5×5 floor tiles), duration, Lightning, number of stompboxes, Reverb.
- **Synergies:**
  - Fuzz ring's inward knock stacks enemies into the Bubble.
  - Chorus mode procs on-hit effects well.
  - Clean's slow helps Domino Chord land.

### 8. Jelly Patch

- **Role:** Ranged, spender, damage amplifier
- **Tags:** Attack, Projectile, AoE, Duration, Link
- **Cost:** 15 Gain, 0.5 s; up to 3 puddles, 8 s each
- **What it does:** Lob a jelly glob that splats into a puddle, up to three at once. The puddles are joined by glowing patch cables, and damage dealt to an enemy standing in one is copied at 35% to every other enemy standing in a puddle. Copied damage cannot be copied again.
- **On Beat:** The copy rises to 50% for that puddle.
- **Sources**
  - **Paper:** Simard, Perry, Jones, Myrold, Durall & Molina, "Net transfer of carbon between ectomycorrhizal tree species in the field", *Nature* 388, 579–582, 1997. **(!)** The title wording is unresolved and the net benefit is contested (a 2023 critique). Trees joined by a fungal network swap resources, and a cedar that is not joined does not.
  - **Game:** *Portal 2*, **gels** (paint a surface once and everything that touches it is transformed).
  - **Guitar:** **Patch cables** and the **ABY box** (one signal sent to many outputs).
  - **Condensed:** The fungal network gives the shared pool: joined members share what they get, and non-members do not. Portal gel gives the idea of painting a spot once so that it transforms later hits. Patch cables give the visible links.
- **Animation and feel:** The glob wobbles and lands with a cartoon "boing" and a squish. Each puddle jiggles like jelly. Cables sprout under the floor like roots, with small mushrooms at the joints. Shared hits travel as bright pulses along the cables with a patch-cable "bzzt".
- **Scaling:** Puddle count, copy percentage, duration, puddle area. It copies every damage type. Chaos copies need no special rule.
- **Synergies:**
  - The best partner for single-target hits: a Resonant Slam critical, a Bubble flash or a Tee Off landing, copied across the pack.
  - Flytrap Pick roots the target in the puddle.
  - Loop Trail slows the network.

---------------------------------------------------------------------
## CASTER: THE PEDALBOARD
---------------------------------------------------------------------

### 9. Bumblebee Solo

- **Role:** Caster, spender, roaming pack clear
- **Tags:** Spell, AoE, Duration, Chaining, Lightning
- **Cost:** 30 Gain, 0.6 s; lasts 8 beats
- **What it does:** Summon a toy bumblebee inside a 12 m ring. Each beat it hops to the nearest enemy it has not zapped yet and zaps there for 120% lightning damage (3 m radius), and when no enemy is near it takes one long leap across the ring to the biggest cluster. The ring shrinks 10% per beat, so late hops land closer together and the bee's final zap is double.
- **On Beat:** Lasts 9 beats.
- **Sources**
  - **Paper:** Viswanathan, Buldyrev, Havlin, da Luz, Raposo & Stanley, "Optimizing the success of random searches", *Nature* 401, 911–914, 1999 (author list from memory). **(!)** Reanalyses (Edwards et al. 2007) dispute whether real animals do this. When targets are sparse, many short steps with rare long leaps is the best search.
  - **Game:** The shrinking **storm circle** of *Fortnite* / *PUBG* (not searched).
  - **Guitar:** The **solo** (short runs with rare octave leaps) and the shred showpiece "Flight of the Bumblebee". **(!)** From memory.
  - **Condensed:** The Lévy walk gives the hop rule: short hops when there are targets close by, a long leap when there are not. The storm gives the shrinking ring that squeezes late hops. The solo gives the sound: a run of notes with an octave jump.
- **Animation and feel:** A little wind-up bumblebee with a key in its back. Each short hop is a quick chromatic run of sixteenth notes. A long leap is an octave-jump glissando with a bright zip and a trail. A chalk or hula-hoop ring shrinks on the floor, and the last zap is a chord with a flash.
- **Scaling:** Tempo (hops per second), duration in beats, Area, Lightning, extra bees (Chorus), chain count.
- **Synergies:**
  - Flytrap Pick's clack makes short hops dominate.
  - Loop Trail funnels enemies into a cluster for its leaps.
  - Jelly Patch copies its zaps.
  - Overdrive pedal converts it to fire.

### 10. Patch Cables

- **Role:** Caster, spender (per second), channelled bossing
- **Tags:** Spell, Channelling, Duration, Lightning
- **Cost:** 10 Gain per second; range 12 m; you walk at 50% speed
- **What it does:** Channel to plug cables into up to 4 enemies nearest to you. Each cable's damage ramps one tier per second (100%, 200%, 300% then 400% lightning damage per second). Every second the cable with the least total damage is pruned and its tiers are added to the strongest, so the web narrows to one thick cable.
- **On Beat:** Start at tier 2.
- **Sources**
  - **Paper:** Tero, Takagi, Saigusa, Ito, Bebber, Fricker, Yumiki, Kobayashi & Nakagaki, "Rules for biologically inspired adaptive network design", *Science* 327, 439–442, 2010. A slime mould grew a network as good as Tokyo's rail system: tubes that carry more flow thicken, and tubes that carry less thin away.
  - **Game:** *Overwatch*, **Symmetra's** beam (it locks to one target and ramps through three levels).
  - **Guitar:** The **patch cable** web of a pedalboard, and **sustain** (sound that thickens the more it is fed).
  - **Condensed:** Physarum gives the self-pruning web: wide at first, thin at the end. Symmetra gives the tier ramp that rewards staying locked. The patch cable gives the object: cables from the jack.
- **Animation and feel:** The guitar's jack spits out four cables that snake across the floor like slime mould. The thick cable hums louder as it grows, with a rising sustained note. Pruned cables go limp and fizzle. The last cable swells fat and ends in a bright arc and a screech.
- **Scaling:** Cast speed (channel tick rate), Lightning, number of cables, max tier, Gain cost reduction, range.
- **Synergies:**
  - It starts as add-clear and finishes as a boss beam.
  - Flytrap Pick's root keeps the target in range.
  - Jelly Patch copies each tick.
  - Standby stops Gain decay while you wait for the next channel.

### 11. Cricket Chirp

- **Role:** Caster, **generator**, cast while moving
- **Tags:** Spell, Channelling, AoE, Sound, Fire (applies Resonance)
- **Cost:** none; gives +2 Gain and +1 Resonance per chirp; 4 m ring, 40% fire damage per chirp
- **What it does:** Hold to chirp, sending a ring of sound out from you, and you can do it while walking at full speed. The chirp rate is 2 per second, plus 1 per 25 Gain you hold, plus 1 while you are moving. A hot cricket sings faster.
- **On Beat:** Starting on the beat gives a free first chirp.
- **Sources**
  - **Paper:** Dolbear, "The Cricket as a Thermometer", *The American Naturalist* 31, 970–971, 1897 (volume and pages from memory). Chirp rate rises with temperature (T°F ≈ chirps in 15 s + 40).
  - **Game:** *Braid*, World 3 "Time and Place" (time only moves when you move). **(!)** From memory.
  - **Guitar:** **Tremolo picking** and **tempo** (BPM): chirps per minute are beats per minute.
  - **Condensed:** Dolbear gives the rule that a hotter cricket sings faster, and Gain is the thermometer. Braid gives the movement rule: moving winds it up. Tremolo picking gives the sound and the rate.
- **Animation and feel:** A wind-up cricket sits at your boot and rubs its legs, a thin stridulating "treble" ticking on the beat. A thermometer gauge on the amp goes from blue to red. At high Gain the cricket glows and steams, and each chirp ring has a small hit-stop.
- **Scaling:** Cast speed, Tempo, Gain per chirp, Fire, Area, Resonance per chirp.
- **Synergies:**
  - The caster's way to kite and still fill Gain for Bumblebee and Patch Cables.
  - Resonance feeds Overdrive Bubble's swell (Eureka) and Humbucker.
  - Loop Trail sets the slow and Chirp rings keep the pack inside it.

### 12. Loop Trail

- **Role:** Caster, spender, slow zone and funnel
- **Tags:** Spell, AoE (line), Duration, Cold
- **Cost:** 15 Gain, 0.6 s; 10 m long, lasts 6 s
- **What it does:** Sweep a trail of sticky notes along the floor that slows enemies crossing it by 25% and chills them for 40% cold damage per second. Each new enemy that crosses reinforces the trail by +10% slow and +10% damage (up to 5 times) and adds 0.5 s of duration. Casting along an existing trail overdubs it and doubles its current reinforcement.
- **On Beat:** Starts with 2 reinforcements.
- **Sources**
  - **Paper:** Deneubourg, Aron, Goss & Pasteels, "The self-organizing exploratory pattern of the Argentine ant", *Journal of Insect Behavior* 3, 159–168, 1990 (citation details from memory). Ants amplify small differences with pheromone, and a trail is a vote that grows.
  - **Game:** *Bloons TD 6*, **Glue Gunner** (a slow that multiplies every other tower). **(!)** From memory.
  - **Guitar:** The **looper pedal** (record a phrase, then layer it).
  - **Condensed:** The ant trail gives the positive feedback: the more enemies cross it, the stronger it gets. The Glue Gunner gives the slow effect. The looper gives the overdub, a second pass layered on top.
- **Animation and feel:** A glittering line of looped notes is chalked onto the floor, with toy ants carrying crumbs along it. Each crossing adds another layer of glow and a denser looped sample. The slow is a wet glue squelch. The trail fades like a decaying delay.
- **Scaling:** Length (Area), duration, Cold, slow strength, reinforcement cap, Reverb.
- **Synergies:**
  - The slow lets Domino Chord and Bumblebee Solo land on a bunched pack.
  - Chirp rings and Stompbox pulses finish the slowed.
  - Pairs with Tee Off: launch into the trail.

---------------------------------------------------------------------
## UTILITY
---------------------------------------------------------------------

### 13. Cable Snap (movement)

- **Role:** Movement
- **Tags:** Movement, Sound, AoE (line), Physical
- **Cost:** 2 charges, 3.5 s recharge each; range 14 m
- **What it does:** Hold to stretch the cable to a marker, and release to snap there instantly, passing through enemies and floor gaps; enemies on the line are twanged sideways. On landing you are unplugged for 0.8 s: enemies drop their aggro on you. Your next hit within that time deals 30% more (an ambush).
- **On Beat:** Releasing on the beat restores the charge.
- **Sources**
  - **Paper:** Ingber, "The Architecture of Life", *Scientific American* 278(1), 48–57, 1998. Cells keep their shape by a balance of tension and compression: poke the structure and it springs back.
  - **Game:** *Dishonored*, **Blink** (a landing marker, then you arrive almost instantly, and stealth follows).
  - **Guitar:** The **whammy bar dive** and recovery, and the **cable** as a tether under tension.
  - **Condensed:** Tensegrity gives the stretch-and-snap action. Blink gives the marker, the instant arrival and the quiet moment after landing. The whammy bar gives the sound: a dive-bomb that recovers.
- **Animation and feel:** The cable stakes into the ground at the marker with a "thunk" and stretches like a rubber band. A tension hum rises in pitch with the distance. Release is a "pwang!" with a whammy dive-bomb. You fly along a trail of stretched cable. On landing the audio ducks and your outline goes translucent.
- **Scaling:** Charges, range, recharge speed, post-landing ambush bonus, movement speed (Wah).
- **Synergies:**
  - Escape after Standby, or get into Tee Off range.
  - The ambush hit is a free Resonant Slam.
  - Land into a Chladni wall as safe ground.

### 14. Standby (defence)

- **Role:** Defence
- **Tags:** Channelling, Duration, Cold
- **Cost:** free; hold; 8 s cooldown after waking
- **What it does:** Hold to flip the amp to Standby: you stop moving, take 50% less damage rising to 90% over 3 s, and cannot be stunned or knocked back. Gain stops decaying and you regenerate 5% of your life per second. When you wake, a third of the damage you prevented returns as a 4 s bleed, capped at 25% of your maximum life.
- **On Beat:** Releasing on the beat halves the bleed.
- **Sources**
  - **Paper:** Shankar et al., "Hummingbird torpor in context: duration, more than temperature, is the key to nighttime energy savings", *Journal of Avian Biology*, 2020. **(!)** The author list is unverified. Torpor saved 65–92% of energy per hour, but how long the bout lasted mattered more than depth.
  - **Game:** *Frostpunk*, **Emergency Shift** (borrow now, pay later).
  - **Guitar:** The **amp standby switch** and the **full palm mute**, a hand laid flat on all the strings.
  - **Condensed:** Torpor gives a defence whose value grows with how long you hold it. Emergency Shift gives the cost: the debt comes back when you wake. The standby switch gives the on/off action.
- **Animation and feel:** The hero hugs the guitar, goes blue-grey, and a nightlight glow and floating "z" notes appear. Hits land with a dull muted thunk, with no hit-stop. Waking is the amp's "pop" and a thump of the debt, with the hero shaking sleep off.
- **Scaling:** Max reduction, ramp speed (the 3 s), regeneration, debt percentage and cap, cooldown.
- **Synergies:**
  - Gain stays full for Slam or Finale after waking.
  - Cable Snap to leave.
  - Chladni walls give a place to hide while you hold it.

### 15. Chladni Plate (utility)

- **Role:** Utility, reshape the floor
- **Tags:** Spell, AoE, Duration, Physical
- **Cost:** 10 s cooldown; radius 6 m; lasts 6 s
- **What it does:** Slam a glitter-covered plate on the target area, and tap to cycle through the 12th, 7th and 5th harmonics, which give 1, 2 or 3 nodal lines. The nodal lines harden into foam walls that block movement and root any enemy touching them. The floor between the lines buzzes for 60% damage each beat and pushes enemies toward the nearest line.
- **On Beat:** The walls form instantly.
- **Sources**
  - **Paper:** Chladni, *Entdeckungen über die Theorie des Klanges*, 1787 (the later Faraday paper is not used). Sand on a driven plate gathers on the still lines (nodes), and each frequency gives its own pattern.
  - **Game:** *Prey* (2017), **GLOO Cannon** (foam that hardens into walls, platforms and plugs).
  - **Guitar:** **Natural harmonics** at the 12th, 7th and 5th frets, which are the nodal points of the string.
  - **Condensed:** Chladni gives the rule that the frequency picks the pattern and stuff ends up on the still lines. GLOO gives the hardening into usable walls. The harmonics give the three settings, the player's choice of node count.
- **Animation and feel:** A big drum skin dusted with glitter or kinetic sand comes down with a drum-roll. Glitter races into lines and sets as pastel foam. The floor between the lines buzzes with a bowed-string drone, and enemies are pushed to the lines like sand.
- **Scaling:** Duration, Area, cooldown, wall durability, damage per beat, Reverb.
- **Synergies:**
  - Root plus Resonant Slam on the wall.
  - Tee Off lands enemies into the walls.
  - Fuzz and Bubble finish the penned pack.
  - Standby behind a wall.

### 16. Humbucker Crescendo (ultimate)

- **Role:** Ultimate
- **Tags:** Attack, Spell, AoE (line), Lightning, Sound
- **Cost:** needs 50 Gain and spends all of it; 25 s cooldown
- **What it does:** Hold to charge while moving at half speed; sparks flash blue, orange then pink at 1, 2 and 3 s. Release to fire a magnetic beam along your aim that snaps every enemy inside it onto the centre line and drags them to its end, where they detonate for 600%, 1000% or 1600% weapon damage (by tier). Damage is 1% more per Gain spent and 4% more per Resonance stack on each enemy, and you gain a turbo (+20% movement speed) for 2, 3 or 4 s.
- **On Beat:** Releasing on the beat adds a tier (up to pink).
- **Sources**
  - **Paper:** Blakemore, "Magnetotactic bacteria", *Science* 190, 377–379, 1975 (volume and pages from memory). Cells contain a chain of magnetite crystals that works as a compass needle and lines them up along magnetic field lines.
  - **Game:** *Mario Kart*, **drift mini-turbo** (hold a drift, sparks go through colour tiers, release for a boost proportional to the charge). **(!)** From memory.
  - **Guitar:** The **humbucker pickup** (magnets under the strings) and the **crescendo** to the final chord.
  - **Condensed:** The bacteria give the idea of aligning along a field line. Mario Kart gives the tiered charge and the speed reward on release. The pickup and the crescendo give the theme and the build to the last chord.
- **Animation and feel:** Pickup lights glow on the guitar. Fridge magnets, paperclips and loose toys fly toward you, and drift sparks fly from your heels with a rising synth chirp. At pink the screen vignettes. Release is a giant power chord, iron-filing field lines are drawn on the floor like a Magna Doodle, and enemies line up like a conga line. They detonate in stage pyro and confetti, with a 12-frame hit-stop and a spotlight.
- **Scaling:** Weapon damage, Gain held (so Crunch and Gain-retention stats), Resonance stacks, beam width and length, cooldown, turbo duration, charge speed.
- **Synergies:**
  - The end of every build loop: fill Gain, stack Resonance, then release.
  - Cable Snap into position.
  - Jelly Patch copies the detonation.

---------------------------------------------------------------------
# PART 3: THREE EXAMPLE BUILDS
---------------------------------------------------------------------

## Build A: Riff Bruiser (melee-led)

- **Bar:** Tremolo Flurry (generator), Resonant Slam, Domino Chord, Tee Off, Cable Snap, Standby, Humbucker Crescendo. One ranged tool: Jelly Patch.
- **Pedals:** Octave Down on Resonant Slam, Delay on Tremolo Flurry (repeats the Echo), Chorus on Domino Chord.
- **Stats:** Attack speed, crit, Physical, max Resonance stacks, Gain on hit.
- **Clear:** Tee Off a clump so it lands in a pack, Domino Chord on the landing, and Flurry on the survivors to refill Gain.
- **Boss:** Cable Snap in for the ambush, Flurry into Buzz to build 5+ Resonance, then Resonant Slam on the beat (doubling the stacks and keeping half). Jelly Patch under the boss and adds copies the slam to everything nearby. Standby when the boss telegraphs a big hit.
- **Weakness:** Range. Cable Snap and Tee Off answer it, and ranged bosses are the trouble.

## Build B: Pick Rigger (ranged-led)

- **Bar:** Flytrap Pick (generator), Jelly Patch, Overdrive Bubble, Stompbox Sprinkler, Cable Snap, Chladni Plate, Humbucker Crescendo.
- **Pedals:** Chorus on Flytrap Pick (volley of picks), Overdrive on Bubble, Reverb on Stompbox.
- **Stats:** Projectile count, Area, Duration, Tempo, Fire and Lightning.
- **Clear:** Tag two enemies at the edge with Flytrap Pick (one on beat counts as two). The CLACK pulls the pack together. Jelly puddles go down in the middle, the Bubble swells fast because the Resonance on the pack feeds it, and a Fuzz Stompbox ring pens them in.
- **Boss:** Five picks for rooted digestion while the Stompbox's Clean mode slows it. Chladni walls stop adds, and Cable Snap keeps you out of range.
- **Cross-group tool:** Chladni Plate from utility. Resonance from Flytrap Pick also feeds the Finale.
- **Weakness:** Setup time. A fast boss that will not stay in the zone beats it.

## Build C: Pedalboard Mage (caster-led)

- **Bar:** Cricket Chirp (generator), Bumblebee Solo, Patch Cables, Loop Trail, Chladni Plate, Cable Snap, Standby, Humbucker Crescendo. One ranged tool: Overdrive Bubble.
- **Pedals:** Tempo-focused: Wah on Cable Snap, Delay on Bumblebee Solo, Reverb on Loop Trail.
- **Stats:** Tempo, cast speed, Area, Duration, Lightning and Fire, Gain retention.
- **Clear:** Kite and chirp: Cricket Chirp fills Gain while you walk and keeps the pack in the Loop Trail slow. Bumblebee Solo hops through the bunched pack. Overdrive Bubble goes down on the pile of Resonance carriers.
- **Boss:** Chirp until Resonance is stacked and Gain is high, Patch Cables from range (the web starts on the adds and narrows to the boss), and Chladni walls to block adds. Standby to hold Gain and heal when a big hit is coming, and Humbucker Crescendo to finish.
- **Weakness:** Being caught. Cable Snap, the Loop Trail slow and Standby are the answers, and a mistimed Standby leaves a gap in Gain flow.

---------------------------------------------------------------------
## Source notes

- Citations marked **(!)** are uncertain, disputed or from memory, as flagged in RESEARCH.md. The weakest is Pair 4 (Kalko & Schnitzler). The disputed findings are Millennium Bridge (cause), Venus flytrap (one touch), mycorrhizal net transfer and Lévy flight (reanalysis).
- Game mechanics for Fall Guys, Civilization VI, Symmetra, Braid, Bloons, Blink, Frostpunk, Prey, Mario Kart and the battle-royale storm are from memory and were not searched.
- The design uses each finding as an *inspiration for a rule*, not as proof: if a finding is later overturned, the skill still works as a game mechanic.
