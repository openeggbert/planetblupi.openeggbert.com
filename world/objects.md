# Object Layer

## Overview

Each world cell optionally holds one object, stored in:
- `Cellule.objectChannel` — image channel (`CHOBJECT=2` or `CHOBJECTo=3`)
- `Cellule.objectIcon` — sprite index within the channel

Tall objects (trees, buildings) use **two channels**:
- `CHOBJECT (2)` — lower part of the object (overlays the cell's floor)
- `CHOBJECTo (3)` — upper part (overlays the cell one row higher in screen space)

A value of `objectIcon == -1` means no object is present.

---

## Object Categories (obj000.blp)

| Category | Example objects |
|----------|----------------|
| **Vegetation** | Trees, bushes, flowers, moss, grass, palms (region 1), pines (region 3) |
| **Resources** | Logs (wood), planks, stone, iron ore, tomatoes |
| **Buildings** | Hut / home, laboratory, factory, incubator, iron mine |
| **Structures** | Palisade (fence/plot), wall (mur), bridge, watchtower |
| **Vehicles (static)** | Boat, jeep, armour — as map objects, not character entities |
| **Enemy markers** | Spider, virus, electro tower, robot, tank spawn indicators |
| **Items** | Dynamite, mine, flag (waypoint), key, teleporter, egg, tomato, potion |
| **Hazards** | Fire, trap |
| **Special** | Hatched cell (mission target), special tile markers |

---

## Channel System

During rendering, `objectChannel` of a cell is interpreted as:

```cpp
if (objectChannel == CHOBJECT) {
    // Draw lower part of object (icon objectIcon)
    // at the position of this cell
}
if (objectChannel == CHOBJECTo) {
    // Draw object as overlay
    // (for tall objects overlapping cells above)
}
```

The upper overlay channel (`obj-o*.blp`) contains icons aligned to visually
connect with corresponding icons in `obj*.blp`.

---

## Placing and Reading Objects

```cpp
BOOL CDecor::PutObject(POINT cel, int channel, int icon)
// Places an object on cell cel
// channel = CHOBJECT or CHOBJECTo
// icon = sprite index

BOOL CDecor::GetObject(POINT cel, int &channel, int &icon)
// Reads the object from a cell
// Returns FALSE if the cell has no object (icon == -1)
```

---

## Special Objects — Notes

### Fire (`Cellule.fire`)
Fire intensity is stored directly in `Cellule.fire` (0–MAXFIRE=400).
Fire spreading is controlled by `CDecor::MoveFire()` and `MoveProxiFire()` in `decmove.cpp`.

### Hatched Cell (mission target)
Cells with certain icons are marked as "hatched" — mission target cells.
`CDecor::IsTerminated()` checks whether `Term` conditions are met
(correct object or character on the hatched cell).

### Teleporter
Teleporters always exist in pairs. The `GOAL_TELEPORTE` opcode handles
transferring Blupi from one teleporter to its partner.

### Mine
Mines (`BUTTON_FABMINE`) are invisible to enemies.
The triggering entity is `perso=6` (Mine detonator) — an invisible character
bound to the mine's position that detonates when triggered.

### Bridge
A bridge is a special object that allows Blupi to cross water.
`CDecor::IsBuildPont()` checks whether a bridge can be built.
Bridge animation uses the `Move` system via `GOAL_ADDMOVES`.

---

## Object Passability Table (obstacle.cpp)

```cpp
// tableObstacleObject[] — passability of each object icon index
// 0 = passable, 1 = obstacle
// Large objects (trees, buildings) are blocking
// Small decorations (flowers, grass) are passable
static char tableObstacleObject[] = { ... };
```

---

## Object-related Search Functions

| Function | Description |
|----------|-------------|
| `IsWorkableObject(cel, rank)` | Can the character work on the object at this cell? |
| `SearchOtherObject(rank, initCel, action, distMax, channel, f1,l1,f2,l2, foundCel, foundIcon)` | Find nearest matching object within distMax |
| `IsSpiderObject(icon)` | Is this icon a valid spider target? |
| `SearchSpiderObject(...)` | Spider looks for an object to destroy |
| `IsTracksObject(icon)` | Is this icon crushable by tracks? |
| `SearchTracksObject(...)` | Tank looks for an object to crush |
| `IsRobotObject(icon)` | Is this icon a valid robot work target? |
| `SearchRobotObject(...)` | Robot looks for work or something to attack |
| `IsBombeObject(icon)` | Is this icon something a bomb targets? |
| `SearchElectroObject(...)` | Electro tower scans for Blupi in range |
