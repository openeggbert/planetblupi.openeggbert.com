# Character Overview

## Storage

All characters are stored as `Blupi` structs in `CDecor::m_blupi[]` (100 slots).
The `perso` field identifies the character type.

```cpp
// Create a character:
int CDecor::BlupiCreate(POINT cel, int action, int direct, int perso, int energy);

// Delete a character at a cell:
BOOL CDecor::BlupiDelete(POINT cel, int perso=-1);

// Delete a character by rank:
void CDecor::BlupiDelete(int rank);

// Kill a character (plays death animation):
void CDecor::BlupiKill(int exRank, POINT cel, int type);
```

---

## All Character Types

| `perso` | Internal name | French name | Controlled by |
|---------|--------------|-------------|---------------|
| 0 | Blupi | Blupi | Player |
| 1 | Spider | Araignée | AI enemy |
| 2 | Virus | Virus | AI enemy |
| 3 | Tracks | Tracks | AI enemy |
| 4 | Robot | Robot | AI enemy |
| 5 | Bomb | Bombe | AI (autonomous) |
| 6 | Mine detonator | Détonateur | Passive trigger |
| 7 | Electro tower | Électro | AI enemy (stationary) |
| 8 | Disciple | Disciple / Robot2 | Player (helper) |

---

## Character Lifecycle

```
BlupiCreate()
    │
    ├─ Sets bExist = TRUE
    ├─ Sets cel, action, aDirect, perso, energy
    ├─ Calls BlupiInitAction() to set initial sprite
    │
    └─ Character enters the game loop

Each tick:
    BlupiNextAction(rank)   ← advances animation frame
    BlupiNextGoal(rank)     ← advances GOAL_* sequence
    BlupiPushFog(rank)      ← updates fog of war

Death:
    BlupiKill() → plays death animation → BlupiDelete()
```

---

## Selection System

Players can select one or multiple Blupi characters:

```cpp
void CDecor::BlupiHiliDown(POINT pos, BOOL bAdd);  // mouse press — start selection
void CDecor::BlupiHiliMove(POINT pos, BOOL bAdd);  // mouse drag — extend selection rect
void CDecor::BlupiHiliUp(POINT pos, BOOL bAdd);    // mouse release — finalise selection
void CDecor::BlupiDeselect();                       // deselect all
void CDecor::BlupiDeselect(int rank);               // deselect one character
void CDecor::BlupiDrawHili();                       // draw selection highlights
```

`m_bHiliRect` is TRUE when the player is dragging a selection rectangle.
`m_nbBlupiHili` holds the count of currently selected Blupi.
`m_rankBlupiHili` holds the rank of the single selected Blupi (-1 if multiple).

---

## Energy System

Each Blupi has `energy` (0..MAXENERGY=4000).

- Energy drains over time and during actions
- When energy reaches 0, Blupi must eat or drink (BUTTON_MANGE / BUTTON_BOIT)
- If energy reaches 0 with no food available, Blupi eventually dies
- Tired Blupi use `ACTION_STOPf` / `ACTION_MARCHEf` (tired variants)
- On the **Easy** skill level, energy drains slower; **Hard** drains faster

---

## Arrow Indicator

`m_celArrow` / `Blupi.bArrow` — a directional arrow drawn above a Blupi.
Used to indicate that a Blupi has a waypoint queued.

---

## Busy / Click Timing

```cpp
char busyCount;   // increments each tick while character is busy
char busyDelay;   // delay before accepting new commands
char clicCount;   // tracks double-click count
char clicDelay;   // delay window for double-click detection
```

These throttle how quickly a character can receive new commands,
preventing accidental double-commands from rapid clicks.

---

## Command Queue (listButton)

Each character has a FIFO queue of up to `MAXLIST=10` commands:

```cpp
short listButton[MAXLIST];   // BUTTON_* command types
POINT listCel[MAXLIST];      // target cells
short listParam[MAXLIST];    // extra parameters

// Queue management:
BOOL  CDecor::ListPut(int rank, int button, POINT cel, POINT cMem);  // enqueue
void  CDecor::ListRemove(int rank);                                    // dequeue head
void  CDecor::ListFlush(int rank);                                     // clear all
int   CDecor::ListSearch(int rank, int button, POINT cel, ...);       // search queue
```

---

## Carried Object

A Blupi can carry one object at a time:

```cpp
short takeChannel;  // channel of carried object (CHOBJECT etc.), -1 = nothing
short takeIcon;     // icon of carried object
```

The carried object is rendered above the Blupi's head using the same sprite
as its in-world equivalent.
