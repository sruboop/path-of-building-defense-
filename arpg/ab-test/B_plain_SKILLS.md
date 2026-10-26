# SKILLS — "The Slugger" (baseball-bat class, toy-scale ARPG)

## 0. Research digest → design rules

**Sources used** (web search this session): [Blast Motion swing phases](https://blastmotion.com/?p=123744), [Statcast barrel / launch-angle summaries](https://rapsodo.com/what-is-exit-velocity-and-how-to-increase-it/), [COMSOL pitch physics](https://www.comsol.com/blogs/physics-behind-baseball-pitches), [Baseball-Reference Eephus](https://www.baseball-reference.com/bullpen/Eephus), [Little League infield fly](https://www.littleleague.org/university/articles/explanation-infield-fly-rule), [Wikipedia: Bunt](https://en.wikipedia.org/wiki/Bunt_(baseball)), [Checked swing](https://en.wikipedia.org/wiki/Checked_swing), [Rally cap](https://en.wikipedia.org/wiki/Rally_cap), [It Takes Two](https://en.wikipedia.org/wiki/It_Takes_Two_(video_game)), [Hypercritic on its level tools](https://hypercritic.org/collection/it-takes-two-hazelight-studios-review-analysis-2021), [PoE2 skill gem system](https://mobalytics.gg/poe-2/guides/skill-gem-system), [PoE wiki gem tags](https://pathofexile.fandom.com/wiki/Gem_tag), [D4 Barbarian generators/spenders](https://icy-veins.com/d4/barbarian-class-abilities), [hit-stop notes](https://bugnet.io/blog/how-to-use-hit-pause-to-make-impacts-feel-powerful).

**Gaps:** searches returned nothing usable on the changeup, rundowns, relay/cutoff throws, the seventh-inning stretch, the cycle, walk-offs, the home-run trot, or PoE2 combo/ailment specifics. I filled those from general knowledge; treat them as unverified. Also, no source ties the rally cap to the 1987 Twins (that was the Homer Hanky). Rally-cap origins are disputed, with the Mets' mid-80s inside-out caps the best-known. I use "rally cap" generically.

**Facts that drive the design**
- *Swing phases:* stance → load → transition → swing → impact, a kinetic chain from ground up. Every attack gets **load / swing / follow-through** frames (anticipation, hit, recovery).
- *Sweet spot:* a small zone near the barrel (~6" from the end). Melee skills reward hitting with the **barrel end of the arc** (the outer ring), not the handle.
- *Launch angle × exit velocity:* "barrel" ≈ 26–30° and 98+ mph. Low line drives are fastest, ~25–30° goes farthest. So projectile skills have an **angle choice**: flat = fast and piercing, high = slow, far and AoE.
- *Pitch physics:* spin makes a Magnus force. Topspin/curve drops and bends, sidespin bends sideways (slider), the screwball bends the opposite way, the knuckleball is near spinless and wobbles unpredictably, the eephus is a ~55 mph or slower high arc, and a changeup is a fastball-looking pitch that arrives slow.
- *PoE2:* tags decide which modifiers apply. Support gems change a skill without adding abilities. Scaling comes from attack speed, area, crit, ailments, projectile count, and cooldown recovery.
- *D4:* basic skills generate a resource and core skills spend it.
- *Feel:* hit-stop of a few frames (≈50–100 ms for heavy hits) on the involved objects only, never the whole game. Add telegraphs, anticipation, and animation cancels.
- *It Takes Two:* each level's tools come from its setting (clock = time, hive = sap + fire). Our skills should read as **toys and yard objects doing baseball**.

### Shared systems (kept small)
| System | Rule |
|---|---|
| **Hype** (resource) | Generators (⊕) build it, spenders (⊖) cost it. Capped at 100, decays out of combat. |
| **The Count** | Hits from *Attack* skills put **Strikes** on an enemy (max 3). The 3rd Strike is a **Strikeout**: a stun plus 25% more damage taken for 4 s, and you gain a **Runner**. |
| **Runners** | 0–3 charges shown as bases on the HUD diamond (also gained by Slide). At 3 you are **Bases Loaded**. |
| **Dead balls** | Bunt and kills drop ball pickups at your feet. Some skills use them as ammo. |
| **Supports** (PoE2-style) | Pitch types are support gems: **Slider** (+sidespin, projectiles curve to a side), **Screwball** (opposite curve), **Changeup** (delayed hit, +damage), **Fastball** (+speed, pierce). These aren't among the 16, but the skills below are written to take them. |

Tag shorthand: **A**=Attack, **M**=Melee, **P**=Projectile, **AoE**, **Mv**=Movement, **CD**=Cooldown, **Ch**=Channel, **Dur**=Duration, **Gen**/**Sp**=generator/spender. Damage types: Physical, Fire, Lightning.

---

## 1. Full Swing — "Hit for the Cycle"
- **Type/tags:** Attack, Melee, AoE (arc), Physical, Gen ⊕ (+8 Hype/hit). No cooldown.
- **What it does:** A 4-hit bat combo in a frontal arc. The hits are **Single → Double → Triple → Home Run**, and each is wider and harder than the last. The Home Run hit knocks enemies back, off ledges and into walls. Enemies hit on the **outer barrel ring** take a Sweet Spot crit. Landing all four within the combo window triggers **Cycle**: a short damage and speed buff.
- **Baseball source:** swing phases (stance, load, swing, impact), the sweet spot, and "hitting for the cycle" (single, double, triple, home run in one game).
- **Animation/feel:** a quick two-foot load, a hip-first rotation, and a short follow-through. Hit-stop is 2 frames on a Single and 6 on the Home Run (only the hit enemy and the bat freeze). Sound is a wooden *tock* that climbs in pitch with each hit. The Home Run hit adds a *crack*, a white-flash arc and dust ring. Sweet-spot hits give a brighter spark and a ping. You can cancel into any skill during recovery.
- **Scaling/build:** attack speed (shortens the load), area (fatter arcs), crit chance and multiplier (Sweet Spot crits), physical %, melee. It is the base for **Melee/Crit Slugger** builds. Supports: *Added Fire* (the Home Run hit ignites), *Multistrike*, *Heavy Swing* (slower, bigger).
- **Synergies:** the Hype generator that feeds every spender. It lays Strikes for **Strikeout** → Runners → **Grand Slam**. The Home Run hit knocks enemies into **Rundown** zones. It cancels into **Check Swing**.

## 2. Line Drive
- **Type/tags:** Attack, Projectile, Physical, Sp ⊖ (15 Hype), uses a ball.
- **What it does:** Smacks a ball in a straight, fast line that **pierces** all enemies. Hold to set the **launch angle** (flat = more speed and pierce, ~28° = it arcs, lands, and bounces once for AoE). It uses a free ball from your pocket (recharges), or a dead ball for bonus damage.
- **Baseball source:** launch angle and exit velocity. The low line drive has the highest exit speed, and a ~26–30° fly ball is the home-run "barrel".
- **Animation/feel:** a short level swing, and the ball leaves with a white streak and a sonic *thwip*. It has a 3-frame hit-stop on the first enemy. The angle choice is shown by a ghost arc on the ground.
- **Scaling/build:** projectile damage and speed, pierce, crit, extra projectiles (a fan of two or three), Chain. The core ranged option of **Projectile Slugger** builds.
- **Synergies:** with **Curveball**/Slider it becomes a bending shot. **Pitching Machine** feeds it free balls. **Double Play** picks up where it ends. The ball is the carrier for **Knuckleball** and **Eephus** (see their notes).

## 3. Infield Fly
- **Type/tags:** Attack, Projectile, AoE, Curse-like Mark, CD 6 s, Sp ⊖ (20 Hype).
- **What it does:** Pops a ball nearly straight up. Up to **three enemies** inside the highlighted cluster are **Called Out**: they take +30% damage, can't dodge or block, and their Strikes jump to 2. When the ball lands it deals a small AoE. If the ball is caught (see **Rally Cap**) you can recast it for free.
- **Baseball source:** the infield fly rule. With runners on first and second and under two outs, a pop-up the infield can catch is an automatic out, whether caught or dropped.
- **Animation/feel:** an upward uppercut swing, then the ball goes up with a whistling ring-out and a white **"IFF"** umpire-arm signal icon over the marked enemies. The ball lands with a soft splat and a puff of chalk. Hit-stop is a slight 3 frames on the pop.
- **Scaling/build:** duration, mark count, area, "increased damage taken". It is a **debuffer** for boss and group damage and a base for **Crit** (Called Out enemies take bonus crit).
- **Synergies:** it is the setup for **Eephus**, **Double Play** and **Grand Slam** (guaranteed hits on marked foes). It builds the Count fast for **Strikeout**.

## 4. Bunt
- **Type/tags:** Attack, Melee, Defence, Projectile-deflect, CD 2 s, no Hype cost.
- **What it does:** A tiny, precise cone. **Hit projectiles with it and they drop dead** at your feet as balls (ammo). If used just before a hit lands (a 0.2 s "perfect" window), it also **cushions** the blow, so that melee attacker is staggered and you lose no balance. It deals low damage but a big stagger, and it **always** gains Hype.
- **Baseball source:** bunting. The bat is held square, you "catch" the ball with soft hands and drop it dead. A sacrifice bunt gives yourself up to advance the runner. A drag bunt is a quiet, quick one.
- **Animation/feel:** the bat swings up horizontally, with a squared-hands pose. The ball makes a soft *thup* and rolls to a stop. Almost no hit-stop (1 frame) but a big visible squash on the enemy. A gold ring marks the perfect timing.
- **Scaling/build:** a **defensive** tool. Scales with cooldown recovery, perfect-window size, block or armour on a perfect bunt, and stagger. The dead-ball count scales **Double Play**.
- **Synergies:** it produces ammo for **Double Play**, **Line Drive** and **Pitching Machine**. A perfect bunt can immediately refund **Check Swing**.

## 5. Check Swing
- **Type/tags:** Attack, Melee, Defence, Mv-lite (cancel), CD 4 s, Gen ⊕ on success.
- **What it does:** The **animation-cancel button**. During any skill's wind-up or recovery you can press it to stop the swing mid-way (a half-swing). That cancel gives 0.4 s of stagger immunity and sets up your **next** attack to start at its load pose (so it comes out 30% faster). If an enemy's attack lands during the half-swing, it is **counter-hit** for a Strike and a stagger.
- **Baseball source:** the checked swing, a swing started and stopped before the wrists roll over. The umpire rules on whether you went around.
- **Animation/feel:** the bat stops abruptly with a *whoosh-stop* (hands freeze, wobble), a small body flinch, and a rubbery vibration. No hit-stop, because it is about control. If it works, the screen shows a quick "NO SWING!" pop-up.
- **Scaling/build:** attack speed, cooldown recovery, counter damage and crit. It makes **animation-cancel builds** good: spending a big swing then cancelling into the next.
- **Synergies:** it cancels **Home Run** hit recovery, **Eephus** wind-up and **Grand Slam** bluffs. **Bunt** can refund it.

## 6. Bat Flip
- **Type/tags:** Attack, Melee, AoE, Taunt, Dur, CD 10 s, Sp ⊖ (30 Hype). Triggers automatically on a crit kill if supported with *Showboat*.
- **What it does:** Toss the bat high with a flourish. Every enemy in range is **Showed Up**: it is taunted and gains **+20% damage taken** while it stares at you. The bat spins in the air for 1.5 s as a **hovering AoE blade** (continuous small damage), and lands in a slam that re-grips your hand. Your Hype and crit chance are boosted while the bat is airborne, but you take a **Beanball** (a single dodgeable fastball from the nearest enemy, "the unwritten rules").
- **Baseball source:** the bat flip, a celebration with a rich unwritten-rules culture (the pitcher may retaliate).
- **Animation/feel:** a slow-motion 0.4 s flip. The camera pushes in on you, the bat turns with a gold trail, and the crowd noise swells. Landing slam has a large 8-frame hit-stop. Sound is a cheering *"ooooh"*.
- **Scaling/build:** area, duration, damage taken, crit, taunt radius. It is the **Showman** (aggro and crowd-control) skill, and converts risk (Beanball) into reward.
- **Synergies:** Showed Up stacks with **Called Out** (Infield Fly) and the **Strikeout** vulnerability. It makes **Rundown** fill faster. With **Home Run Trot** it is a "victory lap" combo.

## 7. Home Run Trot
- **Type/tags:** Movement, AoE, Fire, Dur, CD 12 s, Sp ⊖ (25 Hype).
- **What it does:** A four-leg dash around a **diamond** path (first, second, third, home). At each corner you leave a **Base** (a small burning pad). Touching all four lays a **fire diamond** that burns for 4 s, and you end up back where you started. Each leg is a short unstoppable jog (you can't be stunned), and it *gains a Runner* if all four corners are completed.
- **Baseball source:** the home-run trot, a slow, celebratory lap round the bases after a homer, and the rule that a runner must touch every base in order.
- **Animation/feel:** a casual, cartoon *jog* with exaggerated elbows, plus a trailing flame and a stadium fanfare. Each base is a *stomp*, with 2-frame hit-stop and a puff. The final lap closes with a *whoosh* and a ring of fire. Slow-mo on the home leg.
- **Scaling/build:** Fire damage, area, duration, movement speed, burn / ignite chance. It is a **mobility + Fire** option for **Fire Trot** builds.
- **Synergies:** gives Runners toward **Grand Slam**. Enemies on the diamond are easy targets for **Line Drive** and **Eephus**. **Check Swing** cancels it for early exit.

## 8. Slide
- **Type/tags:** Movement, Attack, Melee, AoE (line), CD 4 s (2 charges), no Hype cost.
- **What it does:** A fast low dash. Choose **feet-first** (a hard trip: enemies in the path are knocked down) or **head-first** (a longer, quicker dive that dodges one projectile and ends with a free Strike). Passing *through* an enemy attack's wind-up grants a Runner (**Stolen Base**).
- **Baseball source:** sliding (feet-first, head-first, hook slide) and stealing bases by timing the pitcher's move.
- **Animation/feel:** a dust-cloud streak with a *shhhhk* skid and a flash of a "SAFE!" umpire pose (arms wide) when you dodge. Hit-stop is 3 frames on a trip.
- **Scaling/build:** movement speed, area, attack damage on slide, charges, cooldown recovery. It is the **mobility** base for most builds.
- **Synergies:** Runner source for **Grand Slam**. It sets up Strikeouts on knocked-down enemies and puts you in range for **Full Swing**.

## 9. Pitching Machine
- **Type/tags:** Spell-like Summon, Totem, Projectile, Dur 12 s, CD 8 s, Sp ⊖ (20 Hype).
- **What it does:** Drops a giant toy **pitching machine** (a wind-up toy on wheels) that fires a ball every 1.2 s at the nearest enemy. Balls bounce harmlessly (small damage), then become **dead balls**. If *you* hit a flying ball with a skill it becomes **Live**: your next attack on it adds that projectile's damage. Supports select the pitch it throws: Fastball, Curve, Slider, Changeup.
- **Baseball source:** batting-practice pitching machines, and the pitch types (each machine "setting" copies a real pitch).
- **Animation/feel:** the machine pops up with a *boing* and a spring, the arm swings, and a ball *fwump*s out with a puff of steam. A visible telegraph shows the ball's path before it fires so you can hit it for a combo. A yellow flash lights when you hit a Live ball.
- **Scaling/build:** totem count, duration, projectile damage, attack speed (rate of fire), Slider/Curve supports. It is the **summon / ammo** engine for **Machine Gunner** builds.
- **Synergies:** gives ammo to **Line Drive**, **Curveball**, **Knuckleball**. **Rundown** and **Infield Fly** hold enemies in the line of fire.

## 10. Curveball
- **Type/tags:** Attack, Projectile, Physical, Sp ⊖ (15 Hype).
- **What it does:** Hits a spinning ball that **bends around** the target, curving 90° and hitting enemies from the **side or behind** for +40% damage ("backstab"). Hold to pick the direction (curveball vs. screwball opposite). It returns in a boomerang arc if it misses.
- **Baseball source:** curveball and slider physics. Spin creates a Magnus force, so topspin / sidespin bends the path, and a screwball curves the opposite way.
- **Animation/feel:** a roll-over swing with a *twist*, and a spiral-spin trail (blue ribbon). A "whoosh-whoosh" doppler sound as it curves. Hit-stop 3 frames.
- **Scaling/build:** projectile damage, curve strength (a support), pierce, crit. A **flanking** build for obstacles and shields.
- **Synergies:** hits enemies hit by **Infield Fly** or **Rundown** from behind for big crits. It stacks Strikes on enemies behind cover. **Pitching Machine** can throw Curve balls to match.

## 11. Knuckleball
- **Type/tags:** Attack, Projectile, Chaos/Physical, Sp ⊖ (10 Hype), CD 1.5 s.
- **What it does:** A slow, nearly spinless ball that **wobbles unpredictably** (random zig-zag) and **cannot be dodged by tracking**. It deals low damage but can hit **many times** (each wobble pass is a hit) and gets +10% damage per hit. Enemies that watch it take a free Strike.
- **Baseball source:** the knuckleball. With no spin, vortices shed behind the ball, so its path is erratic even to the pitcher.
- **Animation/feel:** a gentle push-swing, then a floaty, **flutter** with a flickering shimmer, and a comic *wobble-wobble* sound. 1-frame hit-stop, with soft hits that add up.
- **Scaling/build:** projectile count, duration, hits per pass, ailment chance (chaos: poison-like "Dizzy"). It is a **chaos/ailment** build, a damage-over-time spreader.
- **Synergies:** applies lots of small Strikes for **Strikeout**. Works well with **Rundown** (enemies keep getting hit while stuck) and **Pitching Machine** (many balls).

## 12. Eephus
- **Type/tags:** Attack, Projectile, AoE, Physical, CD 8 s, Sp ⊖ (30 Hype). Delayed.
- **What it does:** Lobs a ball very high. It lands after 1.5 s on a **big red target circle** for a huge hit. If you strike the falling ball again at its peak (timing ring) it drops as a meteor with 2× damage.
- **Baseball source:** the eephus (a ~55 mph blooper). Rip Sewell's lob; Ted Williams hit one for a homer in the 1946 All-Star Game.
- **Animation/feel:** a *slow-motion uppercut*, then a comedic *"bwoooop"* slide-whistle as the ball goes up. A shadow and ring telegraph the landing. Then a *BOOM* with a 10-frame hit-stop and a screen shake.
- **Scaling/build:** area, damage, crit, cooldown recovery, delay-reduction. A **big-hit** skill for bosses and for stationary packs.
- **Synergies:** **Infield Fly**, **Rundown** and **Bat Flip** make enemies stand still on the target. The second hit combos with **Line Drive**.

## 13. Double Play
- **Type/tags:** Attack, Projectile, Chain, Physical, Sp ⊖ (20 Hype). Needs a dead ball.
- **What it does:** Picks up a nearby **dead ball** and throws it at an enemy (the **force out**), then the ball ricochets as a **relay** to a second enemy (the **tag**). Both hit. If both targets are already Struck, it chains a third time (a **Triple Play**).
- **Baseball source:** the double play (two outs on one play), relay throws, and the force play vs. the tag.
- **Animation/feel:** a quick scoop, an over-the-shoulder throw with a *pop*, and a fast ricochet to the second target. Each hit has 3 frames of hit-stop. A catch-and-throw "double" sound effect.
- **Scaling/build:** chain count, projectile damage, ammo (dead balls) recovery, crit. A **chain** build.
- **Synergies:** fed by **Bunt**, **Pitching Machine** and kills. Marks from **Infield Fly** guarantee the chain.

## 14. Rundown ("Pickle")
- **Type/tags:** Spell-like Trap, AoE, Dur 5 s, CD 14 s, Sp ⊖ (25 Hype).
- **What it does:** Place two **gnome fielders** (lawn-gnome minions) at two points. Enemies in the line between them are **trapped in a pickle**: forced to run back and forth, hit by a thrown ball at each end for steady damage, and **slowed** as they scramble. Hit-stop on each bounce.
- **Baseball source:** the rundown (a pickle), where a runner is caught between two bases and the fielders throw until he's tagged.
- **Animation/feel:** two gnome fielders tip their hats, then throw with a *pang!*. The trapped enemy zig-zags with a funny "wheee" sound. Ball trails link the two gnomes. Hit-stop 2 frames each.
- **Scaling/build:** duration, damage per throw, trapped count, area, slow. A **control** skill for the **Trapper** build.
- **Synergies:** pairs with **Eephus** and **Infield Fly**. **Full Swing**'s Home Run knockback pushes enemies in. **Knuckleball** hits the stuck enemies many times.

## 15. Rally Cap
- **Type/tags:** Buff, Aura-like, Defence, Dur 6 s, CD 20 s, Sp ⊖ (all Hype above 30).
- **What it does:** Flip your cap inside out. You gain **life regeneration**, damage reduction, and a stack of **Rally** for each 3 s you're below 50% life. Afterwards the **Seventh-Inning Stretch** pulse heals you and nearby allies for a burst and resets the cooldown of Bunt and Check Swing. Catch a falling ball (e.g. from **Infield Fly**) to refresh it.
- **Baseball source:** the rally cap, a superstition when the team is trailing late, and the seventh-inning stretch (fans stand, stretch and sing).
- **Animation/feel:** the cap turns inside out with a comic *flip-pop*, a glowing silver outline, and a crowd chant. A pulsing "stretch" animation (arms up) with a rising chime. Hit-stop none.
- **Scaling/build:** duration, heal amount, damage reduction, cooldown recovery, "low-life" scaling. It is the **comeback** skill.
- **Synergies:** gives free Check Swing and Bunt for defensive cycles. Pairs with **Bat Flip** for aggro tanking.

## 16. Grand Slam
- **Type/tags:** Attack, Melee, AoE, Fire/Physical, Ultimate, Sp ⊖ (consumes Runners).
- **What it does:** Requires **Bases Loaded** (3 Runners). A massive swing: it deals huge AoE damage and **scores** one "run" for each Runner (+50% damage per Runner). If it kills a boss or rare enemy it's a **Walk-Off**: it explodes into a shower of loot and drops a Rally Cap buff. With fewer Runners it works as a weaker "Sacrifice Fly".
- **Baseball source:** the grand slam (a home run with bases loaded, 4 runs) and the walk-off (a run that ends the game).
- **Animation/feel:** the camera zooms. The three bases light up, you take a massive swing and the screen goes white. A 12-frame hit-stop, a crowd roar, firework confetti, and a "GRAND SLAM!" banner. The screen shakes. Enemies fly out of the field.
- **Scaling/build:** damage, area, crit multiplier, Runner efficiency. The **finisher** of every build.
- **Synergies:** built by **Slide**, **Home Run Trot** and Strikeouts from **Full Swing**/**Infield Fly**. **Check Swing** can cancel the start if the target dies.

---

## Example builds

### A. "Cycle Slugger" (melee crit)
Main: **Full Swing**. Supports: Multistrike, Heavy Swing. Utility: **Check Swing** (cancel), **Slide** (mobility), **Bat Flip** (taunt), **Grand Slam** (finisher).
Loop: Full Swing combo → Cycle bonus → cancel into the next with Check Swing → build Strikeouts → Grand Slam. Scaling: attack speed, crit, melee.

### B. "Machine Gunner" (projectile / chain)
Main: **Line Drive** + **Pitching Machine** + **Double Play**. Utility: **Bunt** (ammo and defence), **Curveball** (flanking), **Infield Fly** (mark).
Loop: place the machines, bunt dead balls, mark with Infield Fly, chain Double Plays. Scaling: projectile damage, chain, extra projectiles.

### C. "Fire Trapper" (control / Fire)
Main: **Home Run Trot** (fire diamond) + **Rundown** + **Eephus**. Utility: **Knuckleball** (spread ailments), **Rally Cap** (sustain), **Slide**.
Loop: Rundown holds enemies on the burning diamond, Eephus lands on them, Knuckleball adds ailments, Rally Cap heals. Scaling: Fire, area, duration, ignite.
