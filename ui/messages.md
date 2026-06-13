# Windows Messages (WM_*)

All custom Windows messages are defined as `WM_USER+N` offsets in `include/def.h`.

---

## WM_UPDATE

| Constant | Value | Description |
|----------|-------|-------------|
| `WM_UPDATE` | WM_USER+1 | Force redraw of the game window |

---

## WM_DECOR* — Decoration Messages

| Constant | Value | Description |
|----------|-------|-------------|
| `WM_DECOR1` | WM_USER+20 | Decoration event 1 |
| `WM_DECOR2` | WM_USER+21 | Decoration event 2 |
| `WM_DECOR3` | WM_USER+22 | Decoration event 3 |
| `WM_DECOR4` | WM_USER+23 | Decoration event 4 |
| `WM_DECOR5` | WM_USER+24 | Decoration event 5 |

---

## WM_ACTION_* — Character Action Messages

These are sent by `CEvent` to `CDecor` to trigger specific goal sequences.
Each maps to a named table in `decgoal.cpp` via `GetTableGoal()`.

| Constant | Value | Description |
|----------|-------|-------------|
| `WM_ACTION_GO` | WM_USER+30 | Move to target cell |
| `WM_ACTION_ABAT1`–`ABAT6` | +31–+36 | Chop tree (6 variants) |
| `WM_ACTION_BUILD1`–`BUILD6` | +37–+42 | Build construction types 1–6 |
| `WM_ACTION_STOP` | +43 | Stop character |
| `WM_ACTION_CARRY` | +44 | Pick up object |
| `WM_ACTION_DEPOSE` | +45 | Put down object |
| `WM_ACTION_ROC1`–`ROC7` | +46–+52 | Mine rock (7 variants) |
| `WM_ACTION_MUR` | +53 | Build wall |
| `WM_ACTION_CULTIVE` | +54 | Cultivate |
| `WM_ACTION_CULTIVE2` | +55 | Cultivate variant 2 |
| `WM_ACTION_MANGE` | +56 | Eat food |
| `WM_ACTION_MAKE` | +57 | Generic make |
| `WM_ACTION_BUILD` | +58 | Generic build |
| `WM_ACTION_PALIS` | +59 | Build palisade |
| `WM_ACTION_NEWBLUPI` | +60 | Hatch new Blupi |
| `WM_ACTION_PONTE` | +61 | Build bridge (east) |
| `WM_ACTION_PONTS` | +62 | Build bridge (south) |
| `WM_ACTION_PONTO` | +63 | Build bridge (west) |
| `WM_ACTION_PONTN` | +64 | Build bridge (north) |
| `WM_ACTION_PONTEL` | +65 | Build bridge (east, long) |
| `WM_ACTION_PONTSL` | +66 | Build bridge (south, long) |
| `WM_ACTION_PONTOL` | +67 | Build bridge (west, long) |
| `WM_ACTION_PONTNL` | +68 | Build bridge (north, long) |
| `WM_ACTION_TOUR` | +69 | Build watchtower |
| `WM_ACTION_CARRY2` | +70 | Pick up object (variant 2) |
| `WM_ACTION_DEPOSE2` | +71 | Put down object (variant 2) |
| `WM_ACTION_MANGE2` | +72 | Eat (variant 2) |
| `WM_ACTION_BOIT` | +73 | Drink potion |
| `WM_ACTION_BOIT2` | +74 | Drink (variant 2) |
| `WM_ACTION_LABO` | +75 | Use laboratory |
| `WM_ACTION_FLEUR1` | +76 | Pick flowers (1) |
| `WM_ACTION_FLEUR2` | +77 | Pick flowers (2) |
| `WM_ACTION_DYNAMITE` | +78 | Place / detonate dynamite |
| `WM_ACTION_DYNAMITE2` | +79 | Dynamite (variant 2) |
| `WM_ACTION_T_DYNAMITE` | +80 | Tracks dynamite |
| `WM_ACTION_FLEUR3` | +81 | Pick flowers (3) |
| `WM_ACTION_R_BUILD1`–`R_BUILD6` | +82,+84,+86,+88,+90,+114 | Robot build 1–6 |
| `WM_ACTION_R_MAKE1`–`R_MAKE6` | +83,+85,+87,+89,+91,+115 | Robot make 1–6 |
| `WM_ACTION_BATEAUE` | +92 | Boat move east |
| `WM_ACTION_BATEAUS` | +93 | Boat move south |
| `WM_ACTION_BATEAUO` | +94 | Boat move west |
| `WM_ACTION_BATEAUN` | +95 | Boat move north |
| `WM_ACTION_BATEAUDE` | +96 | Boat disembark east |
| `WM_ACTION_BATEAUDS` | +97 | Boat disembark south |
| `WM_ACTION_BATEAUDO` | +98 | Boat disembark west |
| `WM_ACTION_BATEAUDN` | +99 | Boat disembark north |
| `WM_ACTION_BATEAUAE` | +100 | Boat embark east |
| `WM_ACTION_BATEAUAS` | +101 | Boat embark south |
| `WM_ACTION_BATEAUAO` | +102 | Boat embark west |
| `WM_ACTION_BATEAUAN` | +103 | Boat embark north |
| `WM_ACTION_MJEEP` | +104 | Board jeep |
| `WM_ACTION_DJEEP` | +105 | Disembark jeep |
| `WM_ACTION_DRAPEAU` | +106 | Place flag (1) |
| `WM_ACTION_DRAPEAU2` | +107 | Place flag (2) |
| `WM_ACTION_DRAPEAU3` | +108 | Place flag (3) |
| `WM_ACTION_EXTRAIT` | +109 | Extract iron ore |
| `WM_ACTION_FABJEEP` | +110 | Manufacture jeep |
| `WM_ACTION_FABMINE` | +111 | Manufacture mine |
| `WM_ACTION_MINE` | +112 | Trigger mine |
| `WM_ACTION_MINE2` | +113 | Mine variant 2 |
| `WM_ACTION_E_RAYON` | +116 | Electro tower fire ray |
| `WM_ACTION_ELECTRO` | +117 | Blupi electrocuted |
| `WM_ACTION_ELECTROm` | +118 | Electro mine |
| `WM_ACTION_GRILLE` | +119 | Electro grill effect |
| `WM_ACTION_MAISON` | +120 | Go home |
| `WM_ACTION_FABDISC` | +121 | Create disciple |
| `WM_ACTION_A_MORT` | +122 | Spider death |
| `WM_ACTION_REPEAT` | +123 | Repeat last action |
| `WM_ACTION_TELEPORTE00` | +124 | Teleport (variant 00) |
| `WM_ACTION_TELEPORTE10` | +125 | Teleport (variant 10) |
| `WM_ACTION_TELEPORTE01` | +126 | Teleport (variant 01) |
| `WM_ACTION_TELEPORTE11` | +127 | Teleport (variant 11) |
| `WM_ACTION_FABARMURE` | +128 | Manufacture armour |
| `WM_ACTION_MARMURE` | +129 | Enter armour |
| `WM_ACTION_DARMURE` | +130 | Exit armour |

---

## WM_BUTTON* — Toolbar Button Messages

| Range | Values | Description |
|-------|--------|-------------|
| `WM_BUTTON0`–`WM_BUTTON39` | WM_USER+200 – WM_USER+239 | Toolbar button 0–39 clicked |

---

## WM_READ* / WM_WRITE* — Save/Load Slot Messages

| Range | Values | Description |
|-------|--------|-------------|
| `WM_READ0`–`WM_READ9` | WM_USER+300 – WM_USER+309 | Load game slot 0–9 |
| `WM_WRITE0`–`WM_WRITE9` | WM_USER+310 – WM_USER+319 | Save game slot 0–9 |

---

## WM_PHASE_* — Phase Transition Messages

See [Game Phases](../engine/game-phases.md) for the complete list.
Range: `WM_USER+500` through `WM_USER+537`.

---

## WM_PREV / WM_NEXT / WM_MOVIE

| Constant | Value | Description |
|----------|-------|-------------|
| `WM_PREV` | WM_USER+600 | Navigate previous |
| `WM_NEXT` | WM_USER+601 | Navigate next |
| `WM_MOVIE` | WM_USER+602 | Start movie |
