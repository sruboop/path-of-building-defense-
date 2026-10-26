# The Slugger: 16 bat skills

A toy-sized little-leaguer with a baseball bat, fighting through a giant
backyard, bedroom, garage and a little-league field at dusk. Every skill is
one baseball idea you can read at a glance.

This set combines the two proposals from the A/B test in `ab-test/`. It
takes the codegraph proposal's core systems and adds the best skills from
the plain proposal, as both blind reviewers recommended. Every number is a
starting point to playtest, not a balanced value.

## Core systems (only three)

| System | Rule |
|---|---|
| **Runners** (resource, 0–3) | A base diamond on the HUD. Generators put runners on base; spenders "drive them in" for more damage per runner. Three runners is **Bases Loaded**. |
| **Barrel** (timing) | Every bat swing has a sweet-spot window late in the swing (and the outer ring of the arc). Hit it for a **Barrel**: a guaranteed crit, the longest hit-stop, the loudest *CRACK*, and +1 Runner from generators. Attack speed makes the swing faster, but not the window, so it stays learnable. |
| **The Count** (enemy state) | Hits put **Strikes** on an enemy. The 3rd is a **Strikeout**: stunned and taking +25% damage for 4 s. Payoff skills read Strikeouts. |

Tags: Attack, Melee, Strike (bat swing), Projectile, AoE, Chain, Movement,
Guard, Summon, Aura, Duration, Cooldown, Ultimate.

**Pitch supports** (support gems that change any Projectile skill):
- **Fastball:** +speed, +pierce.
- **Slider:** curves to one side.
- **Screwball:** curves the other way.
- **Changeup:** hits late, +damage.
- **Tee-Ball:** slower, but every hit is a Barrel.

---

## Generators

### 1. Full Swing: Hit for the Cycle
- **Tags:** Attack, Melee, Strike, AoE (arc). Basic, no cost.
- **Does:** A 4-hit combo: **Single → Double → Triple → Home Run**. Each hit is wider and harder; the Home Run knocks enemies back into walls and hazards. Barrels add Runners. Landing all four in one combo triggers **Cycle**: +attack speed and +damage for 4 s.
- **Baseball:** swing phases (stance, load, swing, impact), the sweet spot, hitting for the cycle.
- **Feel:** hit-stop climbs from 2 frames on the Single to 6 on the Home Run. A wooden *tock* rises in pitch each hit; the Home Run adds a *CRACK* and a dust ring. A Barrel flashes a gold ring. Recovery can be cancelled into any skill.
- **Scaling:** attack speed, crit, melee/physical damage, area, added elemental damage (the Home Run hit ignites).
- **Synergies:** feeds every spender. Strikes build toward Strikeouts. The Home Run hit knocks enemies into Rundown and Worm Burner lanes.

### 2. Bunt
- **Tags:** Attack, Melee, Guard, Cooldown (2 s).
- **Does:** Square up and catch whatever comes in. Projectiles in a small cone **drop dead** at your feet as balls (ammo). A melee hit absorbed in the 0.2 s perfect window staggers the attacker. Any deadened projectile or hit gives +1 Runner.
- **Baseball:** the sacrifice bunt (give up the swing to move the runner over) and the drag bunt.
- **Feel:** the bat goes still, soft *thup*, almost no hit-stop, the ball plops and rolls with squash-and-stretch. A sprinkler's spray just dribbles away.
- **Scaling:** cone size, perfect window, block, cooldown recovery, Runner gain.
- **Synergies:** dead balls feed Double Play, Line Drive and Pitching Machine. It turns ranged enemies into free resource.

### 3. Steal Base
- **Tags:** Movement, Attack, Cooldown (2 charges).
- **Does:** Sprint and slide. You're immune during the slide, and small enemies in the path are tripped. Sliding *through* an enemy's attack wind-up is a **Stolen Base**: +1 Runner and a free Strike on that enemy.
- **Baseball:** stealing on the pitcher's motion; feet-first and head-first slides.
- **Feel:** a lead-off crouch, burst, then a long dust-streak *shhhk*. An umpire's "SAFE!" arms pop up when you steal through an attack.
- **Scaling:** move speed, charges, slide distance, cooldown recovery. Supports turn the dust trail into a slow.
- **Synergies:** your main dodge, and it rewards dodging *into* danger. Gets you in range for Full Swing and Grand Slam.

## Spenders

### 4. Line Drive
- **Tags:** Attack, Strike, Projectile, Pierce. Spends 1 Runner.
- **Does:** A flat, fast "frozen rope" that pierces everything in a line. A spent Runner adds pierce and damage. It uses a dead ball if one is near, for bonus damage.
- **Baseball:** the line drive (10–25° launch angle), the hardest-hit ball.
- **Feel:** a short level snap. The ball flashes white and leaves a vapour line. Each enemy pierced gives a *ting* and a tiny stop; the last one gets a *thwack*. Sound pitch rises with speed.
- **Scaling:** projectile damage/speed, pierce, crit, extra projectiles, pitch supports.
- **Synergies:** spends Runners from generators; ammo from Bunt and Pitching Machine. Ricochets off the Pitching Machine.

### 5. Worm Burner
- **Tags:** Attack, Strike, Projectile (rolling), AoE. Spends 1 Runner.
- **Does:** A low chop sends a grounder skidding along the floor. It bowls over small enemies (knocked down, +1 Strike) and **bounces off walls, furniture and toy blocks** for extra hits. Each Runner spent adds bounces.
- **Baseball:** the grounder / "worm burner" (<10° launch angle), balls off the outfield wall.
- **Feel:** a low scoop and chalk smear. The rolling ball thrums; enemies scatter like bowling pins; walls go *bonk* with a cartoon spring.
- **Scaling:** bounces, area (ball size), projectile speed, stun buildup.
- **Synergies:** "pinball" clear in corridors and toy-block rooms. Knocked-down enemies are set up for Infield Fly.

### 6. Curveball
- **Tags:** Attack, Strike, Projectile. Spends 1 Runner.
- **Does:** A ball that bends around its target and hits from the **side or behind** for +40% damage, getting around shields and cover. Hold to choose the bend direction (curve or screwball). If it misses, it comes back like a boomerang.
- **Baseball:** the Magnus effect: topspin/sidespin bends the pitch; the screwball breaks the opposite way.
- **Feel:** a roll-over swing with a twist, a blue spiral trail and a doppler *whoosh-whoosh* as it bends.
- **Scaling:** projectile damage, bend strength, crit, extra projectiles (one curve each way).
- **Synergies:** finishes enemies held by Rundown or stuck on shields; flanks bosses that face you.

### 7. Sweeper
- **Tags:** Attack, Melee, Strike, AoE. Spends Runners (each widens it).
- **Does:** A huge 180° sweep that **drags enemies sideways** and leaves them clustered at the edge of the arc. A Barrel adds a return pass.
- **Baseball:** the sweeper (a slider with big horizontal break) and a full pull-side swing.
- **Feel:** wide stance and big wind-up, then a flat two-handed sweep with a team-colour trail. A deep *whump*, a heavy 0.15 s stop and a camera nudge; toys and marbles fly off-screen.
- **Scaling:** area, arc width, melee damage, knockback distance, attack speed.
- **Synergies:** the pack gatherer for Double Play, Eephus and Grand Slam. Aim the drag into sprinklers and other hazards.

### 8. Double Play
- **Tags:** Attack, Projectile, Chain. Spends 1 Runner.
- **Does:** A ball that chains **6 → 4 → 3** between three enemies, with the fielding numbers floating over each. If all three links hit, two Runners come back. If all three already have Strikes, it becomes a **Triple Play** with a fourth link.
- **Baseball:** the 6-4-3 double play, the triple play, scorekeeping notation.
- **Feel:** clean contact, then a white-stitched comet going *pop-pop-pop* like glove catches, rising in pitch. Bigger stop on the last link. Chain supports make the numbers get silly (9-6-4-3-…).
- **Scaling:** chain count, projectile damage, crit.
- **Synergies:** best right after Sweeper. Refunds Runners for Grand Slam.

## Setup and control

### 9. Infield Fly
- **Tags:** Attack, Melee, Strike, Cooldown (6 s). Launch, cull.
- **Does:** An uppercut that pops a target straight up. When it lands it's **called out**: enemies below 30% life, or Struck out, are finished off instantly.
- **Baseball:** the infield fly rule: the batter is out whether or not the ball is caught.
- **Feel:** a rising scoop and a *whoosh* with a rising tone. At the top, an umpire arm and an "INFIELD FLY!" banner; a *ding* on landing and a cartoon poof.
- **Scaling:** cull threshold, airtime, cooldown recovery, melee damage. In Bases Loaded it launches a small area.
- **Synergies:** the elite and boss finisher. Airborne enemies take bonus damage from Line Drive, Double Play and Grand Slam.

### 10. Eephus
- **Tags:** Attack, Projectile, AoE, Cooldown (8 s).
- **Does:** A ridiculously slow, high lob. It lands after 1.5 s on a big red circle for a huge hit. Swing at it again at the top of its arc (a timing ring) and it comes down as a meteor for double damage.
- **Baseball:** the eephus (~55 mph junk pitch). Rip Sewell threw it; Ted Williams homered off one in the 1946 All-Star Game.
- **Feel:** a slow-motion uppercut and a slide-whistle *bwoooop* going up. A shadow and a ring show where it lands. *BOOM*, a long stop and screen shake.
- **Scaling:** area, damage, crit, cooldown recovery, shorter fall time.
- **Synergies:** lands on enemies held by Rundown, clustered by Sweeper, or Struck out. The bat-swing timing skill rewards Barrel practice.

### 11. Rundown ("Pickle")
- **Tags:** Summon/Trap, AoE, Duration (5 s), Cooldown (14 s).
- **Does:** Two **lawn-gnome fielders** pop up at two points. Enemies on the line between them are caught in a pickle: forced to run back and forth, slowed, and hit by a throw at each end (+1 Strike per throw).
- **Baseball:** the rundown, a runner trapped between two bases while fielders throw back and forth.
- **Feel:** the gnomes tip their caps, then throw with a *pang!*; ball trails link them. Trapped enemies zig-zag with a "wheee".
- **Scaling:** duration, throw damage, line length, number trapped, slow.
- **Synergies:** holds enemies for Eephus and Curveball. Full Swing's Home Run knocks enemies into the pickle.

### 12. Pickoff
- **Tags:** Attack, Projectile, Cooldown (8 s). Counter, single target.
- **Does:** A snap throw at one enemy. If it's **winding up an attack** (a wind-up toy's key turning, a vacuum charging), the throw deals triple damage, interrupts it ("caught napping") and gives an instant Strikeout.
- **Baseball:** the pickoff, catching a runner leaning off the bag. A balk is a fake, so only real wind-ups count.
- **Feel:** a sidearm flick and a *whap*. On a pickoff, the toy's key stops with a rubber squeak, an umpire "OUT!" pops up, and a 0.15 s stop with a camera zoom. On anything else it just does normal damage.
- **Scaling:** counter multiplier, projectile speed, crit, cooldown recovery.
- **Synergies:** the boss skill: read the tell, Pickoff, then Grand Slam the Struck-out boss.

## Defence and utility

### 13. Check Swing
- **Tags:** Attack, Guard, Cooldown (2 s). Cancel.
- **Does:** Stop any swing halfway. It cancels the recovery, gives a 0.4 s dodge window, and counter-hits anything that attacks during it (+1 Strike). If nothing attacks you, you gain **Patience** instead (+crit for your next swing, stacks to 3).
- **Baseball:** the checked swing; taking pitches to work the count.
- **Feel:** the bat freezes mid-arc with a squeak and a wobble; swipes whiff past. A "NO SWING!" pop-up and a quick counter-hit.
- **Scaling:** dodge window, counter damage, Patience crit, cooldown recovery.
- **Synergies:** the skill-ceiling button: cancel Full Swing's Home Run or Sweeper's recovery and stay safe.

### 14. Pitching Machine
- **Tags:** Summon, Projectile, Duration (12 s), Cooldown (14 s).
- **Does:** Unfolds a clunky toy pitching machine that lobs a ball at the nearest enemy every second. Hit one of its balls with any swing and it's **always a Barrel**, fired off with your skill. Pitch supports choose what it throws.
- **Baseball:** the batting cage and practice pitching machines.
- **Feel:** springs and a *clank-whirr* when it sets up, a *fwump* per pitch, and a dotted arc so you can time your swing. The hardest *CRACK* in the game.
- **Scaling:** pitch rate, number of machines, duration, projectile damage. The machine copies some of your projectile modifiers.
- **Synergies:** a stream of guaranteed Barrels and Runners. Line Drive and Double Play fire its balls. The core of the "batting cage" build.

### 15. Seventh-Inning Stretch (Rally Cap)
- **Tags:** Aura, Duration (6 s), Cooldown (18 s).
- **Does:** The crowd stands and sings. Every second it heals you and allies nearby and grants attack speed. If you cast it below 35% life, you flip your **Rally Cap**: +damage and +move speed for the duration.
- **Baseball:** the seventh-inning stretch ("Take Me Out to the Ball Game") and the rally cap comeback superstition.
- **Feel:** you plant the bat and flip your cap inside-out. A ghostly crowd of toy fans stands up, an organ plays a bar, and a warm chord sounds with each pulse.
- **Scaling:** healing, area, duration, attack-speed bonus, low-life bonus.
- **Synergies:** recovery for any build; the Rally Cap powers low-life builds; extends co-op play.

## Ultimate

### 16. Grand Slam
- **Tags:** Attack, Melee, AoE, Ultimate, Cooldown (30 s). Needs Bases Loaded.
- **Does:** Spend all 3 Runners on a giant moonshot that comes down as a huge explosion: **four runs, 4× damage**. Bonus against airborne and Struck-out enemies. Kills set off smaller **walk-off** blasts. With fewer Runners it's a weaker **Sacrifice Fly**.
- **Baseball:** the grand slam (four runs with the bases loaded), the walk-off.
- **Feel:** time slows, the stadium lights come on and all three bases light up. A huge overhead swing with a 0.2 s stop and a *CRACK*, then the ball arcs across the screen with a landing marker. A fireworks blast, a "GRAND SLAM!" banner, and a short, invulnerable home-run trot as the recovery.
- **Scaling:** damage per Runner, area, crit, cooldown recovery, extra walk-off blasts.
- **Synergies:** the payoff that organises the whole kit: generate, set up Strikeouts, cash in.

---

## Example builds

**Cycle Slugger** (melee crit, boss + clear)
- **Skills:** Full Swing main, Check Swing, Steal Base, Pickoff, Grand Slam.
- **Scaling:** attack speed, crit, melee.
- **Loop:** finish the Cycle → cancel recoveries with Check Swing → Pickoff the boss's wind-up for a Strikeout → Grand Slam.

**Batting Cage** (projectile / summon)
- **Skills:** Pitching Machine ×2 with Fastball and Slider, Line Drive, Double Play, Bunt, Sweeper.
- **Scaling:** projectile damage, chain, pierce, number of machines.
- **Loop:** set the machines by a wall, Sweeper the pack together, Double Play it, Line Drive the line, Bunt the enemy shots for more balls.

**Pinball Trapper** (control / area)
- **Skills:** Rundown, Worm Burner, Eephus, Curveball, Seventh-Inning Stretch.
- **Scaling:** area, bounces, duration, stun buildup.
- **Loop:** pickle the pack between gnomes, bounce grounders through the toy blocks, then drop an Eephus meteor on the stuck crowd. Curveball goes around shields; the Stretch heals.
