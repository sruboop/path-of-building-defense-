# RESEARCH.md — raw material for the 16 inspiration pairs

Research only; no skills designed. Each section has (a) a paper finding with its mechanism, (b) a game skill with why it is fun, (c) links.
Confidence notes: details come from search-result summaries and abstracts, not full-text reads. Items marked (unverified) were not confirmed against a primary source.

---

## 1. Non-Newtonian fluids (oobleck) × Souls-like

**(a) Paper.** Waitukaitis & Jaeger, "Impact-activated solidification of dense suspensions via dynamic jamming fronts", *Nature* 487, 205–209 (2012).
- Finding: Hit a cornstarch-and-water mix with a rod and a solid-like front starts right under the impact point and grows downward. Stresses reached were about 100× the biggest shear stresses seen before. The authors say the old "shear thickening" explanation needs revisiting.
- Mechanism: The impact creates a moving jamming front. Liquid ahead of it gets converted to jammed solid as the front passes ("it essentially grows its own solid as it propagates"). The solid exists only while the front is moving and is built out of the liquid itself.
- Follow-up: Peters, Majumdar & Jaeger, *Nature* 2016, directly observed "dynamic shear jamming", distinct from ordinary shear thickening.

**(b) Game skill.** *Sekiro: Shadows Die Twice* — Deflect and the Posture system.
- How it works: Tap Guard just before a hit lands. The window is about 30 frames by default and shrinks to about 7 if you recently released Guard (fan-wiki figures, may be version-specific). A mistimed press is only a normal block. A successful deflect negates the damage, fills the enemy's Posture gauge a lot, and briefly staggers them. A quick counter-slash adds more Posture damage. Filling Posture opens a Deathblow that kills most enemies whatever HP they have left. Bosses need their Posture emptied once per health bar.
- Why it's fun: Attacking and defending are the same act. Being aggressive-but-precise is rewarded and mashing is punished. The metal-on-metal spark and the clang give instant feedback, and the Posture bar gives a second, visible win condition.

**Links:** https://news.uchicago.edu/story/messy-experiment-cleans-physics-mystery-cornstarch · https://research-explorer.ista.ac.at/record/113 · https://sekiroshadowsdietwice.wiki.fextralife.com/Deflection · https://sekiroshadowsdietwice.wiki.fextralife.com/Posture · https://www.pushsquare.com/news/2019/03/guide_sekiro_shadows_die_twice_combat_-_posture_deflections_shinobi_prosthetic_and_stealth

---

## 2. Plant electrical signalling × Survival horror

**(a) Paper.** Böhm, Scherzer, Krol, Hedrich et al., "The Venus Flytrap *Dionaea muscipula* Counts Prey-Induced Action Potentials to Induce Sodium Uptake", *Current Biology* 26, 286–295 (2016).
- Finding: The trap counts touches. One touch of a trigger hair primes it, and a second within about 20 seconds snaps it shut. More touches (about 3 and up) switch on digestive enzyme production, and about 5+ switch on nutrient uptake (sodium transporters). The trap is effectively a tally counter that scales its response with the number of signals.
- Mechanism: Each hair touch fires an action potential carried by a calcium wave across the whole trap. Calcium accumulates and decays over seconds, so the plant "counts" by crossing calcium thresholds. This stops it wasting energy on a raindrop or a non-nutritious prey.
- Follow-up: A Würzburg 2023 release describes a mutant that cannot count its impulses.

**(b) Game skill.** *Alan Wake* — flashlight burns away the Taken's darkness shield.
- How it works: Enemies are shielded by darkness and are immune to bullets until it is burned off. Aim the flashlight at them and a circle shrinks as the shield weakens, which is the on-screen readout. Hold the boost to burn faster, spending battery. Then shoot. Stronger darkness can regrow over time. In *American Nightmare* only boosted light breaks shields.
- Why it's fun: It splits combat into two beats, expose then punish. The tool you use for navigation is also your armour-piercing step. Battery and boost create a risk/reward tension, and the shrinking ring gives readable progress.

**Links:** https://opus.bibliothek.uni-wuerzburg.de/files/12805/Boehm_Current_Biology.pdf · https://www.scientificamerican.com/blog/artful-amoeba/the-venus-flytrap-can-count-past-2 · https://www.sci.news/biology/carnivorous-venus-flytraps-can-count-03586.html · https://en.wikipedia.org/wiki/Alan_Wake · https://alanwake.fandom.com/wiki/Fadeouts

---

## 3. Echolocation in bats × Physics puzzle game

**(a) Paper.** Ghose & Moss, "The sonar beam pattern of a flying bat as it tracks tethered insects", *J. Acoust. Soc. Am.* (2003); Ghose, Horiuchi & Moss (2007) on the two-lobed beam; Ghose's UMD dissertation, "Sonar Beam Direction and Flight Control in an Echolocating Bat".
- Finding: A flying big brown bat points its sonar beam at the target to within about 3°, a kind of "acoustic gaze", and locks on one target even when two are present. The dissertation reports that during pursuit the bat holds the absolute direction to the target roughly constant, which minimizes time-to-intercept against erratic prey, and that beam direction is coupled to turn rate with a delay. The beam has two vertical lobes in flight.
- Mechanism: The bat aims the beam by head movement and uses it as a steered sensor. A pursuit rule ("keep the bearing constant", like a navy interception) is combined with a switch between "looking around" and "homing in" modes (reported in a 2006 *J. Neurosci.* news item). Exact title and year of that last paper were not confirmed.

**(b) Game skill.** *Portal* — momentum flinging.
- How it works: Fall into a portal and you leave the exit portal at the speed you gained, in the exit's facing direction. Drop into a floor portal from height and exit sideways to cross a gap. A "wedge fling" puts the exit on an upward slope for more range. A "double fling" is used when there's no deep pit. In the first game you can still airstrafe a bit, and in Portal 2 there is little to no air control.
- Why it's fun: One simple rule ("speed is conserved through the portal") lets the player invent routes the designer never listed. The payoff is the feel of a big arc through the air.

**Links:** https://pmc.ncbi.nlm.nih.gov/articles/PMC3384009 · https://drum.lib.umd.edu/handle/1903/3397 · https://cnsmaryland.org/2006/02/17/common-sense-bats-see-like-humans-umd-study-finds · https://theportalwiki.com/wiki/Flinging · https://developer.valvesoftware.com/wiki/Fling_(Portal_2) · https://primagames.com/eguides/portal-eguide/essentials/gameplay/portal-science

---

## 4. Tardigrade survival × Immersive sim

**(a) Paper.** Boothby, Tapia, Brozena, ... Goldstein, "Tardigrades Use Intrinsically Disordered Proteins to Survive Desiccation", *Molecular Cell* 65(6), 975–984 (2017).
- Finding: Tardigrade-specific disordered proteins (TDPs) are needed for drying survival and, put into yeast and bacteria, add tolerance. Press coverage says survival rose about 100-fold in those hosts (unverified against the paper).
- Mechanism: Tardigrades don't build a rigid shell. As water leaves, the floppy proteins fill in for it and set into a non-crystalline glass (vitrification) around the cell contents. That glass stops proteins from unfolding and membranes from fusing, and the better a protein vitrifies the better it protects. Add water and the glass dissolves and the animal wakes.
- Also: Dsup ("damage suppressor", *Ramazzottius varieornatus*, Univ. of Tokyo). Human cells made to express it had about half the X-ray DNA damage. A UCSD follow-up found one part binds DNA and another forms a protective shield. Primary citations not retrieved.

**(b) Game skill.** *Prey* (2017) — GLOO Cannon.
- How it works: It fires a foam that hardens on contact and deals no damage. It slows or fully freezes Typhon (a Mimic freezes in a few shots, a Phantom takes many). Frozen enemies take bonus damage, especially from the Wrench. Foam can be fired onto walls to build climbable stairs and platforms, and it also puts out fires and temporarily stops electric arcs.
- Why it's fun: One tool does crowd control, a combat combo setup, traversal and an environment fix. The player decides in the moment which use applies. It is a classic immersive-sim "yes, and" tool. Range is short early on and upgrades widen it.

**Links:** https://iris.unimo.it/handle/11380/1129511 · https://www.u-tokyo.ac.jp/focus/en/articles/a_00518.html · https://www.genomebc.ca/blog/one-protein-protects-tardigrade-dna-from-damage/ · https://ceramics.org/ceramic-tech-today/saved-by-glass-tardigrades-use-biological-vitrification-to-survive-complete-desiccation/ · https://prey.fandom.com/wiki/GLOO_Cannon · https://www.gamepressure.com/prey/gloo-cannon/z59bdf

---

## 5. Cellular automata × Stealth game

**(a) Paper.** Mordvintsev, Randazzo, Niklasson, Levin, "Growing Neural Cellular Automata", *Distill* (2020). Also Bert Wang-Chak Chan, "Lenia — Biology of Artificial Life", *Complex Systems* 28(3), 2019 (arXiv 1812.05433).
- Finding: Every cell runs the same tiny learned rule and sees only its neighbours' 16-value state (4 colour channels, 12 hidden). From a single seed cell the grid grows a target picture (the lizard emoji) and, if trained with damage, regrows it when part is erased.
- Mechanism: Local-only update, repeated, trained end-to-end by comparing the final image to the target. Hidden channels act like chemical signals telling cells where they are. Self-repair emerges because the rule is "move toward the target", not "reach the target by a fixed script".
- Lenia: A continuous-state, continuous-space automaton with smooth kernels. It produced over 400 species in 18 families of "creatures" that move, split and bounce.

**(b) Game skill.** *Hitman* (World of Assassination) — disguises and Enforcers.
- How it works: Take a worker's outfit and most NPCs of that role treat you as one of them. Only "Enforcers", who know that outfit's real wearers, can see through the disguise, and they are marked with a dot or triangle (visible with Instinct). Security heads can see through all disguises. Some areas are restricted to certain outfits. Fan wiki; exact markers vary by source.
- Why it's fun: Stealth becomes a puzzle of identity: whom you look like, who can read you, and where you can walk. Each Enforcer is a soft, readable threat you can plan around, lure and remove.

**Links:** https://arxiv.org/abs/1812.05433 · https://www.complex-systems.com/abstracts/v28_i03_a01/ · https://arxiv.org/pdf/2103.08737 · https://hitman.fandom.com/wiki/Disguise · https://www.trueachievements.com/game/HITMAN/walkthrough/2
(Note: the Distill article itself was not opened; summary comes from follow-up papers. Search for "Growing Neural Cellular Automata distill.pub" to cite.)

---

## 6. Starling murmurations × Fighting game

**(a) Paper.** Ballerini et al. (12 authors), "Interaction ruling animal collective behavior depends on topological rather than metric distance: Evidence from a field study", *PNAS* 105, 1232–1237 (2008).
- Finding: From 3D reconstruction of real flocks, each starling reacts to about 6–7 nearest neighbours, no matter how far away those are. It's not "everyone within X metres".
- Mechanism: Reacting to a fixed count of neighbours keeps the flock cohesive when density changes (e.g. when a falcon compresses or stretches it), because a metric radius would suddenly include far more or far fewer birds. Turn information then passes bird to bird in waves.

**(b) Game skill.** *Guilty Gear -Strive-* — Roman Cancel.
- How it works: Press three attack buttons together, costing 50% of the Tension bar. It cancels the move you are doing and releases a shockwave that slows nearby opponents. Red (on hit) pops the foe up slowly so you can extend combos, and the explosion counts as a hit for damage scaling. Purple (on whiff or recovery) wipes out the end of a move. Yellow (in blockstun) is defensive. Per sources, a dedicated shortcut button exists in settings.
- Why it's fun: A single resource spend lets you break your own commitment, so it rewards creative improvisation. Each of three colours has a clear read for you and the opponent, and the time-slowing flash gives a strong hit-stop style cue.

**Links:** https://web3.arxiv.org/abs/0709.1916 · https://en.wikipedia.org/wiki/Flocking · https://www.nationalgeographic.com/photography/article/starling-birds-flock-cloud · https://www.gfinityesports.com/guilty-gear-strive/how-to-roman-cancel-in-guilty-gear-strive/ · https://compete.playstation.com/en-us/article/roman-cancel-types-guilty-gear-strive-guide · https://www.arcsystemworks.jp/guiltygear/db/en/volume2.php

---

## 7. Tensegrity structures × City builder

**(a) Paper.** Ingber, "Tensegrity I. Cell structure and hierarchical systems biology", *J. Cell Science* 116 (2003); Ingber's 1993 cellular tensegrity model. Robot side: Surovik, Bruce, Wang, Vespignani, Bekris, "Any-axis Tensegrity Rolling via Bootstrapped Learning and Symmetry Reduction", ISER 2018 (NASA SUPERball line).
- Finding: Cells hold their shape like a tensegrity: a network of cables (actin filaments) under pre-existing tension, with microtubules acting as the compressed struts. Experiments (traction force microscopy) showed microtubules bear compression and add to the cytoskeletal prestress. Measured cell mechanics matched tensegrity predictions.
- Mechanism: Pre-stress. Tension in the cables is balanced by compression in isolated struts, so the whole thing is stiff for its weight, and a push on one point is shared across the whole network. In robots the same property means they survive drops and roll by changing cable lengths (a 2025 robot preprint reports a gait climbing 28° slopes, unverified).
- Also relevant: it is a "stress-supported" structure, so it fails if the tension is lost.

**(b) Game skill.** *Frostpunk* — Book of Laws with Hope and Discontent.
- How it works: Two separate bars (both can be full or both empty). Hope falls or Discontent rises too far for too long and you are exiled or the city revolts. A new law can be passed about every 18 in-game hours. Productivity laws (child labour, 24-hour shifts) raise Discontent. Healthcare or entertainment laws raise Hope. Faith and Order trees are mutually exclusive. Ignored problems escalate into protests. You can push to totalitarian extremes, where the system stops mattering.
- Why it's fun: Each law is a real moral trade-off with a visible meter cost, and the choices are permanent. Pressure is spread over a whole society.

**Links:** https://pmc.ncbi.nlm.nih.gov/articles/PMC2614693 · https://resolve.cambridge.org/core/books/cytoskeletal-mechanics/models-of-cytoskeletal-mechanics-based-on-tensegrity/6BE47F20CE96A5CA26FE6D59E3D11C53 · https://pracsys.cs.rutgers.edu/?p=428 · https://arxiv.org/pdf/2501.15078 · https://en.wikipedia.org/wiki/Frostpunk · https://www.pcgamer.com/au/frostpunk-developers-on-hope-misery-and-the-ultimately-terrifying-book-of-laws

---

## 8. Archerfish spitting × Roguelike deckbuilder

**(a) Paper.** Vailati, Zinnato & Cerbino, "How Archer Fish Achieve a Powerful Impact: Hydrodynamic Instability of a Pulsed Jet in *Toxotes jaculatrix*", *PLoS ONE* 7(10): e47867 (2012). Related: Gerullis & Schuster, *Current Biology* (2014), mouth-opening control of water speed (details not confirmed).
- Finding: The impact is stronger than the fish's own muscles can produce. The fish spits a jet whose speed rises during the spit, so the tail of the jet is faster than the head.
- Mechanism: The faster back part catches the slower front part and feeds its water and momentum into the head, which grows into a big drop that hits with far more force. It is an instability in the jet, using physics outside the body. The 2014 work links the speed change to split-second changes in mouth opening.

**(b) Game skill.** *Slay the Spire* (Defect) — Orbs: channel, passive, evoke.
- How it works: The Defect has Orb slots. Each channeled Orb gives a passive effect at end of turn and a stronger one when evoked (by a card, or when a new Orb pushes the rightmost one out of full slots). Original-game values: Lightning 3 passive/8 evoke damage to a random enemy; Frost 2/5 Block; Dark builds +6 per turn and evokes that stored total on the lowest-HP enemy; Plasma 1 energy at start of turn/2 energy on evoke. Focus raises passive and evoke values (not Plasma).
- Why it's fun: Orbs are a queue that trade slow value for a big immediate payoff, and the player chooses when to cash in. Cards that use the queue in odd ways create combos you build across a run.

**Links:** https://www.koreatimes.co.kr/amp/business/tech-science/20121026/fish-shoots-down-prey-with-super-powered-jet · https://www.scientificamerican.com/blog/observations/fish-shoots-down-prey-with-super-powered-jet-video · https://m.phys.org/news/2013-12-uncover-amazing-physics-feat-archerfish.html · https://www.sciencenews.org/article/archerfish-mouth-secret-precision-spit · https://www.highgroundgaming.com/slay-the-spire-defect-guide-tips-builds/ · https://www.pcgamesn.com/slay-the-spire-2/defect

---

## 9. Hummingbird torpor × Trading card game

**(a) Paper.** Shankar, Schroeder, Wethington, Graham & Powers, "Hummingbird torpor in context: duration, more than temperature, is the key to nighttime energy savings" (bioRxiv 2018; later *J. Exp. Biol.* version, 2020, not confirmed in search).
- Finding: 43 wild-caught birds from 8 species. Torpor happened in warm tropical and cool temperate sites, and chance of entering it was barely linked to night temperature. Saving per hour in torpor was 65–92% when air was near the bird's minimum body temperature. But total nightly energy depended most on how long the bout lasted, not how deep it was. Duration tracked photoperiod (night length). The smallest species, black-chinned (about 2.9 g), mostly went into deep torpor.
- Mechanism: A bird spends the night on a slow-burn fuel budget. Rather than only getting colder, it drops its metabolism and stays down as long as it can, then wakes to feed. Deep vs shallow torpor is a dial, but time spent down is the bigger lever.
- Context: Older work (Powers 1991) looked at nocturnal fat use in Anna's and Costa's hummingbirds.

**(b) Game skill.** *Hearthstone* — Discover.
- How it works: The card shows you three options and you pick one to add to your hand (or per its text, summon etc.). Options come from a neutral or your-class pool and the card's own restrictions apply. Introduced in League of Explorers (2015). Developers reduced the class-card weighting to increase variety (still-current status not confirmed).
- Why it's fun: A tiny decision with real agency inside a random effect. It reduces bad luck and lets players adapt to the board state, and each Discover is a small "which one?" puzzle.

**Links:** https://www.biorxiv.org/content/10.1101/383679.full.pdf · https://www.americanscientist.org/node/4906 · https://datadryad.org/dataset/doi:10.5061/dryad.t4b8gthzh · https://hearthstone.wiki.gg/wiki/Discover · https://outof.cards/hearthstone/cards/keywords/discover · https://invenglobal.com/articles/9055/hearthstones-discover-mechanic-is-receiving-a-fundamental-change

---

## 10. Lévy flight foraging × Battle royale

**(a) Paper.** Humphries et al., "Environmental context explains Lévy and Brownian movement patterns of marine predators", *Nature* 465 (2010). Also Humphries et al., *PNAS* (2012) on albatrosses ("Foraging success of biological Lévy flights recorded in situ").
- Finding: Across 14 open-ocean predator species (sharks, tuna, billfish, sunfish), movement fit Lévy patterns: many short hops with rare very long jumps. Individuals switched between Lévy and Brownian (ordinary random walk) depending on habitat: Lévy in sparse, less productive water, Brownian in rich shelf and front areas. For wandering albatrosses, prey caught during Lévy movement was nearly four times their daily energy need.
- Mechanism: When food is sparse and you can't see it, mostly-local search with occasional long relocations avoids re-covering the same ground. In rich patches, plain wandering is enough. The classic theory is Viswanathan et al., *Nature* 1999 (not opened in search). The authors note statistical-fitting controversy over how to detect Lévy behaviour.

**(b) Game skill.** *Fortnite* — the Storm (shrinking safe zone).
- How it works: A circle on the map marks where the safe zone will shrink to. The current zone holds for a wait time and then shrinks over a shrink time. Players outside take damage, and later phases hit harder with shorter waits. Storm Surge in competitive modes adds 25 damage every 5 seconds to stop storm-camping. Moving storms exist in some modes. Timings get retuned often (recent 2026 hotfix numbers from news items; check the current patch notes).
- Why it's fun: It forces players to relocate and meet each other. The pace is scripted yet readable, so every match has the same tension arc: loot, roam, converge.

**Links:** https://eprints.soton.ac.uk/340115/ · https://plymsea.ac.uk/id/eprint/6189/ · https://acap.aq/news/news-archive/2012-news-archive/levy-flight-movements-are-shown-to-help-wandering-and-black-browed-albatrosses-find-food-at-sea · https://fortnite-archive.fandom.com/wiki/The_Storm_(Battle_Royale) · https://www.techradar.com/gaming/consoles-pc/fortnites-storm-circles-are-getting-nerfed-because-theyre-too-fast

---

## 11. Slime mould network growth × Puzzle platformer

**(a) Paper.** Tero, Takagi, Saigusa, Ito, Bebber, Fricker, Yumiki, Kobayashi & Nakagaki, "Rules for Biologically Inspired Adaptive Network Design", *Science* 327, 439–442 (22 Jan 2010).
- Finding: *Physarum polycephalum* grown on a map with oat flakes at the major Greater Tokyo cities built a tube network comparable to the real rail system in efficiency, fault tolerance and cost. Light was used as a barrier to stand in for mountains and lakes.
- Mechanism: A decentralised feedback rule. It starts as a dense mesh, tubes that carry more flow thicken, and unused ones shrink and vanish. There is no planner. Tuning the model trades off cost, transport efficiency and resilience.

**(b) Game skill.** *Braid* — time rewind.
- How it works: The player can rewind time at will, even after dying. Each world changes the rule: in one, some objects ignore your time manipulation; in another, time moves forward when you go right and backward when you go left. Reviews note some puzzles need pixel-precise timing.
- Why it's fun: Death has no cost, so there's no fear in trying. It also turns every level into a "what if I redo that?" puzzle, and the world-by-world rule twist gives a new idea each time.

**Links:** https://pubmed.ncbi.nlm.nih.gov/20093467/ · https://ir.lib.hiroshima-u.ac.jp/00029243 · https://www.nationalgeographic.com/science/article/slime-mould-attacks-simulates-tokyo-rail-network · https://www.discovermagazine.com/technology/slime-mould-attacks-simulates-tokyo-rail-network · https://en.wikipedia.org/wiki/Braid_(video_game) · https://giantbomb.com/reviews/braid-review

---

## 12. Gravitational lensing × Sandbox crafting game

**(a) Paper.** Kelly et al., Supernova Refsdal discovery (*Science* 2015, "Multiple images of a highly magnified supernova formed by an early-type cluster galaxy lens"; title/year not confirmed in search), and the follow-up Kelly et al., "Déjà Vu All Over Again: The Reappearance of Supernova Refsdal", *ApJ Letters* 819, L8 (2016; arXiv 1512.04654).
- Finding: In Nov 2014 Hubble saw one distant supernova (redshift 1.49) as four copies in an Einstein-cross arrangement around an elliptical galaxy in cluster MACS J1149.5+2223 (z = 0.54). Lens models predicted a fifth image in a different image of the host galaxy within about a year. On 11 Dec 2015 Hubble found it at the predicted spot, the first supernova whose time and place were predicted in advance. Only some models got the timing and brightness right, which exposes systematic errors in lens models.
- Mechanism: Mass bends light, and the cluster's lumpy mass (plus one galaxy) makes light take different-length paths, so copies arrive at different times. This gives a built-in time delay that can be modelled and tested.
- Other items found: microlensing exoplanets (first in 2004 by MOA/OGLE; over 200 found by end of 2023) and Einstein rings.

**(b) Game skill.** *Minecraft* — Elytra with firework rockets.
- How it works: Glide with elytra, then use a firework rocket to be pushed in the direction you're facing. Boosted level flight is about 33.5 blocks/s per a third-party calculator, and every rocket reaches that speed. Higher flight duration only holds it longer. Boost length is about 10×(2+duration) ticks. Crafting: 1 paper + 1–3 gunpowder gives 3 rockets of duration 1–3. The best fan numbers are from a calculator citing the wiki; verify.
- Why it's fun: Crafted consumables become mobility, and the player steers the arc by pitching up and down. It makes the whole map feel smaller and gives a clear goal-to-gear loop.

**Links:** https://arxiv.org/abs/1512.04654v2 · https://www.astronomy.com/science/hubble-captures-first-ever-predicted-exploding-star/ · https://physicsworld.com/a/gravitational-lensing-brings-extrasolar-planets-into-focus/ · https://minecraft.fandom.com/wiki/Firework_Rocket · https://www.minecraftmaps.com/tools/elytra-flight-calculator

---

## 13. Superfluid helium × Pinball

**(a) Paper.** Gomez, Bostedt et al., "Shapes and vorticities of superfluid helium nanodroplets", *Science* (2014; SLAC X-ray laser). Also Guo's group (FAMU-FSU), *Nature Communications* (July 2023) on vortex rings.
- Finding: X-ray images of spinning helium nanodroplets showed a regular 3D grid of quantised vortices (quantum tornadoes). About 1% took unexpected wheel-like shapes. Christoph Bostedt called it surprising. The 2023 study tracked vortex rings with solidified deuterium tracer particles and found only the self-consistent two-way (S2W) model reproduces their motion.
- Mechanism: Superfluid helium has zero viscosity and rotates only in fixed whirls with set circulation (quantised vortices), not like a normal spinning fluid. Spinning it makes many identical tiny vortices arranged in a lattice instead of one smooth swirl.
- Related, from general sources: the Rollin film, a very thin film that climbs the inside of a container and drips off the outside, due to no viscosity plus van der Waals attraction to the wall.
- Authors of the 2014 paper are not confirmed by the search results; cite from the SLAC release.

**(b) Game skill.** Real pinball — Nudge/Tilt and Ball Save (and locked-ball multiball).
- How it works: You can nudge the table to steer the ball. A tilt bob (a weighted pendulum) detects excess movement. Two or three warnings stop the flippers and a full tilt forfeits end-of-ball bonuses. Skilled players use slap saves. Ball save returns a drained ball for a short window after launch, after objectives, or at multiball start. Multiball often needs three locks, then releases more balls and turns the lock hole into a jackpot.
- Why it's fun: The player has a tiny hidden second control that pushes against a hard rule, and the penalty is dramatic and legible. A saved ball feels like a rescue.

**Links:** https://www6.slac.stanford.edu/news/2014-08-21-x-ray-laser-probes-tiny-quantum-tornadoes-superfluid-droplets · https://phys.org/news/2014-08-x-ray-laser-probes-tiny-quantum.html · https://news.fsu.edu/news/science-technology/2023/07/17/famu-fsu-researchers-confirm-theory-for-superfluid-helium/ · https://phys.libretexts.org/Courses/Prince_Georges_Community_College/General_Physics_I:_Classical_Mechanics/52:_Fluid_Dynamics/52.11:_Superfluids · https://www.flippers.be/basics/101_tilt.html · https://tiltforums.com/t/do-tight-tilts-make-you-a-better-player/3230

---

## 14. Acoustic metamaterials × Farming sim

**(a) Paper.** Fang, Xi, Xu, Ambati, Srituravanich, Sun & Zhang, "Ultrasonic metamaterials with negative modulus", *Nature Materials* 5(6), 452–456 (2006).
- Finding: A waveguide loaded with an array of tiny Helmholtz resonators acts as if its bulk modulus is negative near resonance, so sound there can't propagate. It was, per Fang, discovered "entirely accidentally". Fang and Xiang Zhang got the 2025 Brillouin Medal for it. A related line: Mei et al., *Nature Communications* 2012, "dark" acoustic metamaterials that absorb low-frequency sound.
- Mechanism: The structure, not the material, sets the behaviour. Each resonator is a small cavity plus a neck with its own acoustic "inductance" and "capacitance", and near its resonant frequency it pushes back against the wave out of phase. Because it's sub-wavelength, the whole array behaves like a new material. Combine negative density and negative modulus for double-negative behaviour.
- Other cited: Cummer & Schurig (2007) on acoustic cloaking; Cheng et al. (2008) multilayer cloak.

**(b) Game skill.** *Stardew Valley* — Sprinklers.
- How it works: Basic sprinklers water the four adjacent tiles. Quality sprinklers water the eight surrounding tiles (3×3). Iridium sprinklers water a 5×5 area (24 tiles). Only tilled soil is watered. Pressure nozzles enlarge the pattern. Players lay out crops around a pattern, and a fan guide's spacing advice is ambiguous, so check in game.
- Why it's fun: A fixed-shape area effect that you tile like a puzzle; getting the layout efficient is a satisfying spatial optimisation, and the reward (no more daily watering) is immediate.

**Links:** https://arxiv.org/pdf/0812.2952 · https://mech.hku.hk/?p=29066 · https://www.esa.int/gsp/ACT/doc/EVENTS/acoustic_workshop/ACT-PRE-0914-valencia-review_acoustic_metamaterial.pdf · https://www.pocketgamer.com/stardew-valley/sprinker-layouts · https://west-games.com/stardew-valley-sprinkler-layout-calculator/ · https://steamcommunity.com/app/413150/discussions/0/2806204039995872725

---

## 15. Origami engineering / deployable structures × Rhythm game

**(a) Paper.** Filipov, Tachi & Paulino, "Origami tubes assembled into stiff, yet reconfigurable structures and metamaterials", *PNAS* 112 (2015); commentary by Reis, Brau & Terwagne? — the search returned "Reis, Pedro Miguel, Transforming architectures with origami, PNAS 2015" (authors/title partly unconfirmed; the PDF is on the EPFL flexlab site).
- Finding: Miura-ori is a flat sheet that folds with one degree of freedom, but alone it is floppy. Two neighbouring Miura tubes zipped together in a zig-zag arrangement stay remarkably stiff and still deploy with just one degree of freedom, because they resist bending and twisting. Examples: a model bridge and a deployable canopy.
- Mechanism: The panels in the zipper constrain each other, so the shape-changing motion is allowed but every other motion is blocked. Other found work: Miura sheets are multistable and can snap between states while deploying, so rigid-folding models miss part of the dynamics; slits can be added to non-rigid patterns to make them rigid-foldable.
- Note: Filipov et al.'s authors/year come from my memory of the cited work and the search gave only the Reis commentary. Verify before citing.

**(b) Game skill.** *Crypt of the NecroDancer* — move on the beat, Groove Chain.
- How it works: You can only act on the beat. Each kill without missing a beat adds to the Groove Chain, which multiplies gold dropped. Missing a beat resets the multiplier to 1 and may let an adjacent monster hit you. Skipping a beat is allowed but costs the bonus. Coins buy items and are the score, and some items scale with the multiplier. The Bard removes the beat rule.
- Why it's fun: Everything the player does is on the music's tempo, so play becomes a dance. A visible chain makes each clean step feel worth keeping.

**Links:** https://pmc.ncbi.nlm.nih.gov/articles/PMC4603457 · https://www.epfl.ch/labs/flexlab/wp-content/uploads/2017/12/55_2015_Reis_PNAS_TransformingArchitecturesOrigami.pdf · https://dspace.mit.edu/handle/1721.1/102098 · https://en.wikipedia.org/wiki/Crypt_of_the_NecroDancer · https://crypt-of-the-necrodancer.fandom.com/wiki/File:NecrodancerUI.png

---

## 16. Ant colony foraging × Tactics RPG

**(a) Paper.** Pagliara, Gordon & Leonard, "Regulation of harvester ant foraging as a closed-loop excitable system", *PLoS Computational Biology* (2018). Related: Pinter-Wollman et al., *Animal Behaviour* (2013), on interactions regulating forager activation.
- Finding: Harvester ants decide to leave on a foraging trip based on how often they bump antennae with returning foragers, not on any message. Departure rate is linked to recent contacts, and ants leaving to forage had more interactions than ants returning to the deeper nest. The colony adjusts its foraging to food supply without any ant knowing the big picture.
- Mechanism: Closed-loop feedback with excitable-system dynamics: more food means more returning foragers, more contacts, and more departures. A refractory period keeps it stable. Gordon's review argues that the interaction rate, not the content, shapes task choice.
- Not found: Reid & Latty's (2011) trail-network paper for Argentine ants; the search missed it.

**(b) Game skill.** *Final Fantasy Tactics* — Charge Time (CT) turn order.
- How it works: Each tick every unit's CT increases by its Speed. At 100 or more it can act, and after acting its CT resets and its clock restarts. Faster units act more often over the whole fight, and the displayed turn list lets you plan two or three turns ahead. Haste/Slow, Mime and Ramza specifics were not retrieved.
- Why it's fun: Turn order is a resource and a puzzle. Because you can see who acts next, stat choices matter and a big slow spell has a clear timing risk.

**Links:** https://naomi.princeton.edu/wp-content/uploads/sites/744/2021/11/PagGorLeoPLoS_CB2018.pdf · https://pinterwollmanlab.eeb.ucla.edu/wp-content/uploads/sites/86/2016/05/Pinter-Wollman-et-al-2013-AB.pdf · https://cdn.aaai.org/ocs/2471/2471-10789-1-PB.pdf · https://StrategyWiki.org/wiki/Final_Fantasy_Tactics/Gameplay · https://geekchamp.com/?p=779025
