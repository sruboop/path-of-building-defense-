# The Slugger, take 2: 16 bat skills built from 16 odd pairings

Every number is a starting point to playtest, not a balanced value.

**How the sources were checked.** Each pair got a web search for the paper and one for the game. I mark a source **[verified]** when the search results confirmed the finding, or **[partly verified]** when they confirmed the finding but not the exact citation. Details I added from memory are marked **[memory]**. The full list of gaps is in "Source notes" at the end.

## Core systems (kept small)

| System | Rule |
|---|---|
| **Runners** (0–3) | Kept from the old kit. Generators put runners on base, spenders drive them in for more power. Three is **Bases Loaded**. |
| **Barrel** (timing) | Kept. Every swing and every timed skill has a gold sweet-spot ring. Hit it for a guaranteed crit, a longer hit-stop and +1 Runner. The ring does not shrink with attack speed, so it stays learnable. |
| **Touches** (new, replaces the Count) | Each enemy remembers recent hits from you for 3 s. Skills read "touched once" and "touched twice". Only Tag Out and Pine Tar write to it, so the rule stays tiny. |

Tags: Attack, Melee, Strike, Projectile, AoE, Chain, Movement, Guard, Summon, Trap, Aura, Duration, Cooldown, Ultimate, plus the status tags **Slick** (wet), **Tarred**, **Jammed**, **Burn**.

**Role map**

| Role | Skills |
|---|---|
| Generators | 2 Tag Out, 1 Dead Hands, 3 Mine!, 11 Pine Tar |
| Spenders | 6 Pepper Flock, 12 Instant Replay, 13 Superball, 8 Spitball (optional spend) |
| Pack clear | 12, 13, 6, 7 Baselines, 5 Hidden Ball Trick |
| Single target | 8 Spitball, 2 Tag Out, 9 On Deck (setup) |
| Movement | 10 Steal Home, 4 Rain Delay |
| Defence | 1 Dead Hands, 3 Mine!, 14 Backstop Scarecrow, 15 Paper Fielders |
| Ultimate | 16 Rally Ants |

---

## 1. Dead Hands (a bunt that turns hard hits to stone)
- **Tags:** Attack, Melee, Guard, Cooldown (1.5 s). Spends nothing. Generator.
- **Does:** Square up and tap in the 0.25 s window as a hit lands. The harder the hit, the more it **jams**: a big hit freezes the attacker stiff for 2 s, and a weak hit just shoves you back. Your next swing at the frozen enemy is a **Riposte**, a guaranteed crit for 300% damage that gives +1 Runner.
- **Sources:**
  - *Paper:* "Impact-activated solidification of dense suspensions via dynamic jamming fronts", Waitukaitis & Jaeger, *Nature* 487, 2012 **[verified]**. Cornstarch-and-water (oobleck) is liquid when pressed gently, but a hard impact makes a solid column grow under the striker. It works through a front of jammed particles that spreads from the impact point. The harder you hit, the more solid it gets, and it can even bounce a bowling ball.
  - *Game:* **Dark Souls** parry and riposte **[verified]**. A shield or dagger parry staggers the enemy, and a light attack then triggers a high-damage riposte. The parry is risky: in DS3 community frame data it is about 8 frames to start, 8 active and 30 recovery. Whiff it and you are punished.
  - *Baseball:* the dead-ball bunt, where you absorb the ball's energy with soft hands.
- **Condensed:** Souls gives the risky timed parry and the riposte. Oobleck gives the twist: the parry's reward depends on how hard the hit is, so you want to catch the boss's biggest blow, not chip damage. The bunt gives the stance and the soft-hands look.
- **Feel:** The bat goes loose and limp. A big hit lands with a soft *thup* as the attacker freezes mid-lunge, coated in a cornstarch-white crust that cracks. Hit-stop is tiny on the parry and large on the Riposte (8 frames), with a dust burst and the *CRACK*. Weak hits make a wobbly jelly ripple.
- **Scaling:** window size, Riposte damage and crit multiplier, freeze duration, parry-to-stagger conversion, cooldown recovery. Tags: Melee, Guard, Crit.
- **Synergies:** frozen enemies are safe targets for Instant Replay and Tag Out. Boss builds use it on the slam, then spend the Runner on Pepper Flock.

## 2. Tag Out (the two-touch trap)
- **Tags:** Attack, Melee, Strike, Touches. Generator, basic skill, no cost.
- **Does:** A quick jab-tag with the bat's end. Hit an enemy twice within 3 s and the second touch **snaps shut**: bonus damage, a 1 s root, and +1 Runner. The fifth touch **digests** it: the enemy drops **Orange Slices**, small heal orbs. Two slices picked up within 2 s merge into a **Sports Drink**, a bigger heal.
- **Sources:**
  - *Paper:* "Calcium dynamics during trap closure visualized in transgenic Venus flytrap", Suda, Hasebe, Hedrich et al., *Nature Plants*, 2020 **[partly verified: found via press releases; author list from memory]**. A touch on a sensory hair makes an action potential and a calcium wave. The trap only closes when a second touch comes in time to push the calcium past a threshold. The plant keeps counting, and from the fifth touch it makes digestive enzymes.
  - *Game:* **Resident Evil** herb mixing **[verified]**. Green herbs heal, and mixing green with red or a second green makes a stronger heal. Healing is a small puzzle about combining pickups.
  - *Baseball:* a tag out, where you touch the runner with the ball.
- **Condensed:** The flytrap's count (two to snap, five to eat) becomes the combo. The herb mix becomes the two slices merging into a sports drink, and a little-league orange slice is the toy-world herb.
- **Feel:** a snappy *tick-tick* jab. A tiny flytrap-jaw outline flashes at the target on the first touch. The second touch makes a loud *SNAP* and a green-and-red mouth closes on the enemy for a short hit-stop. The fifth touch makes a gulp, a burp and orange slices that bounce out.
- **Scaling:** attack speed, touch window, snap damage, root time, healing from slices, melee/physical damage.
- **Synergies:** snap Runners feed every spender. Orange slices make a self-heal loop that rewards staying in melee. Pine Tar's touches count here too.

## 3. Mine! (the call that jams the swing)
- **Tags:** Attack, Guard, AoE (ring), Jammed, Cooldown (6 s). Generator.
- **Does:** Shout "MINE!". A sonar ring spreads out. Any enemy in the final 0.3 s of a wind-up or shot is **Jammed**: the attack misses wildly, any projectile in flight turns around at the same speed and strikes the nearest enemy, and you gain +1 Runner per Jammed enemy. Shouting too early or late does nothing.
- **Sources:**
  - *Paper:* "Bats jamming bats: Food competition through sonar interference", Corcoran & Conner, *Science*, 2014 **[verified]**. Mexican free-tailed bats make a special "sinFM" call that is **timed to overlap a rival's feeding buzz**, the last fast pings before capture. Played at that moment the call makes the rival miss much more often. The same noise played earlier or later does nothing.
  - *Game:* **Portal** momentum **[verified]**. "Speedy thing goes in, speedy thing comes out": an object keeps its speed and direction through a portal. The rule makes a sling puzzle.
  - *Baseball:* the outfielder's call-off ("I got it! Mine!") that stops two fielders colliding.
- **Condensed:** The bat paper gives the timing rule: interrupt at the final moment and not before. Portal gives the payoff: a projectile comes out the other side at full speed. The call-off is what the player does. The result is one short-range reflect that rewards reading tells.
- **Feel:** you cup a hand to your mouth, there is a clear *MIIINE!*, and a thin blue sonar ring. Jammed enemies' eyes spiral and their projectiles flip with a *boing* and a white speed streak. A "CALLED OFF" pop-up. Almost no hit-stop. The ring flashes gold if you hit the Barrel.
- **Scaling:** ring radius, window length, reflected-damage multiplier, cooldown recovery, Runner gain. Tags: Guard, AoE, Projectile.
- **Synergies:** reflected shots can pass through a Superball or a Baseline string for double hits. It gives Runners against ranged packs, which Dead Hands (a melee answer) does not.

## 4. Rain Delay (the tarp blink)
- **Tags:** Movement, Guard, Duration (up to 2.5 s), Cooldown (10 s, 2 charges).
- **Does:** Aim a marker up to 14 m away (it can reach up onto ledges). Pull a tarp over yourself and become a dry, sealed **tun**: invulnerable and immobile, soaking the damage you take. When you release, or after 2.5 s, you **Blink** to the marker and splash for all the damage you soaked.
- **Sources:**
  - *Paper:* "Tardigrades use intrinsically disordered proteins to survive desiccation", Boothby et al., *Molecular Cell*, 2017 **[partly verified: search found the UNC team's TDP proteins that form a glass-like solid on drying, and the title is from memory]**. Tardigrades dry out into a "tun" and survive, because their cells fill with glassy protein instead of crystals.
  - *Game:* **Dishonored** Blink **[verified]**. Hold the button to show a landing marker, move about 10–15 m almost instantly, climb ledges automatically, and in later upgrades throw enemies down at the end (Blink Assault).
  - *Baseball:* the rain delay and the infield tarp.
- **Condensed:** Blink is the movement. The tardigrade makes the "inert and unbreakable" middle step, which turns a plain teleport into a dodge-and-return that pays for hits you stood still for. The tarp is the object.
- **Feel:** a flapping *whump* as the tarp drops, the marker pulses, and a hard rain-on-plastic sound plays while you take hits (each hit adds a bright number). On release the tarp snaps up, you vanish in a spray, and a water burst *SPLASH* appears at the marker.
- **Scaling:** range, charges, soak cap, splash conversion, cooldown recovery. Tags: Movement, Guard, AoE.
- **Synergies:** stand in a boss's slam, then splash back for the same damage. Pairs with Mine! (soak, then jam). Landing on Pine Tar refreshes a charge.

## 5. Hidden Ball Trick (the walking box)
- **Tags:** Summon, Duration (6 s), Cooldown (12 s), AoE.
- **Does:** Drop five cardboard decoy boxes in the pattern of a **glider**, with a toy ball hidden under one. Every beat the whole shape crawls one step diagonally, and enemies follow it in a conga line. When the glider expires each box pops for damage. If you pop out of the box with the ball, your next hit is a guaranteed crit.
- **Sources:**
  - *Paper:* Conway's Game of Life, with Gosper's glider gun, **Gardner's *Scientific American* column, 1970** **[partly verified: search confirmed the glider gun and that Conway tuned his rules so patterns neither explode nor die; exact year and column from memory]**. Three or four simple neighbour rules give a five-cell shape that walks across the grid forever.
  - *Game:* **Metal Gear Solid V** cardboard box **[verified]**. Hide in it, pop out to take an enemy, and leave it as a decoy to pull attention.
  - *Baseball:* the hidden ball trick, where a fielder hides the ball and tags out a runner who steps off the base.
- **Condensed:** MGSV gives the decoy and the pop-out. Life gives the thing that makes it funny and clever: the decoy shape *moves itself* in a way you can predict, so you can walk the pack through a hazard like walking a drone.
- **Feel:** cartoon box *thumps* and slides, shuffling in a staggered diagonal rhythm (tick, tick, step). The boxes glow green in the glider shape. Popping makes confetti, a "!" over enemies' heads, and a squeaky *tada*.
- **Scaling:** duration, box count, pop damage, area, pull strength. Tags: Summon, AoE, Duration.
- **Synergies:** walk the conga line into Baselines or a sprinkler. Pepper Flock chooses its nearest targets, which clumped enemies make easy. Instant Replay loves a tight clump.

## 6. Pepper Flock (the swarm that never loses its neighbours)
- **Tags:** Attack, Projectile, Chain-like (homing). Spender (1 Runner for 7 balls, each extra Runner +3).
- **Does:** Flick seven balls out of a "pepper" warm-up. Each ball steers to its **nearest enemy** and never aims at a fixed spot, so it cannot lose a target as the pack scatters. It can be cast **in the recovery of any melee hit**, cancelling it.
- **Sources:**
  - *Paper:* "Interaction ruling animal collective behavior depends on topological rather than metric distance: evidence from a field study", Ballerini et al., *PNAS*, 2008 **[partly verified: the finding is confirmed, the title and journal are from memory]**. Starling flocks in Rome were reconstructed in 3D, and each bird tracks about **six to seven nearest neighbours**, not all birds within a set distance. This keeps the flock together when density changes.
  - *Game:* **Street Fighter 6** Drive Rush **[verified]**. A cancel lets you skip recovery after a landed normal move (at a cost) to keep your combo going.
  - *Baseball:* pepper, the quick warm-up game of short hits and fast fields.
- **Condensed:** The flock rule gives each ball a "count, don't measure" targeting rule that is easy to see. The fighting-game cancel is the glue, so hitting then flicking feels like a combo.
- **Feel:** a tight wrist-flick, seven white balls bursting out like a bird cloud with a *whirr*, and a murmur of tiny *tik-tik-tik*. Each ball turns sharply in the air. A soft ping per hit, a bigger stop when the last one lands.
- **Scaling:** ball count, projectile damage, homing strength, extra projectiles, crit. Tags: Projectile, Attack.
- **Synergies:** best after Tag Out (the cancel) or Hidden Ball Trick (the clump). Supports "Fastball" and "Slider" change how the flock moves.

## 7. Baselines (the tensioned diamond)
- **Tags:** Trap, AoE, Duration (8 s), Cooldown (10 s), 2 charges.
- **Does:** Plant Home Plate at your feet, then up to three bases within 8 m. Taut string lines join them. Enemies who cross a string are cut and slowed, and **hitting any base plucks the whole net**: every string zaps at once.
- **Sources:**
  - *Paper:* "Tensegrity: the architectural basis of cellular mechanotransduction", Ingber, *Annual Review of Physiology* 59, 1997 **[verified]**. A cell holds its shape with a steady pre-tension in a network, with a few rigid struts. A tug at one point spreads through the whole network, so a pull at the cell's edge reaches the nucleus.
  - *Game:* **Frostpunk** generator and Steam Hubs **[verified]**. A powered network spreads heat zones from a generator through hubs. Overlapping zones do not stack, so you should spread them.
  - *Baseball:* the base paths and the diamond itself.
- **Condensed:** Tensegrity gives the pluck: one hit moves through the whole shape. Frostpunk gives the placement puzzle: a network from one source where bunching is wasteful. The diamond is the shape players already know.
- **Feel:** a rubber-band *twang* as each base lands and the string snaps tight. Strings hum and glow when enemies touch them, and one swing on a base sends a bright pulse round the diamond with a *DOINNNG*.
- **Scaling:** string damage, slow, number of bases, area, pluck damage. Tags: Trap, AoE, Duration.
- **Synergies:** Hidden Ball Trick walks enemies in. Runners standing on a base add +10% each to string damage.

## 8. Spitball (the seed that arrives all at once)
- **Tags:** Attack, Projectile, Slick, Cooldown (1 s). Optional spend of 1 Runner for double.
- **Does:** Hold to aim and release a stream of sunflower-seed spit that **merges into one hard slug exactly where you point**, so damage rises with distance. It makes the target **Slick** (wet). Cast it again on the same Slick enemy and the Slick **doubles**.
- **Sources:**
  - *Paper:* "Small circuits for large tasks: high-speed decision-making in archerfish", Schlegel & Schuster, *Science* 319, 2008 **[verified]**, together with Schuster's spitting-jet work **[partly verified via press: the fish change mouth opening so the jet's tail catches up and forms a bullet-like blob at the target; a longer opening for greater distance]**. Archerfish pick the landing point of falling prey from its first moves and start swimming within about 40–100 ms.
  - *Game:* **Slay the Spire** Catalyst **[verified]**. It doubles (triples if upgraded) a poison value already on an enemy, and the deck exists to stack and then multiply it.
  - *Baseball:* the spitball, and the dugout sunflower-seed spit.
- **Condensed:** the fish gives the hold-and-aim rule (a sharpshooter whose punch arrives at the target), and the card gives the second cast, which turns a status into a payoff.
- **Feel:** a cheeky *ptoo*, a thin seed-spray that narrows to a pellet mid-air, then a wet *SPLAT* and tiny stop. The second cast brings a gurgle and the Slick glistens and swells.
- **Scaling:** range, damage per metre, Slick duration, doubling multiplier, crit. Tags: Projectile, Slick.
- **Synergies:** Slick conducts: lightning and cold hit harder on it. Superball home-in on burning or Slick targets. It is the long-range tool for bosses.

## 9. On Deck (the pinch-hitter nap)
- **Tags:** Utility, Duration, Cooldown (8 s). Costs no Runners.
- **Does:** Press, then press any other skill: it goes **on deck** instead of firing. Its Runner cost drops to zero, and after up to 4 s it fires on its own at your cursor. The longer it waited, the stronger: +20% damage per second.
- **Sources:**
  - *Paper:* "Hummingbird torpor in context: duration, more than temperature, is the key to nighttime energy savings", Shankar, Graham, Powers et al. (2020) **[partly verified: the bioRxiv preprint was found; journal and author list from memory]**. In a field study of 43 wild hummingbirds, torpor saved 65–92% of energy per hour, and **how long each bout lasted** mattered more than how cold it was.
  - *Game:* **Magic: The Gathering** Suspend **[verified]**. Pay a small cost now and exile a card with time counters. One counter comes off each upkeep, and when the last one goes the card is cast free.
  - *Baseball:* the on-deck circle and the pinch hitter.
- **Condensed:** Suspend gives the mechanic exactly. The hummingbird gives the reason to wait: a longer rest saves more, so patience is rewarded linearly.
- **Feel:** the batter on deck takes practice swings and a counter spins above your head like a pitch-clock. A tiny hummingbird sits on it. When it fires you hear the PA announcer: "NOW BATTING!".
- **Scaling:** wait time cap, bonus per second, number of skills queued, cooldown recovery. Tags: Duration, Utility.
- **Synergies:** queue Instant Replay or Rally Ants before a boss phase starts. A skill you queue is still a Barrel if it lands on the gold ring.

## 10. Steal Home (the Lévy hop)
- **Tags:** Movement, Attack, Slide, Cooldown (3 charges).
- **Does:** Slide in a direction. The length is a roll: **most hops are short (3 m), some medium (6 m) and rarely very long (14 m)**. The next hop's length is shown on the HUD ahead of time. The fewer enemies close by, the likelier a long hop. You are invulnerable while sliding, and enemies you slide through take damage that grows with the hop's length.
- **Sources:**
  - *Paper:* "Environmental context explains Lévy and Brownian movement patterns of marine predators", Humphries, Queiroz, Dyer … Sims, *Nature* 465, 2010 **[verified]**. Tracking data from 14 species of sharks, tuna and other ocean predators showed Lévy movement (many short moves, rare very long ones) in poor waters with sparse prey, and Brownian (steady) movement where prey is plentiful.
  - *Game:* **Apex Legends** Wraith, Into the Void **[verified]**. 4 s of invulnerability and +30% speed, a 1.25 s windup, a 25 s cooldown, and a visible blue trail. Guides say to use it before you are nearly dead.
  - *Baseball:* stealing a base, and the lead-off.
- **Condensed:** the predator rule makes the dash itself read the room: busy room, careful short hops; empty room, big jumps. Wraith gives the phase-through-danger purpose. Stealing home is the dream jump.
- **Feel:** a crouched lead-off, a dust *shhhk*, a slide with a streak. The long hop gets a loud umpire "SAFE!" pop-up and a shockwave of dust. Short hops are fast and snappy.
- **Scaling:** charges, hop lengths, long-hop odds, damage per metre, move speed. Tags: Movement, Attack.
- **Synergies:** a slide through a wind-up is a Barrel. The long hop can reach Baselines or Pine Tar quickly.

## 11. Pine Tar (the trail that finds the best route)
- **Tags:** Trap, Tarred, Duration (10 s), Cooldown (8 s). Generator (1 Runner when 3 enemies are stuck).
- **Does:** Fling three globs of pine tar. Tar lines connect them. Enemies who walk a line become **Tarred** (slowed, and they count as touched). Every time something crosses a line it **thickens**: more slow, more damage. Lines nobody walks on **thin and vanish**.
- **Sources:**
  - *Paper:* "Rules for biologically inspired adaptive network design", Tero et al., *Science* 327, 2010 **[verified]**. Slime mould (*Physarum*) joined food sources in a pattern close to the Tokyo rail network. Tubes carrying the most flow get wider, and unused tubes shrink and disappear.
  - *Game:* **Celeste** dash **[verified]**. The dash is limited, shown by hair colour, and is refilled mainly by touching ground and by crystals.
  - *Baseball:* the Pine Tar Incident of 1983, where pine tar on a bat is allowed only up to 18 inches.
- **Condensed:** the slime paper makes the tar *learn*, and puts the best damage where the pack really goes. Celeste's refill makes it a little puzzle for the player: touch your own tar to refresh a Steal Home charge.
- **Feel:** a sticky *splorp*, black-gold strings that stretch, and a gurgling squelch under enemies' feet. Thick lines glow amber and pulse.
- **Scaling:** duration, slow, thickening rate, damage, area. Tags: Trap, Duration, AoE.
- **Synergies:** dash charge refund works with Steal Home. Tarred enemies are easy Tag Out snaps, and they catch fire from a Superball.

## 12. Instant Replay (the Einstein cross)
- **Tags:** Attack, AoE, Chain, Cooldown (5 s). Spender (1 Runner).
- **Does:** Your last Barrel hit is **replayed** at the biggest enemy clump from four directions, as delayed ghosts at +0.4, +1.0, +1.6 and +2.4 s, each for 60% of the original. A replay that kills sets off a new replay on the nearest enemy.
- **Sources:**
  - *Paper:* "Multiple images of a highly magnified supernova formed by an early-type cluster galaxy lens", Kelly et al., *Science* 347, 2015 **[verified]**. A heavy cluster bends light so one exploding star shows up in **four images** around a galaxy in a cross, arriving at different times. The team predicted the star would reappear, and it did in December 2015 (SN Refsdal).
  - *Game:* **Minecraft** Observer **[verified]**. A block that watches for a change in the block in front of it and sends a one-tick pulse. The pulse starts the next thing in a chain.
  - *Baseball:* instant replay and video review.
- **Condensed:** gravity splits one event into four, delayed copies. The Observer makes a replay start another when it sees a change (a kill). Video review is what the player pictures.
- **Feel:** a slow-motion *rewind* whoosh, a TV-screen scan-line over the target and four ghost bats in a cross. Each replay is a little quieter and greyer. "REVIEW COMPLETE" pops up with a buzzer.
- **Scaling:** replay count, delay, replay damage percent, chain count, crit. Tags: AoE, Chain.
- **Synergies:** needs a Barrel, so Dead Hands' Riposte and Tag Out snaps feed it. Runs well after Hidden Ball Trick or Pine Tar drags the pack together.

## 13. Superball (the ball that never slows)
- **Tags:** Attack, Projectile, Bounce, Duration (6 s). Spender (1 Runner).
- **Does:** Smash a rubber superball that **never loses speed**, bounces off everything and climbs over low walls and furniture. It steers toward the **hottest** enemy (burning or shocked). Every third bounce splits off another ball (max 3), and a Barrel hit on it mid-flight is a **skill shot** that doubles its damage.
- **Sources:**
  - *Paper:* Allen & Jones, "New phenomena connected with heat flow in helium II", *Nature*, 1938 **[verified for the fountain effect, with Rollin and Allen–Misener film climbing from memory]**. Superfluid helium has no viscosity. If you heat one end of a plug, the fluid flows *toward the heat* and shoots up as a fountain, the opposite of what a normal liquid does. The same fluid also creeps up and over the walls of its container as a thin film.
  - *Game:* **Pinball** multiball and skill shot **[verified]**. You lock balls, then release several at once, and a perfect plunger pull at the start gets a bonus.
  - *Baseball:* the foul ball and the wall-ball.
- **Condensed:** the fluid gives the ball three strange properties (no energy loss, climbs walls, flows to heat). Pinball gives the multiball and the skill shot. A Super Ball is also a real toy.
- **Feel:** a bright *pa-DOINK* as it leaves the bat and a rainbow streak, then pinball bells and ratchet sounds on each bump. A bumper-style number pops up and the score ticks.
- **Scaling:** bounce count, duration, damage per bounce, split count, heat homing. Tags: Projectile, Bounce, Burn.
- **Synergies:** burning enemies attract it. It works in toy-block rooms. Worm-Burner-style corridors become pinball tables.

## 14. Backstop Scarecrow (the net that lets you through)
- **Tags:** Summon, Guard, Duration (10 s), Cooldown (14 s), AoE.
- **Does:** Plant a scarecrow in a catcher's mask. It **cancels every enemy projectile** within 8 m, but your own shots, allies and enemies walk straight through it. Each cancelled shot is **planted** and grows into a **ball** in 5 s, which you can pick up as a heal or a Runner.
- **Sources:**
  - *Paper:* "Ultra-open acoustic metamaterial silencer based on destructive interference", Ghaffarivardavagh, Nikolajczyk, Anderson & Zhang, *Physical Review B* 99, 2019 **[partly verified: found via press; title from memory]**. A 3D-printed silencer with a big open hole cancelled about 94% of sound while keeping 60% of the opening open, using six helical channels that make a wave to cancel the incoming one.
  - *Game:* **Stardew Valley** scarecrows and sprinklers **[verified]**. A scarecrow protects the crops around it from crows (sources differ on the exact tile range), and sprinklers water a fixed number of neighbour tiles every morning. Crops then grow while you do other things.
  - *Baseball:* the backstop netting, which stops balls and still lets fans see.
- **Condensed:** the metamaterial gives "block this, pass that". The farm gives "what you stop becomes a crop". The netting is what the player sees.
- **Feel:** a soft *fwump* as the net catches a shot, and a seed-sprout *pop*. Little plants wiggle up where bullets died and ripen with a ding. The scarecrow tips its head.
- **Scaling:** radius, duration, growth speed, heal per ball, number of scarecrows. Tags: Summon, Guard, Duration.
- **Synergies:** best with Mine!, which turns shots round, and Pepper Flock, which spends the Runners the balls give. It is the support skill for co-op.

## 15. Paper Fielders (the Miura wall)
- **Tags:** Summon, Guard, Duration (8 s), Cooldown (12 s), Beat.
- **Does:** Unfold a wall of five origami fielders. Each panel is **bistable**: flat (you pass through) or folded (a solid wall that bounces enemies). Hit a folded panel in the Barrel ring and it pops through and launches nearby enemies. Each panel popped on the beat adds **Fury**, making the whole wall tougher and its pops stronger.
- **Sources:**
  - *Paper:* "Using origami design principles to fold reprogrammable mechanical metamaterials", Silverberg, Evans, McLeod, Hayward, Hull, Santangelo & Cohen, *Science* 345, 2014 **[verified]**. Each cell of a Miura-ori fold is bistable. Flipping cells changes how stiff the whole sheet is, and a neighbouring flip of the opposite sense can cancel the first (like a missing atom in a crystal).
  - *Game:* **Metal: Hellsinger** Fury **[verified]**. Acting on the beat builds a 1–16× multiplier and a Perfect gives more. The music grows with the multiplier, and it is lost if you take damage or go off-beat.
  - *Baseball:* the infield shift and the shape of a baseball diamond's fold-out chart.
- **Condensed:** the paper provides the bistable flip and the sum of flips. Hellsinger provides the rhythm and the growing reward. The shift gives the scene.
- **Feel:** crisp paper *fffft* unfolding, a stage of fielders in white origami. A beat metronome ring appears and each on-beat pop gets a snare hit; the music adds a layer for each Fury level.
- **Scaling:** panel count, pop damage, wall life, Fury cap, knock-up height. Tags: Summon, Guard, Beat.
- **Synergies:** panels hold packs for Instant Replay. Baselines strings can be run along the wall.

## 16. Rally Ants (the ultimate)
- **Tags:** Summon, AoE, Ultimate, Cooldown (35 s). Needs Bases Loaded.
- **Does:** Drop a Cracker Jack box. Ant trails run from four sides. Ants choose paths with more scent, and each ant that bites an enemy adds scent, so **the colony snowballs onto the best target** and damage per ant rises. Different buffs you have running ("rallies") are carried by the ants, and the same buff never stacks twice.
- **Sources:**
  - *Paper:* Deneubourg, Aron, Goss & Pasteels, "The self-organizing exploratory pattern of the Argentine ant", *Journal of Insect Behavior* 3, 1990 **[partly verified: the double-bridge experiment and model are confirmed through Perna et al. 2012 in *PLoS Computational Biology*; the 1990 title is from memory]**. In a bridge with two branches to food, Argentine ants end up on the better branch, because ants prefer the branch with more pheromone, which in turn makes more ants choose it.
  - *Game:* **Fire Emblem** Rally **[verified]**. A unit's Rally command buffs allies within a few tiles and ends its turn. Rally skills do not stack with themselves, but different ones do.
  - *Baseball:* the late-inning rally, with rally caps and the stadium wave.
- **Condensed:** the ant model makes the damage focus itself. Fire Emblem's rule gives clear, readable buff stacking. The rally is the baseball spirit that pushes it all.
- **Feel:** a *crinkle* of the box, a rush of tiny feet and a rising stadium chant. Trails glow orange and thicken as ants gather. The final hit gets a crowd roar and "RALLY!" in lights.
- **Scaling:** ant count, scent growth, duration, number of distinct buffs, damage per ant, cooldown recovery. Tags: Summon, AoE, Ultimate.
- **Synergies:** it carries your On Deck, Dead Hands and Pine Tar buffs. A tarred, Slick pack makes the colony choose targets faster.

---

## Example builds

**1. The Counter-Puncher (melee boss killer)**
- *Skills:* Tag Out (main), Dead Hands, Mine!, Spitball, Instant Replay, Rally Ants.
- *Scaling:* crit, melee damage, window size, cooldown recovery.
- *Loop:* parry the boss's big blow with Dead Hands, Riposte for a Barrel, replay it four times, finish with Rally Ants while Spitball keeps Slick doubling on the boss.

**2. The Pinball Wizard (projectile pack clear)**
- *Skills:* Pepper Flock, Superball, Hidden Ball Trick, Pine Tar, Backstop Scarecrow, Steal Home.
- *Scaling:* projectile damage, bounce, burn, homing.
- *Loop:* a glider of boxes pulls the pack into tar, Superball bounces and splits among the burning enemies, Pepper Flock mops up, and the scarecrow turns enemy shots into heals.

**3. The Field Marshal (area and control)**
- *Skills:* Baselines, Paper Fielders, Rain Delay, On Deck, Instant Replay, Rally Ants.
- *Scaling:* area, duration, trap damage, cooldown recovery.
- *Loop:* trap the pack in a Baselines diamond with the paper wall, queue Instant Replay on deck, hide under a Rain Delay tarp for the boss's slam, then splash out and cash in Rally Ants.

---

## Source notes (what I did and did not confirm)

- **Confirmed by search results:** Waitukaitis & Jaeger 2012 (Nature 487); Humphries et al. 2010 (Nature 465); Kelly et al. 2015 (Science 347); Silverberg et al. 2014 (Science 345); Tero et al. 2010 (Science 327); Ingber 1997 (Ann Rev Physiol 59, DOI seen); Schlegel & Schuster 2008 (Science 319); Corcoran & Conner 2014 (Science, jamming during the feeding buzz); the Hedrich-group flytrap counting result (press); Ghaffarivardavagh et al. 2019 (Phys Rev B 99, via press).
- **Confirmed in substance but citation partly from memory:** the starling topological-interaction paper (Ballerini et al. 2008, PNAS), the tardigrade glass-protein work (Boothby et al. 2017), the hummingbird torpor study (Shankar et al.), the Argentine-ant bridge paper (Deneubourg et al. 1990), the Venus flytrap author list, and the 1938 helium papers (the search confirmed the fountain effect, not the film).
- **Weaker links:** the Game of Life item rests on secondary pages. The search did not return Silverberg-style numbers beyond the abstract. Superfluid film climbing and Life's glider shape are known physics and maths but were not in the results.
- **Games confirmed:** Dark Souls (parry frame data from fan wikis, approximate), Resident Evil (herbs), Portal (momentum), Dishonored (Blink), Metal Gear Solid V (box), Street Fighter 6 (Drive Rush), Frostpunk (heat network), Slay the Spire (Catalyst), MTG (Suspend), Apex (Into the Void), Celeste (dash refill), Minecraft (Observer), Pinball FX (locks, multiball, skill shot), Stardew Valley (scarecrow, sprinklers), Metal: Hellsinger (Fury), Fire Emblem (Rally).
- **Not usable from the searches:** Hi-Fi Rush, Crypt of the NecroDancer, XCOM and FFT results, Braid and Super Meat Boy, Octane, so I did not use them.
