# Enemies

## Overview

All enemies are stored in the same `m_blupi[]` array as Blupi characters,
identified by the `perso` field. Enemy AI runs through the same GOAL_* interpreter
as player characters, with dedicated goal tables in `decgoal.cpp`.

---

## Spider (perso=1, Araignée)

**Behaviour**: Active hunter. Pathfinds toward Blupi. On contact, poisons Blupi
(`bMalade=TRUE`), which drains energy faster.

**Special ability**: Can jump over obstacles (`ACTION_A_SAUT`).

**Weaknesses**: Electro ray (`ACTION_A_GRILLE`), dynamite (`ACTION_A_POISON`).

**Death sequence**: `ACTION_A_MORT1` → `ACTION_A_MORT2` → `ACTION_A_MORT3` → `BlupiDelete()`

**Target search**: `SearchSpiderObject(rank, initCel, distMax, foundCel, foundIcon)`
finds the nearest Blupi or building to attack within `distMax` cells.

**Sounds**: `SOUND_A_SAUT` (jump), `SOUND_A_HIHI` (attack laugh), `SOUND_A_POISON` (when poisoned)

---

## Virus (perso=2)

**Behaviour**: Slow spreader. Moves to adjacent objects and corrupts / destroys them.
Does not directly attack Blupi but can destroy buildings, resources, and infrastructure.

**Special ability**: Spreads autonomously to neighbouring cells.

**Weaknesses**: Electro ray, dynamite.

**Sounds**: `SOUND_VIRUS` (spreading)

---

## Tracks / Tank (perso=3)

**Behaviour**: Heavy crusher. Follows a path and crushes anything in the way
(objects, buildings, Blupi). Cannot be stopped by palisades or walls.

**Special ability**: Crushes objects (`ACTION_T_ECRASE`).

**Sounds**: `SOUND_T_MOTEUR` (engine), `SOUND_T_ECRASE` (crushing)

**Target search**: `SearchTracksObject(rank, initCel, distMax, foundCel, foundIcon)`

---

## Robot (perso=4)

**Behaviour**: Most intelligent enemy. Has multiple capabilities:
- Builds and mines like Blupi
- Fires a ray beam at Blupi
- Can recharge its energy

**Actions**: Stop, walk, flatten, build, delay, recharge, crush

**Sounds**: `SOUND_R_MOTEUR` (motor), `SOUND_R_APLAT` (flatten), `SOUND_R_ROTATE` (rotate),
`SOUND_R_CHARGE` (recharge)

**Target search**: `SearchRobotObject(rank, initCel, distMax, foundCel, foundIcon, foundAction)`
— returns both the target cell and the action to perform.

**Robot goal tables**: `WM_ACTION_R_BUILD1`–`R_BUILD6`, `WM_ACTION_R_MAKE1`–`R_MAKE6`

---

## Bomb (perso=5, Bombe)

**Behaviour**: Autonomous seeker. Hops (`ACTION_B_MARCHE`) toward Blupi.
Detonates on contact, creating a large explosion that destroys surrounding objects and Blupi.

**Sounds**: `SOUND_B_SAUT` (hopping)

**Target search**: `SearchBombeObject(rank, initCel, distMax, foundCel, foundIcon)`

---

## Mine Detonator (perso=6, Détonateur)

**Behaviour**: Invisible passive entity. Exists only to trigger a mine explosion
when a triggering condition is met (e.g. enemy walks onto the mine's cell).

**Action**: Only `ACTION_D_DELAY` (600) — just waits.

**Notes**: Created by `GOAL_AMORCE` when a mine is primed.

---

## Electro Tower (perso=7, Électro)

**Behaviour**: Stationary. Rotates to track Blupi in range and fires electric rays.
The ray is drawn as an animated `Move` element using `GOAL_ELECTRO`.

**Actions**:
- `ACTION_E_STOP` (700) — idle
- `ACTION_E_MARCHE` (701) — rotating / tracking
- `ACTION_E_DEBUT` (702) — powering on
- `ACTION_E_RAYON` (703) — firing ray

**Sounds**: `SOUND_E_RAYON` (ray fire), `SOUND_E_TOURNE` (rotation),
`SOUND_RAYON1` (start), `SOUND_RAYON2` (sustained)

**Target search**: `SearchElectroObject(rank, initCel, distMax, foundCel, foundIcon)`

**Ray animation**: `CDecor::BlupiStartStopRayon(rank, startCel, endCel)` creates
a Move element that draws the electric ray beam between tower and target.

**WM_ACTION_E_RAYON** (+116) handles the firing sequence.

---

## Disciple (perso=8, Robot2)

**Behaviour**: Friendly helper. Can perform almost all Blupi tasks autonomously:
build, chop, mine, pick flowers, water, dig, use dynamite.

**Action range**: `ACTION_D_STOP` (800) through `ACTION_D_BECHE` (810)

**Sounds**: Uses a distinct voice set:
- `SOUND_D_BOING` (52) — acknowledgement
- `SOUND_D_OK` (53) — confirms command
- `SOUND_D_GO` (54) — starts moving
- `SOUND_D_TERM` (55) — finishes task

**Creation**: `WM_ACTION_FABDISC` → `GOAL_NEWPERSO` with perso=8

**Notes**: The disciple cannot board vehicles. It uses the same GOAL_* tables as Blupi
for most tasks, but with `ACTION_D_*` animation actions instead of `ACTION_*`.
