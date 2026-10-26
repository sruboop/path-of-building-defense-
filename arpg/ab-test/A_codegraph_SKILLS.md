# SKILLS.md — The Batter: 16 skills

Class fantasy: a toy-sized little-leaguer with a bat, fighting through giant backyards, bedrooms and garages. Every skill is one baseball idea you can read at a glance.

Design basis (from the codegraph notes): sweet spot ≈ 2in zone, ~6in from the barrel end → hit-quality tiers; launch angle (ground ball <10°, line drive 10–25°, fly/HR 20–30°, pop-up >50°); Statcast "barrel"; Magnus pitch shapes; infield fly / squeeze / double play / tag up / pickoff / rundown rules; D4 generator–spender loop; PoE2 tags, support gems, Primed→Stun combos, Culling Strike; hit-stop 0.1–0.2s + sound + camera as the three feel pillars; It Takes Two "apply + detonate" pairs and giant-scale props.

## Core systems (shared by all skills)

- **Runners (0–3).** A diamond HUD (1st/2nd/3rd base) is the class resource. Generators put runners on base; spenders "drive them in" for extra damage per runner. Three runners = **Bases Loaded**: a visible max-pressure state that some skills reward.
- **Barrel timing.** Every Strike has a sweet-spot window late in the swing. Hit it → **Barrel**: crit-weighted, longest hit-stop, loudest crack, and generators give +1 Runner. Early = **pull** (knockback skews left), late = **opposite field** (skews right), mistimed = **jammed** (weak, short stop). Attack speed shrinks the swing but not the window, so it stays learnable.
- **Launch angle.** Hit height decides the enemy's fate: *ground* (rolls/slides), *line* (flat push), *fly* (airborne). Airborne is a status that other skills read.
- **Primed** (PoE2 Stun-style): enemies reach Primed by taking buildup. Primed targets take the payoff from a different skill.
- **Tags.** Attack, Melee, Strike, Projectile, AoE, Chain, Travel, Guard, Summon, Aura, Duration, Cooldown, Ultimate, plus the physical/toy damage base.

---

## 1. Leadoff Swing
- **Type / tags:** Attack, Melee, Strike, Basic, **Generator**.
- **What it does:** A fast two-hit combo (backhand, forehand) in a short frontal arc. Barrel hits add +1 Runner (max 3). No cost, always available.
- **Baseball source:** The leadoff hitter's job is to get on base and set up the lineup.
- **Animation / feel:** Quick stance, small load (hands back), snappy hip-then-torso rotation. Normal hits get a 0.05s stop and a wooden *tock*. A Barrel gets ~0.12s of freeze, a bright *CRACK*, a small camera punch and a gold ring flash on the target. The Runner pops onto the diamond with a little cap-tip sound.
- **Scaling:** Attack speed (more swings, more chances at Barrel), crit chance and multiplier (Barrel is crit-weighted), melee/physical damage, "chance to gain an extra Runner".
- **Grows into a build:** The best bread-and-butter generator for melee builds. Added fire/shock or toy-element damage makes it a legitimate main skill. At high attack speed it becomes a Runner machine.
- **Synergies:** Feeds every spender (Line Drive, Worm Burner, Grand Slam). Primes with Squeeze Play. Check Swing cancels its recovery.

## 2. Bunt
- **Type / tags:** Attack, Melee, Guard, Projectile-interact, **Generator**, short cooldown (0.6s).
- **What it does:** Hold the bat out. A short cone that deadens projectiles and small enemies (drops them at your feet, no damage to you) and shoves enemies away with low knockback. A deadened projectile or a hit enemy gives +1 Runner. A perfect-timed Bunt is a "Sacrifice": deadened projectiles become a dropped ball you can kick or hit.
- **Baseball source:** Sacrifice bunt / drag bunt. Give up the swing to move the runner over.
- **Animation / feel:** The batter squares up, slides a hand up the barrel and the bat goes still. Impact is a soft *thup* with tiny hit-stop, and the ball plops and rolls with a squash and stretch bounce. Comic touch: a sprinkler spray or marble just dribbles away.
- **Scaling:** Block/guard chance, "deaden" radius and cone width, Runner gain, cooldown recovery. Tags: Guard, Attack.
- **Grows into a build:** A defensive-generator package for tank or evasion hybrids. It turns enemy ranged attacks into free resource. Tied to the "perfect game" idea, no-damage windows buff damage.
- **Synergies:** Dropped balls feed Worm Burner and Pitching Machine. Check Swing is the offensive version of the same stillness. Diving Catch covers fast projectiles that Bunt can't.

## 3. Line Drive
- **Type / tags:** Attack, Melee, Strike, Projectile, Pierce, **Spender** (spends up to 1 Runner).
- **What it does:** Hit a ball out of the air in front of you. It fires as a flat, fast, piercing projectile (a "frozen rope") along a line, hitting everything in its path. Each Runner spent adds pierce count and damage. It gets +damage vs the first enemy hit.
- **Baseball source:** Line drive, 10–25° launch angle; four-seam fastball as the flat, fast shape.
- **Animation / feel:** A short pull-and-snap swing. The ball appears on the sweet spot of the bat, flashes white on contact and is replaced by a horizontal streak with a thin vapour line. On each pierce it makes a snappy *ting*, a small hit-stop per target and a tiny speed ramp. Final target gets a loud *thwack*. Sound pitch rises with exit velocity.
- **Scaling:** Projectile damage and speed, pierce count, crit, attack speed. "Exit velocity" (projectile speed) scales damage.
- **Grows into a build:** A reliable single-line clear and boss damage skill. Add Chain or Fork supports for packs. Heavy Barrel/crit investment makes it a screen-wide laser.
- **Synergies:** Spends Runners from Leadoff Swing. Ricochets off walls and the Pitching Machine. Double Play can use it as the first link. Primed targets take bonus damage from the piercing hit.

## 4. Worm Burner
- **Type / tags:** Attack, Melee, Strike, AoE, Projectile (rolling), **Spender** (1 Runner), terrain interaction.
- **What it does:** A low chop sends a ground ball skidding along the floor. It rolls, bowling over small enemies and knocking them down, and bounces off walls, furniture and toy blocks for extra hits. Rolling enemies get tripped (briefly prone and Primed).
- **Baseball source:** Grounder / "worm burner" (<10° launch angle), ball bounces off the outfield wall.
- **Animation / feel:** A low sweeping scoop with the bat near the ground, dust puff and chalk-line smear. The ball makes a rapid thrum as it rolls, and each pin it hits makes a bowling-style clatter. Off walls it makes a *bonk* and a cartoon spring noise.
- **Scaling:** Area (ball size), number of bounces, projectile speed, physical and stun buildup. Runners spent add bounces.
- **Grows into a build:** Packs-in-corridors clear and a Primed applier. With bounce and area supports it fills a room with ricochets, a "pinball" build.
- **Synergies:** Primes for Infield Fly (a prone enemy popped up is a full combo) and Squeeze Play. Dropped balls from Bunt become free grounders. Double Play can start from the ricochet.

## 5. Infield Fly
- **Type / tags:** Attack, Melee, Strike, Cooldown (6s), Launch, Culling.
- **What it does:** An uppercut that pops a target nearly straight up (a high pop-up). Airborne enemies are "called out": anything that falls below 30% life when it lands, or that is Primed, is finished off automatically. Doesn't work on line drives, so it won't cull anything hit by Line Drive.
- **Baseball source:** Infield fly rule: the batter is out whether or not the ball is caught (<2 outs, runners 1st and 2nd or loaded). Pop-ups are >50° launch angle.
- **Animation / feel:** A deep scoop and rising swing. Hit-stop on contact, then the enemy goes up with a *whoosh* and a rising tone. At the apex an umpire's arm and a little ghost "INFIELD FLY" banner appear, then a signature *ding* as the enemy lands and cartoon-poofs.
- **Scaling:** Cooldown recovery, culling threshold, launch height (airborne duration), melee damage. Larger culling threshold at high levels makes it a mid-boss executioner.
- **Grows into a build:** A single-target and elite-killer utility. Pairs with stun-prime builds. In Bases Loaded it launches everything in a small area.
- **Synergies:** Worm Burner and Squeeze Play prime it. Line Drive and Double Play hit airborne enemies for bonus damage. Grand Slam treats airborne enemies as "in the air" for a damage bonus.

## 6. Sweeper
- **Type / tags:** Attack, Melee, Strike, AoE, Slam-like arc, **Spender** (optional Runners add range).
- **What it does:** A huge horizontal 180° sweeping slash that pulls enemies sideways ("sweeping" across the plate) and leaves them clustered at the edge. A Barrel hit adds a second pass that comes back the other way.
- **Baseball source:** The sweeper breaking ball: a slider with big horizontal movement (~80 mph); also a full pull-side swing.
- **Animation / feel:** Wide stance, big wind-up, then a two-handed flat sweep with a visible bat-trail arc in the team colour. Good impact is a deep *whump* with a heavy 0.15s stop and a camera nudge in the swing direction. Light objects (toys, marbles) fly off the field.
- **Scaling:** Area of effect and arc width, melee/physical damage, knockback distance (exit velocity), attack speed. Runners spent increase radius.
- **Grows into a build:** The main pack-clearing skill for AoE builds. Add "pull vs opposite field" supports to push packs into hazards or toward the wall for combos.
- **Synergies:** Gathers enemies for Double Play chains and Grand Slam. Early/late timing sets knockback direction (toward sprinklers or into the Pitching Machine's line).

## 7. Double Play
- **Type / tags:** Attack, Projectile, **Chain**, Cooldown (4s), Spender (1 Runner).
- **What it does:** Hit a ball that ricochets between up to 3 enemies in a "6-4-3" chain. Each link hits for the same damage; if all three connect, the second and third each give a Runner back.
- **Baseball source:** The 6-4-3 / around-the-horn double play: shortstop to second to first, two outs in one motion.
- **Animation / feel:** A clean contact and the ball becomes a white-stitched comet with a number floating above each target (6, 4, 3) as the ball leaves it, matching the real fielding notation. Each link makes a rapid *pop-pop-pop* like a glove catch with ascending pitch. The last target gets a bigger stop.
- **Scaling:** Chain count, projectile damage, projectile speed, crit. "Chain damage over 3" at the high end.
- **Grows into a build:** The mid-range pack skill for chain and projectile builds. Add chain supports and the number of links grows, with the numbers getting silly (9-6-4-3-...).
- **Synergies:** Great after Sweeper (targets clustered). Works with Infield Fly (hit airborne for bonus). Refunds Runners for Grand Slam. Fed by Pitching Machine balls.

## 8. Squeeze Play
- **Type / tags:** Attack, Melee, Setup, Cooldown (5s), Duration (3s).
- **What it does:** A bunt that sends a ball rolling to the target. It marks the enemy **Primed (Squeezed)** for 3 seconds. The next time that enemy takes damage from a *movement* skill (Steal Base slide or Diving Catch), the mark detonates for a large AoE blast. Hitting it with any other skill just consumes it for small bonus damage.
- **Baseball source:** Squeeze play: a bunt timed to score the runner from third. Runner breaks as the bunt is laid.
- **Animation / feel:** A gentle bunt with a deliberate pause. The ball rolls with a spring-wound ticking and a little third-base flag appears over the target. The detonation is a satisfying pop with a confetti burst and a mini hit-stop, plus the runner "scoring" sound.
- **Scaling:** Detonation damage (added as a modifier on the movement skill), area, duration, and Primed buildup. Works with Runner spending: Bases Loaded doubles the blast.
- **Grows into a build:** A deliberate setup-and-payoff skill for boss rotations. Movement-based builds use it as the "bomb" they run into.
- **Synergies:** Steal Base and Diving Catch are the detonators. Tag Up resets its cooldown. Infield Fly benefits from a Squeezed target. Worm Burner primes quickly.

## 9. Check Swing
- **Type / tags:** Attack, Guard, Cooldown (2s), Timing-based, Cancel.
- **What it does:** During any Strike's wind-up you can press Check Swing to stop the swing mid-motion. This cancels the recovery, grants a 0.4s dodge window, and—if an enemy attack lands during the dodge—counter-strikes that attacker for bonus damage. If no attack lands, you gain a stack of "Patience" (+crit chance for the next Strike, up to 3).
- **Baseball source:** Check swing: bat stopped before the barrel crosses the plate; the umpire judges whether it's a swing. Also taking a ball ("walk") to build patience.
- **Animation / feel:** The bat freezes mid-arc with a comical squeak, the batter leans back, hat tilting. Enemy swipes whiff past with a *whoosh*. If the counter triggers, a tiny "safe/ball" umpire call plays and the counter strike hits with hit-stop. Patience stacks show as little ball icons.
- **Scaling:** Dodge window duration, counter damage, Patience stacks and the crit chance they provide, cooldown recovery.
- **Grows into a build:** The skill that makes the class feel tight: animation cancels give high-skill players a way to chain attacks while staying safe. Tanky builds convert it into pure defence.
- **Synergies:** Cancels Leadoff Swing and Sweeper recovery, fuels Barrel crits (Patience), and pairs with Pickoff-style counters. Bunt is the stationary equivalent.

## 10. Steal Base
- **Type / tags:** Movement, Travel, AoE (dust), Cooldown (charges: 2).
- **What it does:** Sprint forward and slide into the target spot. During the slide you have brief invulnerability and knock small enemies aside, leaving a dust trail that slows enemies. Sliding into an enemy "tags" them for bonus damage if Squeezed.
- **Baseball source:** Stolen base: jump off the lead, then a head-first or hook slide. Catcher's pop time sets the risk.
- **Animation / feel:** A short lead-off crouch, a burst of speed with cartoon dust poof, then a dramatic slide with a dust cloud and chalk marks. Cartoon "SAFE!" voice and umpire arms spread at the end. 0.1s of camera dip on arrival.
- **Scaling:** Movement speed, slide distance, charges, dust-trail slow strength and duration. "Travel" tag modifiers.
- **Grows into a build:** The primary dodge/gap-closer. Builds that want to stay mobile stack charges and slide distance; dust becomes a damage-over-time or slow zone.
- **Synergies:** Detonates Squeeze Play. Tag Up resets its charges. Hit-and-run style: Leadoff Swing immediately after a slide gets a Barrel bonus. Dust trail slows enemies for Worm Burner and Double Play.

## 11. Tag Up
- **Type / tags:** Utility, Travel, Anchor, Cooldown (10s).
- **What it does:** Plant a **Base** at your feet (a bright square bag). Anywhere within range, press again to return. Returning *resets cooldowns* of your Travel/Cooldown skills and grants a short speed boost. Only one Base at a time; it lasts 8 seconds. Standing on the Base restores a small amount of life each second.
- **Baseball source:** Tag up: after a fly ball is caught, the runner must retouch the base before advancing (the sac fly). Home base as a safe spot.
- **Animation / feel:** The batter stomps a square canvas bag down with a puff of chalk. Returning plays a quick stretch-and-dive back with a "caught napping" cartoon sound and a bell *ding* as the Base resets. Base glows when ready.
- **Scaling:** Duration, cooldown reset strength, healing on the Base, Base radius (buffs allies/summons standing on it).
- **Grows into a build:** The glue that lets cooldown-based builds loop. Gives a positional puzzle: plant the base before a boss arena mechanic and return.
- **Synergies:** Resets Steal Base, Infield Fly, Squeeze Play, Double Play. Pitching Machine placed next to the Base is protected by its aura. Seventh-Inning Stretch can pulse from the Base.

## 12. Diving Catch
- **Type / tags:** Movement, Travel, Guard, Projectile-interact, Cooldown (6s).
- **What it does:** Dive forward at full extension. If you intercept a projectile along the dive, you catch it and can throw it back at the attacker with extra damage (return damage scales with the projectile's own). Without a catch, you simply cover distance and land with a small AoE.
- **Baseball source:** Diving catch / web gem: full-extension dive ends in a catch; shoestring catch.
- **Animation / feel:** A stretched, almost slow-motion leap with a glove on the end of the bat (or a mitt in the off hand), a long cartoon *fwoosh*, then a slap-catch with a leather *pock* and brief slow-mo (0.2s) on a successful catch. Grass stains on the character's knees afterward. Crowd gasp.
- **Scaling:** Return damage multiplier, catch radius, dive distance, cooldown recovery, and "block chance" for the catch.
- **Grows into a build:** The offensive-defence tool vs ranged enemies and bosses (sprinkler spray, thrown marbles, ball turrets). Builds that want to turn enemies' attacks against them stack return damage.
- **Synergies:** Detonates Squeeze Play. Returns can be hit again by Line Drive for a double-hit. Check Swing is the melee counterpart. Catching Pitching Machine balls (your own) is a fun loop.

## 13. Pitching Machine
- **Type / tags:** Summon, Projectile, Duration (12s), Cooldown (14s).
- **What it does:** Deploy a wind-up pitching machine that lobs balls at the nearest enemy every second. Balls that you hit (by running into them or swinging at them) get empowered with your hit's stats. Hitting a pitched ball with a Strike always counts as a Barrel.
- **Baseball source:** The batting cage, the machine that feeds the batter; hit-the-ball two-part combo.
- **Animation / feel:** A clunky toy-box machine unfolds with springs, a *clank-whirr* spin-up, a *fwump* each throw and a small "ready" light. Balls arc in the air so you can see the sweet-spot timing. Each Barrel on a pitched ball gets the loudest crack.
- **Scaling:** Summon duration, throw rate (attack speed), projectile damage, number of machines. Machine inherits a fraction of your attack and projectile modifiers.
- **Grows into a build:** The bridge to summoner/support styles. With "tee-ball" support the machine stands still and every ball is a guaranteed Barrel. Multiple machines make a "batting cage" build.
- **Synergies:** Provides guaranteed-Barrel feeds for Leadoff Swing generators. Line Drive and Double Play use pitched balls as projectiles. Bunt can deaden one for a free Runner. Tag Up protects the machine.

## 14. Seventh-Inning Stretch
- **Type / tags:** Aura, Duration (6s pulse, 18s cooldown), Warcry-like, Support.
- **What it does:** Everyone stands and sings. For 6 seconds, a pulse every second heals you and allies in range and grants **Rally** (brief attack speed). If you are below 35% life when you cast it, it also activates **Rally Cap**: +damage and +move speed while the pulse lasts.
- **Baseball source:** The seventh-inning stretch ("Take Me Out to the Ball Game"), the rally cap sparking a comeback.
- **Animation / feel:** The bat is planted, the batter takes off the cap and flips it backwards (rally cap). A ghostly crowd of toy fans stands up, an organ plays a short bar of the song and each pulse makes a warm chord with a golden ring. Hit-stop none, the sound is the feedback.
- **Scaling:** Duration, pulse healing, area, attack-speed bonus, low-life bonus for Rally Cap.
- **Grows into a build:** The big recovery and buff tool. Low-life builds lean on Rally Cap, support builds extend duration and area for co-op.
- **Synergies:** Boosts attack speed for Leadoff Swing generators and Check Swing. Pulses from Tag Up's Base. Extra pulses at Bases Loaded. Grand Slam gets "crowd" bonus damage during the Stretch.

## 15. Pickoff
- **Type / tags:** Attack, Projectile, Cooldown (8s), Counter, Single-target.
- **What it does:** Snap-throw a ball (hit from the bat hand) at an enemy's back. If the target is currently winding up, charging or leaning into an attack (a wind-up toy's key spinning, a vacuum charging), the throw deals triple damage and interrupts the attack ("caught napping") and Primes the target.
- **Baseball source:** Pickoff: catching a runner leaning off the bag. A balk is a fake that doesn't work, so only real telegraphs count.
- **Animation / feel:** A quick sidearm flick with a *whap*, the ball zips with a streak. On a successful pickoff, the target's key stops spinning with a rubber squeak, a "OUT!" gesture from an umpire and a big 0.15s stop with a camera zoom. If it's not a telegraph, it just does ordinary damage with no stop.
- **Scaling:** Counter damage multiplier, projectile speed, interrupt power, crit. "Caught napping" scaling by how much of the telegraph had elapsed.
- **Grows into a build:** The boss-fight skill. Rewards players who learn the enemy tells and gives a big payoff for reading them. Boosts make it a stunning stun-setup.
- **Synergies:** Primes targets for Infield Fly and Grand Slam. Check Swing keeps you safe while you wait for the telegraph. Squeeze Play and Pickoff both prime, so Pickoff is the safer way to start a boss rotation.

## 16. Grand Slam
- **Type / tags:** Attack, Melee, Slam, AoE, **Ultimate**, **Spender** (requires 3 Runners = Bases Loaded), Cooldown (30s).
- **What it does:** Spend all 3 Runners. Hit a giant ball that arcs high and crashes into the target zone as a massive explosion. Damage scales with Runners spent (4× at Bases Loaded: "four runs") and gains bonus vs airborne, Primed or Squeezed enemies. Enemies it kills set off smaller secondary explosions (the "walk-off").
- **Baseball source:** Grand slam (home run with bases loaded, 4 runs), the home-run trot, the walk-off.
- **Animation / feel:** The camera slows, the stadium lights come on, the diamond HUD lights all three bases. A huge overhead swing with a long hit-stop (0.2s), *CRACK* and a camera punch followed by a moonshot arc across the screen with a ground-targeted decal showing the landing spot. The impact is a huge fireworks burst. The batter does a quick, invulnerable home-run trot (a few steps with a cap-tip) as a recovery, short and funny.
- **Scaling:** Area, damage per Runner, crit, cooldown recovery, "walk-off" explosions on kill. Heavy-investment builds compress the cooldown by feeding Runners quickly.
- **Grows into a build:** The ultimate payoff that organizes the whole kit: generate Runners with Leadoff Swing, Bunt and Double Play, then cash them in. Defines "cleanup hitter" builds.
- **Synergies:** All generators feed it; Pickoff and Squeeze Play prime for the bonus. Infield Fly (airborne) amplifies it. Seventh-Inning Stretch pulses add the crowd bonus. Tag Up resets its cooldown.

---

## Three example builds

### A. "Leadoff Machine" — fast-attack crit generator build (bossing + clear)
- **Core:** Leadoff Swing (main) → Line Drive and Grand Slam as spenders.
- **Support:** Pickoff for boss telegraphs; Check Swing to cancel recoveries; Steal Base for mobility; Tag Up to reset it.
- **Scaling:** Attack speed, crit chance and multiplier, "extra Runner on Barrel".
- **Loop:** Swing to fill the diamond, Line Drive to pierce down the line, Grand Slam on a Pickoff-primed boss. Check Swing between hits keeps you safe.

### B. "Pinball Cage" — projectile / summon ricochet build (pack clearing)
- **Core:** Pitching Machine feeds balls; Worm Burner and Double Play bounce them.
- **Support:** Sweeper to cluster enemies, Bunt to turn enemy shots into balls, Tag Up to protect the machines.
- **Scaling:** Projectile damage, chain and bounce count, summon duration, area.
- **Loop:** Drop 1–2 machines near a wall, Sweeper to gather, Worm Burner into the corner, Double Play to chain through the pack. Grand Slam on rares.

### C. "Cleanup Mover" — mobile Squeeze-and-detonate build (elite / boss killer)
- **Core:** Squeeze Play → Steal Base or Diving Catch as the detonator → Infield Fly to cull.
- **Support:** Check Swing for safe starts, Seventh-Inning Stretch for recovery (Rally Cap at low life), Tag Up for cooldown resets.
- **Scaling:** Movement speed, cooldown recovery, culling threshold, Primed buildup.
- **Loop:** Squeeze an elite, slide into it for the blast, pop it with Infield Fly, Tag Up to reset and repeat. Low-life Rally Cap turns near-misses into a power spike.
