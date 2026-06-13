# Win Conditions (Term)

## Overview

Each world file embeds a `Term` struct specifying what must be achieved to
win the mission. `CDecor::IsTerminated()` returns a positive code when all
non-zero conditions are simultaneously satisfied.

```cpp
typedef struct
{
    short bHachBlupi;     // Blupi must stand on the hatched target cell
    short bHachPlanche;   // planks must be on the hatched cell
    short bStopFire;      // all fires must be extinguished
    short nbMinBlupi;     // minimum number of living Blupi required
    short nbMaxBlupi;     // maximum number of living Blupi allowed
    short bHomeBlupi;     // all Blupi must be inside a hut
    short bKillRobots;    // all enemies must be destroyed
    short bHachTomate;    // tomatoes must be on the hatched cell
    short bHachMetal;     // metal (iron) must be on the hatched cell
    short bHachRobot;     // a robot (disciple) must be on the hatched cell
    short reserve[14];    // reserved for future conditions
}
Term;
```

---

## Condition Details

| Field | When active | Satisfied when |
|-------|-------------|----------------|
| `bHachBlupi` | non-zero | At least one Blupi stands on any hatched cell |
| `bHachPlanche` | non-zero | Planks object is on any hatched cell |
| `bStopFire` | non-zero | `StatisticGetFire() == 0` (no fires burning) |
| `nbMinBlupi` | > 0 | Living Blupi count ≥ `nbMinBlupi` |
| `nbMaxBlupi` | > 0 | Living Blupi count ≤ `nbMaxBlupi` |
| `bHomeBlupi` | non-zero | All living Blupi are inside a hut |
| `bKillRobots` | non-zero | No enemy characters remain alive |
| `bHachTomate` | non-zero | Tomatoes object is on any hatched cell |
| `bHachMetal` | non-zero | Metal/iron object is on any hatched cell |
| `bHachRobot` | non-zero | A disciple (robot2) is on any hatched cell |

---

## IsTerminated()

```cpp
int CDecor::IsTerminated()
// Returns:
//   0  → conditions not yet met (game continues)
//   1  → victory (all conditions met)
//  -1  → defeat (not currently used by Term, but set by other conditions)
```

The function checks each non-zero `Term` field every tick.
When all conditions are simultaneously true for `m_winCount` consecutive ticks
(a brief stabilisation period), the game transitions to `WM_PHASE_WIN`.

---

## Statistics Used in Win Check

`StatisticUpdate()` recalculates these counters every tick:

| Counter | Description |
|---------|-------------|
| `m_nbStatHach` | Total hatched cells in the world |
| `m_nbStatHachBlupi` | Hatched cells occupied by Blupi |
| `m_nbStatHachPlanche` | Hatched cells with planks |
| `m_nbStatHachTomate` | Hatched cells with tomatoes |
| `m_nbStatHachMetal` | Hatched cells with metal |
| `m_nbStatHachRobot` | Hatched cells with a disciple |
| `m_nbStatHome` | Total huts |
| `m_nbStatHomeBlupi` | Huts occupied by Blupi |
| `m_nbStatRobots` | Remaining enemies |

---

## Win Condition Initialisation

```cpp
void CDecor::TerminatedInit();
// Resets all win tracking counters
// Called at mission start

Term* CDecor::GetTerminated();
// Returns pointer to the current Term struct
// Used by the statistics panel and win-condition display
```

---

## Typical Mission Win Condition Examples

| Mission type | Typical `Term` fields set |
|-------------|--------------------------|
| Survival | `nbMinBlupi > 0` |
| Delivery | `bHachPlanche` or `bHachTomate` or `bHachMetal` |
| Extermination | `bKillRobots` |
| Shelter | `bHomeBlupi` |
| Fire control | `bStopFire` |
| Combined | Multiple fields simultaneously |
