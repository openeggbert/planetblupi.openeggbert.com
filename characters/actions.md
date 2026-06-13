# Animation Actions (ACTION_*)

All action codes are defined in `include/def.h`.
They control the sprite frame sequence played by `Action()` in `action.cpp`.

A character's current animation is stored in `Blupi.action`.
The current direction is `Blupi.aDirect` (a `DIRECT_*` value).

---

## Blupi (perso=0) Actions

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_STOP` | 0 | Standing still |
| `ACTION_STOPf` | 1 | Standing still (tired variant) |
| `ACTION_MARCHE` | 2 | Walking |
| `ACTION_MARCHEf` | 3 | Walking (tired variant) |
| `ACTION_BUILD` | 4 | Building / constructing |
| `ACTION_PIOCHE` | 5 | Mining / digging (pickaxe) |
| `ACTION_ENERGY` | 6 | Collecting energy (eating/drinking) |
| `ACTION_TAKE` | 8 | Picking up object and putting it on head |
| `ACTION_DEPOSE` | 9 | Putting down the carried object |
| `ACTION_SCIE` | 10 | Sawing wood |
| `ACTION_BRULE` | 11 | On fire (burning to death) |
| `ACTION_TCHAO` | 12 | Vanishing / dying (disappear animation) |
| `ACTION_MANGE` | 13 | Eating |
| `ACTION_NAISSANCE` | 14 | Being born (hatching from egg) |
| `ACTION_SAUTE2` | 15 | Jumping over obstacle (phase 2 of 4) |
| `ACTION_SAUTE3` | 16 | Jumping over obstacle (phase 3) |
| `ACTION_SAUTE4` | 17 | Jumping over obstacle (phase 4) |
| `ACTION_SAUTE5` | 18 | Jumping over obstacle (phase 5) |
| `ACTION_PONT` | 19 | Pushing a bridge segment |
| `ACTION_MISC1` | 20 | Idle animation: shrugging |
| `ACTION_MISC2` | 21 | Idle animation: scratching |
| `ACTION_MISC3` | 22 | Idle animation: yo-yo |
| `ACTION_MISC1f` | 23 | Idle (tired): bof-bof |
| `ACTION_GLISSE` | 24 | Sliding on ice |
| `ACTION_BOIT` | 25 | Drinking a potion |
| `ACTION_LABO` | 26 | Working in the laboratory |
| `ACTION_DYNAMITE` | 27 | Setting off dynamite |
| `ACTION_DELAY` | 28 | Waiting one frame |
| `ACTION_CUEILLE1` | 29 | Picking flowers (phase 1) |
| `ACTION_CUEILLE2` | 30 | Picking flowers (phase 2) |
| `ACTION_MECHE` | 31 | Covering ears (waiting for explosion) |
| `ACTION_STOPb` | 32 | Standing still in a boat |
| `ACTION_MARCHEb` | 33 | Moving in a boat |
| `ACTION_STOPj` | 34 | Standing still in a jeep |
| `ACTION_MARCHEj` | 35 | Moving in a jeep |
| `ACTION_ELECTRO` | 36 | Being electrocuted |
| `ACTION_GRILLE1` | 37 | Being electro-grilled (phase 1) |
| `ACTION_GRILLE2` | 38 | Being electro-grilled (phase 2) |
| `ACTION_GRILLE3` | 39 | Being electro-grilled (phase 3) |
| `ACTION_MISC4` | 40 | Idle: closing eyes |
| `ACTION_CONTENT` | 41 | Happy dance (mission success) |
| `ACTION_ARROSE` | 42 | Watering plants |
| `ACTION_BECHE` | 43 | Digging with a spade |
| `ACTION_CUEILLE3` | 44 | Picking flowers (phase 3) |
| `ACTION_BUILDBREF` | 45 | Building (brief variant) |
| `ACTION_BUILDSEC` | 46 | Building (dry/stone variant) |
| `ACTION_BUILDSOURD` | 47 | Building (muffled variant) |
| `ACTION_BUILDPIERRE` | 48 | Building (rock variant) |
| `ACTION_PIOCHEPIERRE` | 49 | Mining (stone/rock variant) |
| `ACTION_PIOCHESOURD` | 50 | Mining (muffled variant) |
| `ACTION_MISC5` | 51 | Idle: waving / calling |
| `ACTION_TELEPORTE1` | 52 | Teleporter animation (phase 1) |
| `ACTION_TELEPORTE2` | 53 | Teleporter animation (phase 2) |
| `ACTION_TELEPORTE3` | 54 | Teleporter animation (phase 3) |
| `ACTION_STOPa` | 55 | Standing still in armour |
| `ACTION_MARCHEa` | 56 | Walking in armour |
| `ACTION_ARMUREOPEN` | 57 | Armour opening (entering) |
| `ACTION_ARMURECLOSE` | 58 | Armour closing (exiting) |
| `ACTION_SAUTE1` | 59 | Jumping into a jeep (phase 1) |
| `ACTION_MISC6` | 60 | Idle: diabolo trick |

---

## Spider (perso=1) Actions — `ACTION_A_*`

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_A_STOP` | 100 | Standing still |
| `ACTION_A_MARCHE` | 101 | Walking |
| `ACTION_A_SAUT` | 102 | Jumping over an obstacle |
| `ACTION_A_GRILLE` | 103 | Being hit by an electro ray |
| `ACTION_A_POISON` | 105 | Being poisoned (hit by dynamite) |
| `ACTION_A_MORT1` | 106 | Death animation (phase 1) |
| `ACTION_A_MORT2` | 107 | Death animation (phase 2) |
| `ACTION_A_MORT3` | 108 | Death animation (phase 3) |

---

## Virus (perso=2) Actions — `ACTION_V_*`

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_V_STOP` | 200 | Standing still |
| `ACTION_V_MARCHE` | 201 | Walking / spreading |
| `ACTION_V_GRILLE` | 202 | Being hit by an electro ray |

---

## Tracks / Tank (perso=3) Actions — `ACTION_T_*`

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_T_STOP` | 300 | Standing still |
| `ACTION_T_MARCHE` | 301 | Moving (tracks rolling) |
| `ACTION_T_ECRASE` | 302 | Crushing an object |

---

## Robot (perso=4) Actions — `ACTION_R_*`

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_R_STOP` | 400 | Standing still |
| `ACTION_R_MARCHE` | 401 | Walking |
| `ACTION_R_APLAT` | 402 | Flattening / squashing |
| `ACTION_R_BUILD` | 403 | Building / working |
| `ACTION_R_DELAY` | 404 | Waiting (build delay) |
| `ACTION_R_CHARGE` | 405 | Recharging |
| `ACTION_R_ECRASE` | 406 | Crushing an object |

---

## Bomb (perso=5) Actions — `ACTION_B_*`

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_B_STOP` | 500 | Standing still |
| `ACTION_B_MARCHE` | 501 | Hopping / bouncing |

---

## Mine Detonator (perso=6) Actions — `ACTION_D_DELAY`

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_D_DELAY` | 600 | Waiting (invisible, passive) |

---

## Electro Tower (perso=7) Actions — `ACTION_E_*`

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_E_STOP` | 700 | Idle (not firing) |
| `ACTION_E_MARCHE` | 701 | Rotating / tracking target |
| `ACTION_E_DEBUT` | 702 | Starting up / powering on |
| `ACTION_E_RAYON` | 703 | Firing electric ray |

---

## Disciple / Robot2 (perso=8) Actions — `ACTION_D_*`

| Constant | Code | Description |
|----------|------|-------------|
| `ACTION_D_STOP` | 800 | Standing still |
| `ACTION_D_MARCHE` | 801 | Walking |
| `ACTION_D_BUILD` | 802 | Building / constructing |
| `ACTION_D_PIOCHE` | 803 | Mining |
| `ACTION_D_SCIE` | 804 | Sawing wood |
| `ACTION_D_TCHAO` | 805 | Disappearing / dying |
| `ACTION_D_CUEILLE1` | 806 | Picking flowers (phase 1) |
| `ACTION_D_CUEILLE2` | 807 | Picking flowers (phase 2) |
| `ACTION_D_MECHE` | 808 | Covering ears (dynamite) |
| `ACTION_D_ARROSE` | 809 | Watering plants |
| `ACTION_D_BECHE` | 810 | Digging with spade |

---

## How Action() Works (action.cpp)

`CDecor::Action()` is called each tick for each character.

For each `action + aDirect` combination, it looks up:
- A table of sprite icons (from `CHBLUPI` channel) for each animation frame
- The animation phase duration (how many ticks per frame)
- Which sounds to play and when

It advances `Blupi.phase` and updates `Blupi.icon` to the next frame.
When the animation completes, `BlupiNextAction()` is called to transition
to the next state (typically idle `ACTION_STOP` or next GOAL step).
