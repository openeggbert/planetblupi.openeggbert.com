# Task Interpreter (GOAL_*)

## Overview

High-level multi-step tasks are encoded as sequences of **GOAL_* opcodes**
stored in static tables in `src/decgoal.cpp`.
The interpreter in `CDecor::GoalNextOp()` executes one opcode per game tick.

Each task (WM_ACTION_*) maps to a table of GOAL_* opcodes via `GetTableGoal()`.

---

## How the Interpreter Works

```
1. Player clicks → WM_ACTION_* message sent
2. CEvent::EventButton() → BlupiGoal(cel, button)
3. GoalStart(rank, action, cel) → sets goalAction, goalPhase=0, goalCel
4. Each tick: BlupiNextGoal(rank) → GoalNextOp(rank, pTable)
5. GoalNextOp reads next opcode from table:
   - Executes it immediately if possible
   - Or waits for a prerequisite (animation finish, cell free, etc.)
6. When GOAL_TERM is reached → character becomes idle
```

---

## GOAL_* Opcode Reference

Defined in `include/decgoal.h`. Parameter counts in `table_goal_nbop[]`.

| Opcode | Code | Param count | Parameters | Description |
|--------|------|-------------|-----------|-------------|
| `GOAL_TERM` | 0 | 0 | — | End of goal sequence |
| `GOAL_GOHILI` | 1 | 3 | dx,dy, bPass | Move to highlighted cell (relative offset) |
| `GOAL_GOHILI2` | 2 | 3 | dx,dy, bPass | Move to highlighted cell (alternative variant) |
| `GOAL_GOBLUPI` | 3 | 3 | dx,dy, bPass | Move character to cell (absolute from goalCel) |
| `GOAL_PUTFLOOR` | 4 | 4 | dx,dy, ch,icon | Place a floor tile at cell |
| `GOAL_PUTOBJECT` | 5 | 4 | dx,dy, ch,icon | Place an object tile at cell |
| `GOAL_BUILDFLOOR` | 6 | 9 | dx,dy, ch,i, mch,mi, total,delai,step | Animate floor construction (Move element) |
| `GOAL_BUILDOBJECT` | 7 | 9 | dx,dy, ch,i, mch,mi, total,delai,step | Animate object construction (Move element) |
| `GOAL_ACTION` | 8 | 2 | action, direction | Play an animation action |
| `GOAL_INTERRUPT` | 9 | 1 | level | Set interrupt priority (0=highest, interrupts ongoing actions) |
| `GOAL_ENERGY` | 10 | 1 | minimum | Require minimum energy to proceed |
| `GOAL_ADDMOVES` | 11 | 3 | dx,dy, rank | Add movement animation to decoration table |
| `GOAL_OTHER` | 12 | 6 | ch,f1,l1, f2,l2, action | Execute action on a nearby matching object |
| `GOAL_FINISHMOVE` | 13 | 0 | — | Wait for Move animation to finish |
| `GOAL_TAKE` | 14 | 2 | dx,dy | Pick up the object at cell (dx,dy) |
| `GOAL_DEPOSE` | 15 | 0 | — | Put down the currently carried object |
| `GOAL_GROUP` | 16 | 1 | nb | Group action: next nb opcodes apply to multiple Blupi |
| `GOAL_WORK` | 17 | 2 | dx,dy | Mark cell (dx,dy) as current workspace |
| `GOAL_TESTOBJECT` | 18 | 4 | dx,dy, ch,icon | Test if object at cell matches channel+icon |
| `GOAL_FIX` | 19 | 2 | dx,dy | Set fixed reference point (for bridge/cultivate) |
| `GOAL_OTHERFIX` | 20 | 6 | ch,f1,l1, f2,l2, action | Like GOAL_OTHER but relative to fix point |
| `GOAL_ADDICONS` | 21 | 3 | dx,dy, rank | Add icon sequence animation to decoration |
| `GOAL_NEWBLUPI` | 22 | 2 | dx,dy | Create a new Blupi at cell (dx,dy) |
| `GOAL_SOUND` | 23 | 1 | sound | Play SOUND_* effect |
| `GOAL_REPEAT` | 24 | 1 | bool | Enable (1) or disable (0) action repeating |
| `GOAL_OTHERLOOP` | 25 | 1 | action | Loop action until a target matching `action` is found |
| `GOAL_NEXTLOOP` | 26 | 0 | — | Advance the loop counter |
| `GOAL_ARRANGEOBJECT` | 27 | 2 | dx,dy | Call ArrangeObject at cell (for auto-tiling after build) |
| `GOAL_LABO` | 28 | 0 | — | Laboratory work step |
| `GOAL_CACHE` | 29 | 2 | bool, bDynamite | Hide (1) or show (0) the Blupi sprite |
| `GOAL_DELETE` | 30 | 0 | — | Delete this character |
| `GOAL_ELECTRO` | 31 | 3 | dx,dy, rank | Fire an electro ray from Blupi toward cell |
| `GOAL_NEWPERSO` | 32 | 3 | dx,dy, perso | Spawn a new entity (enemy or ally) at cell |
| `GOAL_USINEBUILD` | 33 | 2 | dx,dy | Factory build step (IsUsineBuild check) |
| `GOAL_USINEFREE` | 34 | 2 | dx,dy | Factory free step (IsUsineFree check) |
| `GOAL_EXPLOSE1` | 35 | 2 | dx,dy | Explosion animation — phase 1 |
| `GOAL_EXPLOSE2` | 36 | 2 | dx,dy | Explosion animation — phase 2 |
| `GOAL_VEHICULE` | 37 | 1 | type | Enter (type>0) or exit (type=0) a vehicle |
| `GOAL_TAKEOBJECT` | 38 | 4 | dx,dy, ch,icon | Pick up a specific object (channel+icon) at cell |
| `GOAL_FLOORJUMP` | 39 | 3 | ch,icon, action | Branch based on floor type at current cell |
| `GOAL_ADDDRAPEAU` | 40 | 2 | dx,dy | Add a flag (waypoint) to the path list |
| `GOAL_AMORCE` | 41 | 2 | dx,dy | Prime mine detonator at cell |
| `GOAL_MALADE` | 42 | 1 | bMalade | Set sick / poisoned state (1=sick, 0=recover) |
| `GOAL_IFTERM` | 43 | 2 | dx,dy | Conditional: skip next opcode if at target cell |
| `GOAL_IFDEBARQUE` | 44 | 2 | dx,dy | Conditional: skip if disembarking |
| `GOAL_ISNOMALADE` | 45 | 0 | — | Assert: character must not be sick to proceed |
| `GOAL_SKIPSKILL` | 46 | 2 | skill,d | Skip d opcodes if current skill level matches |
| `GOAL_TELEPORTE` | 47 | 2 | dx,dy | Teleport Blupi to partner teleporter |
| `GOAL_ACTUALISE` | 48 | 0 | — | Refresh character sprite (BlupiActualise) |
| `GOAL_WAITFREE` | 49 | 2 | dx,dy | Wait until target cell is free (not occupied) |

---

## WM_ACTION_* to Goal Table Mapping

Each `WM_ACTION_*` message corresponds to a named goal table in `decgoal.cpp`.
`GetTableGoal(action)` returns a pointer to the opcode table.

| WM_ACTION_* | Value (WM_USER+) | Goal table | Description |
|-------------|-----------------|-----------|-------------|
| `WM_ACTION_GO` | +30 | `table_goal_go` | Move Blupi to target cell |
| `WM_ACTION_ABAT1` | +31 | `table_goal_abat1` | Chop tree (with replant) |
| `WM_ACTION_ABAT2` | +32 | `table_goal_abat2` | Chop tree variant |
| `WM_ACTION_ABAT3` | +33 | `table_goal_abat3` | Chop tree variant |
| `WM_ACTION_ABAT4` | +34 | `table_goal_abat4` | Chop tree variant |
| `WM_ACTION_ABAT5` | +35 | `table_goal_abat5` | Chop tree (no replant) |
| `WM_ACTION_ABAT6` | +36 | `table_goal_abat6` | Chop tree variant |
| `WM_ACTION_BUILD1` | +37 | `table_goal_build1` | Build construction type 1 (hut) |
| `WM_ACTION_BUILD2` | +38 | `table_goal_build2` | Build construction type 2 (laboratory) |
| `WM_ACTION_BUILD3` | +39 | `table_goal_build3` | Build construction type 3 (factory) |
| `WM_ACTION_BUILD4` | +40 | `table_goal_build4` | Build construction type 4 (incubator) |
| `WM_ACTION_BUILD5` | +41 | `table_goal_build5` | Build construction type 5 |
| `WM_ACTION_BUILD6` | +42 | `table_goal_build6` | Build construction type 6 |
| `WM_ACTION_STOP` | +43 | `table_goal_stop` | Stop character |
| `WM_ACTION_CARRY` | +44 | `table_goal_carry` | Pick up object |
| `WM_ACTION_DEPOSE` | +45 | `table_goal_depose` | Put down object |
| `WM_ACTION_ROC1` | +46 | `table_goal_roc1` | Mine rock (variant 1) |
| `WM_ACTION_ROC2` | +47 | `table_goal_roc2` | Mine rock (variant 2) |
| `WM_ACTION_ROC3` | +48 | `table_goal_roc3` | Mine rock (variant 3) |
| `WM_ACTION_ROC4` | +49 | `table_goal_roc4` | Mine rock (variant 4) |
| `WM_ACTION_ROC5` | +50 | `table_goal_roc5` | Mine rock (variant 5) |
| `WM_ACTION_ROC6` | +51 | `table_goal_roc6` | Mine rock (variant 6) |
| `WM_ACTION_ROC7` | +52 | `table_goal_roc7` | Mine rock (variant 7) |
| `WM_ACTION_MUR` | +53 | `table_goal_mur` | Build wall |
| `WM_ACTION_CULTIVE` | +54 | `table_goal_cultive` | Cultivate / tend crops |
| `WM_ACTION_CULTIVE2` | +55 | `table_goal_cultive2` | Cultivate variant |
| `WM_ACTION_MANGE` | +56 | `table_goal_mange` | Eat food |
| `WM_ACTION_MAKE` | +57 | `table_goal_make` | Generic make/craft |
| `WM_ACTION_BUILD` | +58 | `table_goal_build` | Generic build |
| `WM_ACTION_PALIS` | +59 | `table_goal_palis` | Build palisade / fence |
| `WM_ACTION_NEWBLUPI` | +60 | `table_goal_newblupi` | Hatch a new Blupi from egg |
| `WM_ACTION_PONTE` | +61 | `table_goal_ponte` | Build bridge (east) |
| `WM_ACTION_PONTS` | +62 | `table_goal_ponts` | Build bridge (south) |
| `WM_ACTION_PONTO` | +63 | `table_goal_ponto` | Build bridge (west) |
| `WM_ACTION_PONTN` | +64 | `table_goal_pontn` | Build bridge (north) |
| `WM_ACTION_PONTEL` | +65 | `table_goal_pontel` | Build bridge (east, long) |
| `WM_ACTION_PONTSL` | +66 | `table_goal_pontsl` | Build bridge (south, long) |
| `WM_ACTION_PONTOL` | +67 | `table_goal_pontol` | Build bridge (west, long) |
| `WM_ACTION_PONTNL` | +68 | `table_goal_pontnl` | Build bridge (north, long) |
| `WM_ACTION_TOUR` | +69 | `table_goal_tour` | Build watchtower |
| `WM_ACTION_CARRY2` | +70 | `table_goal_carry2` | Pick up object (variant 2) |
| `WM_ACTION_DEPOSE2` | +71 | `table_goal_depose2` | Put down object (variant 2) |
| `WM_ACTION_MANGE2` | +72 | `table_goal_mange2` | Eat (variant 2) |
| `WM_ACTION_BOIT` | +73 | `table_goal_boit` | Drink potion |
| `WM_ACTION_BOIT2` | +74 | `table_goal_boit2` | Drink variant 2 |
| `WM_ACTION_LABO` | +75 | `table_goal_labo` | Use laboratory |
| `WM_ACTION_FLEUR1` | +76 | `table_goal_fleur1` | Pick flowers (variant 1) |
| `WM_ACTION_FLEUR2` | +77 | `table_goal_fleur2` | Pick flowers (variant 2) |
| `WM_ACTION_DYNAMITE` | +78 | `table_goal_dynamite` | Place and detonate dynamite |
| `WM_ACTION_DYNAMITE2` | +79 | `table_goal_dynamite2` | Dynamite variant 2 |
| `WM_ACTION_T_DYNAMITE` | +80 | `table_goal_t_dynamite` | Tracks dynamite |
| `WM_ACTION_FLEUR3` | +81 | `table_goal_fleur3` | Pick flowers (variant 3) |
| `WM_ACTION_R_BUILD1`–`R_BUILD6` | +82–+90 | robot build tables | Robot building actions |
| `WM_ACTION_R_MAKE1`–`R_MAKE6` | +86–+91 | robot make tables | Robot manufacturing |
| `WM_ACTION_BATEAUE` | +92 | `table_goal_bateaue` | Boat: move east |
| `WM_ACTION_BATEAUS` | +93 | `table_goal_bateaus` | Boat: move south |
| `WM_ACTION_BATEAUO` | +94 | `table_goal_bateauo` | Boat: move west |
| `WM_ACTION_BATEAUN` | +95 | `table_goal_bateaun` | Boat: move north |
| `WM_ACTION_BATEAUDE` | +96 | boat disembark east | Disembark east |
| `WM_ACTION_BATEAUDS` | +97 | boat disembark south | Disembark south |
| `WM_ACTION_BATEAUDO` | +98 | boat disembark west | Disembark west |
| `WM_ACTION_BATEAUDN` | +99 | boat disembark north | Disembark north |
| `WM_ACTION_BATEAUAE` | +100 | boat embark east | Embark east |
| `WM_ACTION_BATEAUAS` | +101 | boat embark south | Embark south |
| `WM_ACTION_BATEAUAO` | +102 | boat embark west | Embark west |
| `WM_ACTION_BATEAUAN` | +103 | boat embark north | Embark north |
| `WM_ACTION_MJEEP` | +104 | `table_goal_mjeep` | Board jeep |
| `WM_ACTION_DJEEP` | +105 | `table_goal_djeep` | Disembark from jeep |
| `WM_ACTION_DRAPEAU` | +106 | `table_goal_drapeau` | Place a flag (waypoint) |
| `WM_ACTION_DRAPEAU2` | +107 | `table_goal_drapeau2` | Flag variant 2 |
| `WM_ACTION_DRAPEAU3` | +108 | `table_goal_drapeau3` | Flag variant 3 |
| `WM_ACTION_EXTRAIT` | +109 | `table_goal_extrait` | Extract iron ore |
| `WM_ACTION_FABJEEP` | +110 | `table_goal_fabjeep` | Manufacture a jeep |
| `WM_ACTION_FABMINE` | +111 | `table_goal_fabmine` | Manufacture a mine |
| `WM_ACTION_MINE` | +112 | `table_goal_mine` | Detonate mine |
| `WM_ACTION_MINE2` | +113 | `table_goal_mine2` | Mine variant 2 |
| `WM_ACTION_E_RAYON` | +116 | `table_goal_e_rayon` | Electro tower fire ray |
| `WM_ACTION_ELECTRO` | +117 | `table_goal_electro` | Blupi electrocuted |
| `WM_ACTION_ELECTROm` | +118 | `table_goal_electrom` | Electro mine |
| `WM_ACTION_GRILLE` | +119 | `table_goal_grille` | Electro grill effect |
| `WM_ACTION_MAISON` | +120 | `table_goal_maison` | Go home (into hut) |
| `WM_ACTION_FABDISC` | +121 | `table_goal_fabdisc` | Create a disciple |
| `WM_ACTION_A_MORT` | +122 | `table_goal_a_mort` | Spider death |
| `WM_ACTION_REPEAT` | +123 | `table_goal_repeat` | Repeat last action |
| `WM_ACTION_TELEPORTE00`–`11` | +124–+127 | teleporter tables | Teleport sequences |
| `WM_ACTION_FABARMURE` | +128 | `table_goal_fabarmure` | Manufacture armour |
| `WM_ACTION_MARMURE` | +129 | `table_goal_marmure` | Enter armour |
| `WM_ACTION_DARMURE` | +130 | `table_goal_darmure` | Exit armour |

---

## Example Goal Sequence: `table_goal_go`

```cpp
static short table_goal_go[] =
{
    WM_ACTION_GO,          // header: action this table serves
        GOAL_GOHILI, 0,0, FALSE,   // move to highlighted cell (+0,+0)
        GOAL_TERM,         // done
    0                      // sentinel
};
```

## Example Goal Sequence: `table_goal_maison` (Go Home)

```cpp
static short table_goal_maison[] =
{
    WM_ACTION_MAISON,
        GOAL_GOHILI2, +1,+1, FALSE,           // move to cell adjacent to hut
        GOAL_ACTION,  ACTION_STOP, DIRECT_E,  // face east
        GOAL_ACTION,  ACTION_CONTENT, DIRECT_E, // happy dance
        GOAL_TERM,
    0
};
```

## Example Goal Sequence: `table_goal_abat1` (Chop Tree)

```cpp
static short table_goal_abat1[] =
{
    WM_ACTION_ABAT1,
        GOAL_ENERGY,     MAXENERGY/4,           // require 25% energy
        GOAL_GOHILI2,    0,+1, TRUE,             // move adjacent to tree
        GOAL_GROUP,      4,                      // group of 4 opcodes:
         GOAL_TESTOBJECT, 0,-1, CHOBJECT,6,      //   test: tree is there
         GOAL_INTERRUPT,  0,                     //   set high priority
         GOAL_WORK,       0,-1,                  //   claim workspace
         GOAL_BUILDOBJECT,0,-1, CHOBJECT,30, -1,-1, DIMOBJY+20,1,-1*100, // animate
        GOAL_ACTION,     ACTION_STOP, DIRECT_E,
        GOAL_ADDMOVES,   0,-1, 1,                // add falling animation
        GOAL_ACTION,     ACTION_PIOCHESOURD, DIRECT_E,
        GOAL_GOBLUPI,    0,-1, TRUE,             // move to tree position
        GOAL_ACTION,     ACTION_STOP, DIRECT_E,
        GOAL_ADDMOVES,   0,0, 1,
    ... (continues with sawing and log placement)
        GOAL_TERM,
    0
};
```
