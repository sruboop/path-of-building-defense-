# The Slugger, take 2: 16 fused bat skills

Same hero, same giant backyard / bedroom / garage / little-league field at dusk. The old kit was sixteen
baseball facts with a number attached. This kit starts from a **surprising rule** (taken from a real
paper and a real game skill) and then finds the baseball move that already behaves that way. Each skill
is still one sentence of rules you can read at a glance.

All numbers are playtest starting points, not balanced values. Paper findings are quoted from
RESEARCH.md; items it marks unverified are marked again here.

## Core systems (kept small, three, slightly upgraded)

| System | Rule |
|---|---|
| **Runners** (0 to 3) | Same as before. Generators put runners on base, spenders drive them in. Three is **Bases Loaded**. |
| **Barrel** | Same as before. A late sweet-spot window on every swing gives a guaranteed crit, the longest hit-stop, the loudest *CRACK* and +1 Runner from generators. Attack speed does not widen it. |
| **The Count** *(changed)* | Hits put **Strikes** on an enemy. Strikes now **decay after 6 s** without a new hit (borrowed from the flytrap's decaying calcium). The 3rd is a **Strikeout**: stunned 1.5 s, +25% damage taken for 4 s. |
| **Set** *(new keyword)* | An enemy turned solid. It can't move or act, takes +20% damage, and a **Barrel or any hit over 150% of its life-bar slice shatters it** (small AoE based on the hit). Water (sprinklers, puddles, Rain Delay's tarp splash) un-sets it. |

**Tags used:** Attack, Melee, Projectile, Area, Chain, Movement, Guard, Totem, Summon, Trail, Light,
Channel, Cancel, Rhythm, Duration, Cooldown, Ultimate. **Stats that matter:** attack speed, crit,
projectile speed and count, area, duration, cooldown recovery, movement speed, minion damage, block
and deflect window.

## Coverage at a glance

| Role | Skills |
|---|---|
| Generators | 15 Walk-Up Song (main attack), 10 Fungo (ranged), 1 Foul Tip (defensive) |
| Spenders | 8 Three-Pitch Mix, 13 Knuckleball, 12 Hang Time (rocket), 6 Time Out |
| Pack clear | 10 Fungo, 13 Knuckleball, 15 Walk-Up Song (Fold 3), 16 Benches Clear |
| Single target | 2 Full Count, 8 Three-Pitch Mix |
| Movement | 3 Chase the Fly (gap-closer), 11 Tag Up (retreat), 12 Hang Time (traverse) |
| Defence | 1 Foul Tip, 5 Hidden Ball Trick, 6 Time Out, 7 Backstop, 9 Rain Delay |
| Control / zone | 4 Pine Tar, 14 Ping Pad |
| Ultimate | 16 Benches Clear |

---

## 1. Foul Tip
*Pair 1: non-Newtonian fluids x souls-like*
- **Tags:** Guard, Attack, Area, Timing. No cooldown, 0.4 s lockout after use.
- **Does:** Tap Guard just before a hit lands (0.25 s window). The hit is negated, the attacker takes a Strike, you gain a Runner, and a white ring spreads out from the impact point and **Sets** every enemy it passes. Press too early or mash and the window shrinks to 0.12 s, and a miss is only a soft 30% block.
- **Sources:**
  - *Paper:* Waitukaitis & Jaeger, "Impact-activated solidification of dense suspensions via dynamic jamming fronts", *Nature* 487, 2012. A hard hit makes a solid front that grows outward from the impact and exists only while it moves. A slow press stays liquid.
  - *Game:* *Sekiro*, Deflect. A tap just before the hit negates it and builds the enemy's Posture. Mashing shrinks the window.
  - *Baseball:* the foul tip, a ball that goes sharp and direct from the bat into the catcher's glove and counts as a strike.
  - *Condensed:* The Deflect is the impact. The jamming front is the Posture payoff, so a perfect tap hardens the pack outward from the attacker. The ring is just a shockwave that sets what it touches. Fast hits go solid, slow hits stay soft, which is also the anti-mash rule.
- **Animation and feel:** The bat comes up flat. On success: a sharp *tink*, a white spark, 5 frames of hit-stop, then a cornstarch-white ring ripples out and enemies stiffen with a rubbery *bwomp* and hairline cracks. The attacker gets a "STRIKE!" pip. A mistimed tap gives a dull *thup* and a squish.
- **Scaling:** deflect window, ring radius (grows with area **and with the damage you deflected**), Set duration, damage taken by Set enemies, shatter damage, Runner gain, block.
- **Synergies:** Set enemies shatter on any Barrel, so it feeds Walk-Up Song and Fungo. Time Out follows it for a free reposition. Pine Tar and Foul Tip stack Set sources. Full Count counts the Strike it gives.

## 2. Full Count
*Pair 2: plant electrical signalling x survival horror*
- **Tags:** Light, Channel, Single target, Duration. Cooldown 6 s.
- **Does:** Hold to point the stadium floodlight at one enemy. A shrinking ring burns off its shield or armour layer (about 1.2 s; spend a Runner to double the speed). Then it is **on the count** for 6 s: a lone hit does nothing, the **2nd hit snaps** (big crit damage, 1 s stun), and the **5th hit** (all five lights lit) is the **Full Count**: a huge finisher that refunds 2 Runners.
- **Sources:**
  - *Paper:* Böhm, Scherzer, Krol, Hedrich et al., "The Venus Flytrap *Dionaea muscipula* Counts Prey-Induced Action Potentials to Induce Sodium Uptake", *Current Biology* 26, 2016. One touch primes, a second within about 20 s snaps, 3 or more start digestion, 5 or more start absorption. Calcium decays, so it ignores a raindrop.
  - *Game:* *Alan Wake*. The flashlight burns the Taken's darkness shield, a shrinking ring shows progress, boost spends battery, then you shoot.
  - *Baseball:* the full count (3 balls, 2 strikes) is five pitches in, and the next pitch decides the at-bat. Dusk floodlights are the setting.
  - *Condensed:* Burning the shield is the light. The flytrap's thresholds are the punish. The shrinking ring turns into the scoreboard's five pips (3 green balls, 2 red strikes) and a lone raindrop (one hit) does nothing.
- **Animation and feel:** The floodlight tower clicks on with a *ka-chunk* and hum. A shutter ring closes on the enemy. Each hit lights a scoreboard pip with a bell *ding*. The snap is a clamp-shut *chomp*, the 5th pip a big *CRACK* with a camera push.
- **Scaling:** channel speed, window length, snap and finisher damage (crit), Runners refunded, shield-burn speed. Light radius lets the beam hit a second target at reduced strength.
- **Synergies:** The shield-breaker for armoured elites and bosses. Foul Tip, Three-Pitch Mix and Walk-Up Song supply the 5 hits quickly. Hidden Ball Trick keeps the crowd off you while you channel.

## 3. Chase the Fly
*Pair 3: bat echolocation x physics puzzle game*
- **Tags:** Movement, Attack, Lock. 2 charges, 4 s recharge.
- **Does:** Dash toward the cursor. If an enemy is inside a narrow 3° cone along your aim, you lock on and **curve in on a constant bearing** to intercept it even while it moves. You finish with a bat smash whose damage and knockback scale with **your movement speed when you cast**, and you keep that speed afterwards.
- **Sources:**
  - *Paper:* Ghose & Moss, "The sonar beam pattern of a flying bat as it tracks tethered insects", *J. Acoust. Soc. Am.*, 2003, and Ghose, Horiuchi & Moss, 2007 (two-lobed beam). The bat holds its sonar beam on one target within about 3° and keeps the bearing to it constant while it closes. The exact title of the "looking-around versus homing-in" paper was not confirmed.
  - *Game:* *Portal*, momentum flinging. Speed is conserved through the portal and you leave at the speed you built.
  - *Baseball:* an outfielder running down a fly ball curves so the ball keeps a steady line in his view (McBeath, Shaffer & Kaiser, *Science*, 1995). I recalled this reference from memory, so verify it.
  - *Condensed:* The 3° gaze is the aim lock. Constant bearing is the outfielder's curved route. "Exit at the speed you entered" is the portal rule. One line: *aim roughly, curve in, hit as hard as you were running.*
- **Animation and feel:** A two-lobed chirp ring appears on the target with a high bat-squeak *eek-eek*. You leave a curving speed line as you run the route, and the smash lands with a *pock* and a yellow "CAUGHT!" pop-up.
- **Scaling:** movement speed (distance and damage), charges, lock cone width, melee damage, cooldown recovery. The speed carry means Tag Up and Hang Time landings feed the next Chase.
- **Synergies:** The gap-closer into Foul Tip, Full Count or Walk-Up Song. A knocked-back enemy is a moving lock target.

## 4. Pine Tar
*Pair 4: tardigrade survival x immersive sim*
- **Tags:** Projectile, Area, Duration, Set. Cooldown 8 s.
- **Does:** Throw a tub of pine tar that splats into an amber patch. Enemies in it are slowed, and after 1.5 s they **Set** inside the glass. **You** standing in the patch gain a **glass shell** (a barrier worth 20% of max life that does not decay while dry). Water melts both.
- **Sources:**
  - *Paper:* Boothby, Tapia, Brozena, ... Goldstein, "Tardigrades Use Intrinsically Disordered Proteins to Survive Desiccation", *Molecular Cell* 65(6), 2017. Tardigrades dry into a protective glass (vitrification), and adding water dissolves it.
  - *Game:* *Prey*, GLOO Cannon. It does no damage, hardens on contact, freezes enemies who then take bonus damage, and can be used as a tool.
  - *Baseball:* pine tar on the bat handle (the 1983 George Brett Pine Tar Incident).
  - *Condensed:* The GLOO foam is the tar. The tardigrade glass is a shell that protects whoever is dry and dissolves in water. So a sticky patch sets enemies and shields you, and sprinklers are both your best friend and your worst enemy.
- **Animation and feel:** A lazy underhand toss and a gooey *splorp*. The tar goes from black to glassy amber with a creaking *crrrk*. Set enemies look like toys in candy. The shell chimes like a wine glass, and it hisses into steam when soaked.
- **Scaling:** area, duration, Set time, barrier strength, damage taken by Set enemies, cooldown recovery.
- **Synergies:** Set-then-shatter with any Barrel. Hidden Ball Trick lures enemies in. Do not use it near sprinklers (or use that on purpose to reset a lane).

## 5. Hidden Ball Trick
*Pair 5: cellular automata x stealth game*
- **Tags:** Summon, Decoy, Duration. Cooldown 12 s.
- **Does:** Plant a cardboard cutout of yourself for 6 s. Nearby enemies switch to attacking it, and **each distracted enemy distracts the enemies touching it** one step at a time, so a checkerboard wave rolls outward across the pack. Enemies with a dot over their head (elites and bosses, the Enforcers) are **not fooled**. Distracted enemies are **off the bag**: your next hit on one deals +50% damage.
- **Sources:**
  - *Paper:* Mordvintsev, Randazzo, Niklasson & Levin, "Growing Neural Cellular Automata", *Distill*, 2020 (summary taken from follow-up papers; the article itself was not opened). Every cell follows the same tiny local rule, sees only its neighbours, grows from one seed, and regrows when damaged.
  - *Game:* *Hitman*, disguises and Enforcers. Most NPCs accept your outfit, and only marked Enforcers can see through it.
  - *Baseball:* the hidden-ball trick, where a fielder fakes the throw back to the pitcher and tags the runner who wanders off the bag.
  - *Condensed:* The disguise is the cutout. The local rule is "if my neighbour is fooled, I am fooled", which spreads the trick from one seed. The cutout regrows 10% of its life per second like a self-repairing automaton. The Enforcer dot makes the exception readable.
- **Animation and feel:** You pop a cardboard cutout (your pose, goofy grin) with a *thwip* of a cardboard tab. A chequered tile wave spreads from it with tiny cartoon "?" bubbles. The wave stops at Enforcers, whose dot flashes red. The off-the-bag hit has a sneaky *gotcha* sound.
- **Scaling:** cutout life and regrowth, duration, number of cutouts, spread steps, off-the-bag bonus.
- **Synergies:** The safe moment for channelling Full Count, setting up Backstop or collecting Rain Delay. Spread-out enemies are easy pickings for Fungo and Knuckleball.

## 6. Time Out
*Pair 6: starling murmurations x fighting game*
- **Tags:** Cancel, Area, Slow. Costs 1 Runner. No cooldown.
- **Does:** Call "Time!" during any animation or recovery. It cancels what you are doing and sends a slow ring to the **7 nearest enemies, no matter how far away they are**, rippling from the closest to the furthest. The ring adapts to the situation: after a hit it counts as a hit on them, after a whiff it refunds the Runner, and if an attack is about to land it lets you step aside.
- **Sources:**
  - *Paper:* Ballerini et al., "Interaction ruling animal collective behavior depends on topological rather than metric distance", *PNAS* 105, 2008. A starling reacts to its 6 to 7 nearest neighbours, not everyone within X metres, and turns pass bird to bird in waves.
  - *Game:* *Guilty Gear -Strive-*, Roman Cancel. A bar spend cancels your move, makes a slowing shockwave, and has different colours for hit, whiff and block.
  - *Baseball:* the batter asking the umpire for "Time!" (a real rule).
  - *Condensed:* The cancel is the time-out. The shockwave hits the **nearest seven**, like a flock's neighbour rule, so it works the same in a crowd or when enemies are sparse. The three colours become one skill that does the right thing for the moment.
- **Animation and feel:** You raise a palm, a whistle blows, the colours drain and a ring of sepia radiates with a *whoomp*. The slow travels visibly from enemy to enemy in a wave. Red, purple and yellow outlines show the three contexts.
- **Scaling:** number of neighbours (7 can go up), slow strength and duration, on-hit effects (it counts as a hit), Runner cost reduction.
- **Synergies:** Cancels Walk-Up Song's recovery, Hang Time's landing and Three-Pitch Mix's release. Foul Tip then Time Out repositions you for free. The slow keeps a distant seven in range for Fungo.

## 7. Backstop
*Pair 7: tensegrity x city builder*
- **Tags:** Totem, Guard, Area, Duration. Cooldown 10 s, lasts 8 s.
- **Does:** Hammer four stakes into the ground and stretch a rope net across them. Choose a **law** when you cast: tap for **Taut** (projectiles bounce back at +50% damage, but little life) or hold for **Slack** (it catches projectiles and enemies, with lots of life). All damage to the net is **shared across the whole net** and stored as Tension. If a single stake falls, the net collapses and **releases the stored tension as a blast**.
- **Sources:**
  - *Paper:* Ingber, "Tensegrity I. Cell structure and hierarchical systems biology", *J. Cell Science* 116, 2003. Cables under pre-stress are balanced by isolated compressed struts, so a push on one point is shared by the whole network, and removing the tension makes it fail.
  - *Game:* *Frostpunk*, Book of Laws. You choose between permanent laws, each with a visible meter cost, and some are mutually exclusive.
  - *Baseball:* the backstop net behind home plate and "ground rules" (little-league fields have house rules).
  - *Condensed:* The net is the tensegrity. The "law" is the Taut-or-Slack choice, a visible trade-off you commit to for the cast. Collapse is the payoff for the tension that was shared and stored.
- **Animation and feel:** Four stakes thunk in, ropes snap tight with a *twang* and the net hums. Every hit makes the net bulge and pluck a different note. At collapse the ropes whip outward with a harp-string *SPROING*.
- **Scaling:** net life, reflect damage (Taut), stored-tension blast (Slack), area, duration, number of nets.
- **Synergies:** Enemies caught by Pine Tar or Hidden Ball Trick sit inside the blast. Knuckleball and Fungo balls ricochet off it. Ping Pad covers the gaps in the net.

## 8. Three-Pitch Mix
*Pair 8: archerfish spitting x roguelike deckbuilder*
- **Tags:** Projectile, Queue, Single target. Channel is free; release costs 1 Runner.
- **Does:** Each cast loads the next pitch into a queue of three balls that orbit you: **changeup** (slow, slows what it touches), **slider** (curves), **fastball** (pierces). Orbiting balls ping nearby enemies for small damage. Release throws them in queue order, slowest first, and each one is faster than the last, so they **catch up and merge into one huge drop** that hits the target. A fourth load pushes out the oldest ball as a small burst.
- **Sources:**
  - *Paper:* Vailati, Zinnato & Cerbino, "How Archer Fish Achieve a Powerful Impact: Hydrodynamic Instability of a Pulsed Jet in *Toxotes jaculatrix*", *PLoS ONE* 7(10), 2012. The jet speeds up as it is spat, so the fast tail catches the slow head and merges into one drop that hits harder than the fish's muscles could.
  - *Game:* *Slay the Spire*, Defect's Orbs. A queue of orbs gives a small passive each turn and a big payoff when evoked, and a new orb evokes the oldest.
  - *Baseball:* pitch sequencing. A changeup followed by a fastball makes the fastball look faster.
  - *Condensed:* The orb queue is the pitch queue. The release order slow to fast is the jet's pulsed speed profile, so **the sequencing is the skill**. A fastball thrown first never merges.
- **Animation and feel:** Three coloured balls (green, blue, red) orbit your hip like toy planets, pinging enemies with soft *tick*s. On release: *pop... pop-pop... PHWACK* with rising pitch, the balls blur into one glowing droplet and land with a splash-shaped shockwave.
- **Scaling:** projectile damage, queue size, merge bonus per ball (+40%), projectile speed, crit, passive orbit damage.
- **Synergies:** The boss burst after Full Count's snap. Queue it while Hidden Ball Trick or Backstop buys time. Time Out cancels the release recovery.

## 9. Rain Delay
*Pair 9: hummingbird torpor x trading card game*
- **Tags:** Guard, Channel, Duration, Discover. Cooldown 20 s, up to 6 s.
- **Does:** The infield tarp falls over you. You are rooted and take 90% less damage while you rest, and you regain life and a Runner every 2 s. When you stand up (or at 6 s) you **Discover**: pick one of three random boons whose strength depends on **how long you rested**, not how deep.
- **Sources:**
  - *Paper:* Shankar, Schroeder, Wethington, Graham & Powers, "Hummingbird torpor in context: duration, more than temperature, is the key to nighttime energy savings", bioRxiv 2018 (the later *J. Exp. Biol.* version was not confirmed). Total energy saved depends most on how long the bout lasts, not how deep it is, then the bird wakes to feed.
  - *Game:* *Hearthstone*, Discover. You get three options and pick one, which makes the randomness feel like a decision.
  - *Baseball:* the rain delay, when the grounds crew pulls the tarp over the infield.
  - *Condensed:* The tarp is the torpor. Time spent sets the boon's quality (duration over depth). The waking is the Discover.
- **Animation and feel:** The tarp slumps over you with a heavy *fwomp* and rain patters on it. Your sleepy snore balloons bubble up. When you wake, a card fan of three boons flips up with a *shuff*.
- **Scaling:** duration (boon strength per second), damage reduction, regen, boon pool size ("see 4 choices"), cooldown recovery.
- **Boons (examples):** Fresh Arm (+attack speed), Pitcher's Duel (+crit), Sunflower Seeds (heal), Cleats (+movement speed), Rosin Grip (+Barrel window).
- **Synergies:** Cast right after Time Out or behind Backstop. Boons feed whichever build you play. Its splash is water (it un-sets Pine Tar).

## 10. Fungo
*Pair 10: Levy flight foraging x battle royale*
- **Tags:** Attack, Projectile, Area, Bounce. Basic ranged generator, no cost.
- **Does:** Toss and hit a ball with the long skinny fungo bat. It hops across the floor in a **Levy flight**: mostly short hops, with a rare long one that jumps to a new pack, and it **never lands where it has already landed**. Each landing marks a red circle that **shrinks like the Storm** and drags enemies in before it pops. A pop that catches 3 or more enemies gives +1 Runner (once per cast).
- **Sources:**
  - *Paper:* Humphries et al., "Environmental context explains Lévy and Brownian movement patterns of marine predators", *Nature* 465, 2010. Foragers use many short hops and rare long jumps in sparse places, and ordinary wandering in rich ones. This avoids re-covering ground.
  - *Game:* *Fortnite*, the Storm. A marked circle shrinks on a timer and punishes whoever stays outside.
  - *Baseball:* the fungo bat, which coaches use to hit fly balls scattered around the field for fielding practice.
  - *Condensed:* A fungo scatters balls to random spots, the Levy hop pattern. The shrinking circle is the Storm: its collapse pulls the pack in, so the next hop pop is on a pile.
- **Animation and feel:** A casual toss and a light *pock*. The ball squeaks on every bounce, and a chalk circle contracts with a vacuum-like *fwooo* before a dusty pop. A long hop gets a comic slide-whistle.
- **Scaling:** hops (chain count), area, extra balls (projectile count), projectile damage, **crit chance lengthens the long-hop odds**, attack speed.
- **Synergies:** Sets up Knuckleball and Hang Time on piled enemies. Time Out holds the distant seven in range. Ping Pad "in tune" tiles buff the ball as it hops through.

## 11. Tag Up
*Pair 11: slime mould network growth x puzzle platformer*
- **Tags:** Movement, Trail, Rewind. Cooldown 10 s.
- **Does:** As you move, you leave a glowing gel path of the last 4 s. Cast again to **rewind**: you race back along your own path at triple speed, damaging everything you cross, and restore the life you had at the start of that path (if higher). Spots the path crossed more than once have thickened into **tubes** that hit harder.
- **Sources:**
  - *Paper:* Tero, Takagi, Saigusa, Ito, Bebber, Fricker, Yumiki, Kobayashi & Nakagaki, "Rules for Biologically Inspired Adaptive Network Design", *Science* 327, 2010. A slime mould builds an efficient network by thickening tubes that carry more flow and letting unused ones vanish.
  - *Game:* *Braid*, time rewind. You can undo your actions, even a death, and the rule is simple.
  - *Baseball:* tagging up. After a fly ball is caught, the runner has to go back and touch the base he left.
  - *Condensed:* The rewind is the tag up, and the path is the slime network. Every crossing thickens it, so circling an enemy twice before rewinding is how you "grow" damage. The path fades if unused.
- **Animation and feel:** A grape-jelly trail glows behind you. On recast, the film runs backwards: tape-rewind sound, afterimages, crowd noise pitched down, and you slide home with an umpire's "SAFE!" pop-up.
- **Scaling:** path length and time (rewind window), rewind speed, tube damage per crossing, life restored, area of the trail. The speed carries into Chase the Fly.
- **Synergies:** Run a loop around the pack, then rewind through it. Pine Tar paths work as the tube's "food". Retreat and heal out of danger, then Chase the Fly back in.

## 12. Hang Time
*Pair 12: gravitational lensing x sandbox crafting game*
- **Tags:** Movement, Area, Airborne. Cooldown 8 s.
- **Does:** Leap into a high arc, with the distance set by where you point (far = long low glide, near = tall pop-up). While airborne, spend a Runner to light a **bottle rocket**: a fixed-speed push forward whose length grows with duration, not speed. You land with a slam that is **echoed in a cross of four lensed images**, 0.2 s apart.
- **Sources:**
  - *Paper:* Kelly et al., "Déjà Vu All Over Again: The Reappearance of Supernova Refsdal", *ApJ Letters* 819, 2016. One supernova seen as four images in an Einstein cross, with built-in time delays, and a fifth image predicted in advance.
  - *Game:* *Minecraft*, Elytra and firework rockets. You glide, steer by pitch, and a rocket boosts you at the same speed, with a longer burn for the better rocket.
  - *Baseball:* the pop fly's launch angle and hang time.
  - *Condensed:* The glide is the launch angle. The rocket is the Elytra boost. The four delayed copies of the landing are the lens. One jump, four hits on one place.
- **Animation and feel:** The slow-motion pop-up and the long hang-time pause, then a *fsssst* rocket trail with sparkler sparks. The landing marker appears in advance. Four ghost slams hit one after another with rising *boom-boom-boom-BOOM*.
- **Scaling:** area, damage per echo, **projectile count adds echoes**, rocket duration, cooldown recovery.
- **Synergies:** Land on a pile made by Fungo or Time Out. Cast it right after Tag Up for a speed chain. Backstop collapses under the echoes.

## 13. Knuckleball
*Pair 13: superfluid helium x pinball*
- **Tags:** Attack, Projectile, Area, Bounce. Spends 1 to 3 Runners (one ball each).
- **Does:** Throw a slow, spinless ball that flutters through the room. It never loses speed (zero friction) and ricochets off everything for 6 s. Each enemy it hits leaves a small whirl that tugs enemies in, and **you can nudge it** up to 3 times by tapping a direction. A fourth nudge is a **Tilt**: the ball drops dead.
- **Sources:**
  - *Paper:* Gomez, Bostedt et al., "Shapes and vorticities of superfluid helium nanodroplets", *Science*, 2014 (authors not confirmed in my search; cite from the SLAC release). Superfluid helium has no viscosity and spins as a lattice of many identical little vortices.
  - *Game:* real pinball. You can nudge the table, a tilt bob stops you after a few warnings, and locks lead to multiball.
  - *Baseball:* the knuckleball, thrown with almost no spin so it flutters unpredictably.
  - *Condensed:* The knuckler flutters because it has no spin. The zero-friction ball never slows. The little identical whirls are the vortex lattice. The pinball parts are the nudge, the tilt and multiball (3 Runners = 3 balls, three locks).
- **Animation and feel:** A one-handed push, then the ball wobbles with a funny *wub-wub* and zig-zags like a pinball. Each hit makes a tiny whirl with a rubbery bumper *bwing*. Nudges shake the screen slightly. A tilt flashes a big "TILT" and the ball *plops*.
- **Scaling:** projectile damage, duration, bounce count, whirl pull and area, number of balls, projectile speed.
- **Synergies:** The bouncing pack-clear for corridors and Backstop rooms. Pine Tar patches stop it dead (it sticks). Fungo piles are where the ball likes to bounce.

## 14. Ping Pad
*Pair 14: acoustic metamaterials x farming sim*
- **Tags:** Totem, Area, Duration. 3 charges, lasts 15 s.
- **Does:** Plant an aluminium bat cap on the chalk grid. It rings once a second over a **cross of 4 tiles** (3x3 at gem level 10, 5x5 at level 20). Enemy projectiles inside the ringing tiles are destroyed, and your own projectiles that pass through are **in tune** for +30% damage. Overlapping pads do not stack, so you tile them.
- **Sources:**
  - *Paper:* Fang, Xi, Xu, Ambati, Srituravanich, Sun & Zhang, "Ultrasonic metamaterials with negative modulus", *Nature Materials* 5, 2006. An array of tiny resonators acts as a new material that pushes sound back near its resonant frequency, so the structure sets the behaviour.
  - *Game:* *Stardew Valley*, sprinklers. They water a fixed pattern (4 tiles, 8, then 24) and you tile them for coverage.
  - *Baseball:* the aluminium bat's "ping" and the vibration-node sweet spot.
  - *Condensed:* The pad is the resonator. The field is the sprinkler grid. Place the pads so the patterns just touch and you cover the arena without waste.
- **Animation and feel:** A little tuning-fork hum, then a clear aluminium *PING*. Ringing tiles flash in a chequerboard of colour, projectiles *pffft* into confetti, and in-tune balls trail a musical note.
- **Scaling:** pad count, pattern size (gem level), duration, in-tune damage, ping rate.
- **Synergies:** Projectile builds love it (Fungo, Knuckleball, Three-Pitch Mix). It protects Backstop and Hidden Ball Trick areas.

## 15. Walk-Up Song
*Pair 15: origami engineering x rhythm game*
- **Tags:** Attack, Melee, Rhythm, Area. Basic attack, no cost, main generator.
- **Does:** A beat ring pulses at your feet. Swing **on the beat** (that is the Barrel window) to unfold your folding-paper bat one stage: **poke, wide sweep, giant fan smash**. Each on-beat swing adds 1 Groove (+10% damage, up to x2), and the Fold 3 smash gives +1 Runner. Swinging off-beat refolds the bat and resets Groove, but waiting out a beat is safe.
- **Sources:**
  - *Paper:* Filipov, Tachi & Paulino, "Origami tubes assembled into stiff, yet reconfigurable structures and metamaterials", *PNAS* 112, 2015 (authors and year recalled from memory; verify). Zipped Miura tubes are stiff yet deploy with one degree of freedom, so one motion unfolds the shape.
  - *Game:* *Crypt of the NecroDancer*. You act on the beat, a Groove Chain multiplier builds with every clean move, and a missed beat resets it.
  - *Baseball:* the batter's walk-up song and the stadium organ.
  - *Condensed:* The walk-up song is the beat. Each swing on the beat is one fold of the same motion, from a small poke to a big fan. Groove is the NecroDancer chain.
- **Animation and feel:** A tinny organ riff sets the beat, and the beat ring pulses gold. The bat clicks open with a *fwip-fwip* paper-fan sound at each fold. Fold 3 has a heavy 6-frame hit-stop and a paper-confetti burst. A miss gives a sad trombone *waa*.
- **Scaling:** attack speed (faster combo within the beat, not a wider window), crit, melee damage, area at Fold 3, Groove cap, added elemental damage.
- **Synergies:** Feeds every spender. Barrel hits shatter Set enemies. Time Out cancels recovery without breaking the chain.

## 16. Benches Clear
*Pair 16: ant colony foraging x tactics RPG. The ultimate.*
- **Tags:** Ultimate, Summon, Swarm, Cooldown (40 s, lasts 12 s).
- **Does:** The dugout doors fly open and **nine toy ants in a batting order** line up on a turn bar on your HUD. Each ant's charge bar fills with **your attack speed and the number of enemies hit nearby**, and when it is full the ant charges and bites, then rests for 2 s. More hits means more charging ants, which means more contacts, so the colony snowballs and settles when the fighting stops.
- **Sources:**
  - *Paper:* Pagliara, Gordon & Leonard, "Regulation of harvester ant foraging as a closed-loop excitable system", *PLoS Computational Biology*, 2018. Ants leave on a foraging trip when they have recently bumped antennae with returning foragers. There is a refractory period and no ant sees the whole picture.
  - *Game:* *Final Fantasy Tactics*, Charge Time. Every unit's CT bar fills by its Speed, a full bar can act, and the visible turn list lets you plan.
  - *Baseball:* the bench-clearing brawl.
  - *Condensed:* The whole bench runs out. Each ant is a unit with a CT bar. The ants' rule is the excitable loop (hits trigger more ants), and the rest period is the refractory time. Attack speed is literally Speed.
- **Animation and feel:** A whistle, a shuddering dugout and a stampede of ants in tiny cleats. The lineup bar on screen shows who is "up", and each charging ant gets a speed trail and a *rah!* A big finish shows a confetti "HOME TEAM WINS!".
- **Scaling:** attack speed (charge rate), minion damage, number of ants (9 can rise), contact radius, duration, minion life, cooldown recovery.
- **Synergies:** The payoff for any build that hits a lot. Walk-Up Song and Fungo pump the contact count. Backstop and Hidden Ball Trick hold the pack in place for the ants.

---

## Three example builds

**1. Metronome Slugger** (melee, crit, boss and clear)
- **Skills:** Walk-Up Song (main), Foul Tip, Time Out, Full Count, Chase the Fly, Benches Clear.
- **Scaling:** attack speed, crit, melee, Groove cap, movement speed.
- **Loop:** Chase the Fly into the pack, ride the beat to Fold 3, Foul Tip a big hit to Set the crowd and Barrel to shatter it. Time Out cancels recovery and reshapes the fight. On a boss, Full Count strips the armour, five hits from Walk-Up land the finisher, and Benches Clear closes it out.

**2. Pinball Bullpen** (projectile, area, pack clear)
- **Skills:** Fungo (main), Knuckleball, Three-Pitch Mix, Ping Pad x2, Hang Time, Backstop.
- **Scaling:** projectile damage and count, area, duration, crit (longer Fungo hops).
- **Loop:** Plant two Ping Pads over a corridor. Fungo drags the pack into piles and refills Runners. Knuckleball bounces off the Backstop net for the rest. Three-Pitch Mix queued during the clear becomes a boss drop, and Hang Time echoes land on whoever is left.

**3. Glass Cannon Trapper** (control, Set and shatter, defence)
- **Skills:** Pine Tar, Foul Tip, Hidden Ball Trick, Rain Delay, Tag Up, Walk-Up Song.
- **Scaling:** Set duration and damage taken, area, duration, barrier strength, deflect window.
- **Loop:** Drop Pine Tar and Hidden Ball Trick to lure the pack into the glass while you stand dry inside your shell. Barrel hits shatter the Set enemies in chain reactions. If it goes wrong, Tag Up runs home through the tubes you drew, and Rain Delay turns the quiet into a Discover boon. Keep sprinklers in mind, since water dissolves both your shell and their glass.
