# Data Structures

This file describes all key data structures of the Planet Blupi engine in full detail.

---

## `Cellule` — one world tile

Defined in `include/decor.h`. The world grid is stored as
`Cellule m_decor[100][100]` (MAXCELX/2 × MAXCELY/2 = 10 000 elements).

Access to a cell at world coordinate `(x, y)`:
```cpp
m_decor[x/2][y/2]
```
The 200×200 grid is stored as 100×100 for memory efficiency.

```cpp
typedef struct
{
    short floorChannel;   // image channel for the floor sprite (CHFLOOR etc.)
    short floorIcon;      // sprite index within the floor channel
    short objectChannel;  // image channel for the object sprite
    short objectIcon;     // sprite index within the object channel
    short fog;            // fog of war — icon index (0–14; 0=fully visible)
    short rankMove;       // index into m_move[] (-1 = no animation)
    short workBlupi;      // rank of the Blupi working at this cell (-1 = none)
    short fire;           // fire intensity counter (0=no fire, max MAXFIRE=400)
}
Cellule;
```

### Special `fog` values

The fog icon (0–14) encodes which of the 4 quadrants of the cell are hidden.
See [Fog of War](fog-of-war.md) for the complete encoding table.

A value of `objectIcon == -1` means no object is present.

---

## `Blupi` — one animated character

Defined in `include/decor.h`. The array `m_blupi[MAXBLUPI]` (100 elements) in CDecor
holds all characters — both Blupi and enemies.

```cpp
#define MAXBLUPI   100   // max simultaneous characters
#define MAXUSED    50    // max visited cells remembered per character
#define MAXLIST    10    // max queued commands per character

typedef struct
{
    BOOL  bExist;        // TRUE → slot is occupied
    BOOL  bHili;         // TRUE → character is selected (highlighted)

    short perso;         // character type (see table below)

    // Long-term goal (GOAL_* sequence)
    short goalAction;    // action (WM_ACTION_* code, offset by WM_USER)
    short goalPhase;     // current phase in the GOAL_* sequence
    POINT goalCel;       // target cell for the goal
    POINT passCel;       // intermediate pass-through cell during movement

    short energy;        // remaining energy (0..MAXENERGY=4000)

    // Position and movement
    POINT cel;           // current grid cell
    POINT destCel;       // destination cell for movement
    short action;        // current ACTION_* animation code
    short aDirect;       // current direction (DIRECT_*)
    short sDirect;       // desired direction (DIRECT_*)

    // Rendering
    POINT pos;           // sub-pixel position relative to cell centre
    short posZ;          // z-displacement (height during jump)
    short channel;       // current sprite channel
    short lastIcon;      // previous icon (for change detection)
    short icon;          // current sprite icon index
    short phase;         // animation phase within the current action
    short step;          // global step counter
    short interrupt;     // interrupt priority: 0=high, 1=normal, 2=misc
    short clipLeft;      // left clip (for animations near right edge)

    // Visited position memory (prevents pathfinding loops)
    int   nbUsed;        // number of remembered positions
    char  nextRankUsed;  // circular write index
    POINT posUsed[MAXUSED];   // visited cells
    char  rankUsed[MAXUSED];  // visit count per cell

    // Carried object
    short takeChannel;   // channel of the object being carried
    short takeIcon;      // icon of the object being carried

    POINT fix;           // fixed reference point (cultive, bridge)

    // Progress gauge
    short jaugePhase;    // current gauge value
    short jaugeMax;      // maximum gauge value

    // Control flags
    short stop;          // 1 → character will stop at end of step
    short bArrow;        // TRUE → directional arrow above character (waypoint)
    short bRepeat;       // TRUE → repeat action
    short nLoop;         // loop count for GOAL_OTHERLOOP
    short cLoop;         // current loop iteration
    short vIcon;         // variable icon (changes at runtime)
    POINT goalHili;      // highlighted goal cell
    short bMalade;       // TRUE → character is sick / poisoned
    short bCache;        // TRUE → hidden (not drawn, e.g. during explosion)
    short vehicule;      // vehicle (see table below)

    // Click timing
    char  busyCount;     // busy counter
    char  busyDelay;     // busy delay
    char  clicCount;     // double-click counter
    char  clicDelay;     // double-click delay

    // Command queue
    short listButton[MAXLIST];   // queued BUTTON_* commands
    POINT listCel[MAXLIST];      // target cells for queued commands
    short listParam[MAXLIST];    // parameters for queued commands

    // Repeat level
    short repeatLevelHope;
    short repeatLevel;
}
Blupi;
```

### `perso` values (character type)

| Value | Character | Description |
|-------|-----------|-------------|
| 0 | **Blupi** | Player character. Walks, builds, carries, uses vehicles. |
| 1 | **Spider (Araignée)** | Enemy. Poisons Blupi on contact. Can jump over obstacles. |
| 2 | **Virus** | Enemy. Spreads to adjacent objects and destroys them. |
| 3 | **Tracks (Tank)** | Heavy enemy. Crushes objects and Blupi in its path. |
| 4 | **Robot** | Intelligent enemy. Builds, mines, fires a ray beam. |
| 5 | **Bomb (Bombe)** | Bouncing explosive. Seeks Blupi, detonates on contact. |
| 6 | **Mine detonator (Détonateur)** | Invisible entity tied to a placed mine; detonates on trigger. |
| 7 | **Electro** | Stationary tower firing an electric ray at Blupi in range. |
| 8 | **Disciple (Robot2)** | Friendly helper robot that autonomously performs most Blupi tasks. |

### `vehicule` values

| Value | Vehicle | Description |
|-------|---------|-------------|
| 0 | On foot | Default state |
| 1 | Boat (bateau) | Navigates water cells |
| 2 | Jeep | Moves faster, crosses rough terrain |
| 3 | Armour (armure) | Invulnerable to most attacks |

---

## `Move` — animated decoration element

Defined in `include/decor.h`. Array `m_move[MAXMOVE]` (100 elements) in CDecor.
Used for: fire spreading, bridge animation, building construction steps, etc.

```cpp
#define MAXMOVE     100    // max simultaneous animated decorations
#define MOVEICONNB  1000   // max entries in global icon animation table

typedef struct
{
    BOOL  bExist;       // TRUE → slot is occupied
    POINT cel;          // world grid cell of this decoration
    short rankBlupi;    // index of the Blupi driving this animation (-1 = autonomous)
    BOOL  bFloor;       // TRUE = floor layer, FALSE = object layer
    short channel;      // destination image channel
    short icon;         // current icon index
    short maskChannel;  // mask image channel (0 = no mask)
    short maskIcon;     // mask icon index
    short phase;        // phase in pMoves or pIcon
    short rankMoves;    // index into tableMoves[] (*nb,dx,dy,...)
    short rankIcons;    // index into tableIcons[] (*nb,i,i,...)
    short total;        // total number of animation steps
    short delai;        // delay between steps (in ticks)
    short stepY;        // vertical step × 100 (for bounce effects)
    short cTotal;       // current step counter (counts down from total)
    short cDelai;       // current delay counter
}
Move;
```

---

## `Term` — win conditions

Defined in `include/def.h`. Each world file contains one instance.
`CDecor::IsTerminated()` returns a positive code when all non-zero conditions are met.

```cpp
typedef struct
{
    short bHachBlupi;     // Blupi must stand on the hatched target cell
    short bHachPlanche;   // planks must be on the hatched cell
    short bStopFire;      // all fires must be extinguished
    short nbMinBlupi;     // minimum number of living Blupi
    short nbMaxBlupi;     // maximum number of living Blupi
    short bHomeBlupi;     // all Blupi must be inside a hut
    short bKillRobots;    // all enemies must be destroyed
    short bHachTomate;    // tomatoes must be on the hatched cell
    short bHachMetal;     // metal must be on the hatched cell
    short bHachRobot;     // a robot must be on the hatched cell
    short reserve[14];    // reserved for future conditions
}
Term;
```

---

## `DescFile` — world file header

Defined internally in `src/decio.cpp`. It is the first block of a binary `.blp` file.

```cpp
typedef struct
{
    short   majRev;              // major format version
    short   minRev;              // minor format version
    int32_t nbDecor;             // number of Cellule elements (= 100*100 = 10000)
    int32_t lgDecor;             // size of Cellule section in bytes
    int32_t nbBlupi;             // number of Blupi elements (= MAXBLUPI = 100)
    int32_t lgBlupi;             // size of Blupi section in bytes
    int32_t nbMove;              // number of Move elements (= MAXMOVE = 100)
    int32_t lgMove;              // size of Move section in bytes
    short   reserve1[100];       // 200 bytes reserved
    POINT   celCoin;             // scroll position (top-left visible cell)
    short   world;               // world / mission number
    int32_t time;                // game time (in ticks)
    char    buttonExist[40];     // MAXBUTTON=40: which toolbar buttons are available
    Term    term;                // win conditions
    short   music;               // music track 0–9
    short   region;              // visual region 0–3
    int32_t totalTime;           // total time spent on mission (statistics)
    short   skill;               // difficulty 0–2
    POINT   memoPos[4];          // saved camera positions (F5–F8)
    short   reserve2[29];        // reserved
}
DescFile;
```

After the `DescFile` header, the file contains sequentially:
1. Cellule data (`lgDecor` bytes)
2. Blupi data (`lgBlupi` bytes)
3. Move data (`lgMove` bytes)

---

## `OldBlupi` — backward compatibility

`src/decio.cpp` also defines `OldBlupi` — the older Blupi structure without
the `listButton/listCel/listParam/repeatLevel*` fields. When loading older `.blp`
files, the version fields in `DescFile` trigger conversion from `OldBlupi` to `Blupi`.

---

## `DemoHeader` and `DemoEvent` — demo recordings

Defined in `include/event.h`.

```cpp
struct DemoHeader {
    short version;   // demo format version
    short world;     // world number (mission)
    short skill;     // difficulty (0=easy, 1=normal, 2=hard)
    short flags;     // flags (mode etc.)
};

struct DemoEvent {
    int    time;     // event time in ms from demo start
    UINT   message;  // Windows message (WM_*)
    WPARAM wParam;   // message parameter
    LPARAM lParam;   // message parameter (usually encodes mouse position)
};
```
