# Statistics Panel

## Overview

The right-hand statistics panel shows live mission status.
Position: `POSSTATX=12, POSSTATY=220` (within the HUD area left of the game view).

Implementation: `src/decstat.cpp`

---

## Panel Contents

| Statistic | Description |
|-----------|-------------|
| Living Blupi count | Total Blupi currently alive |
| Active fires | Number of cells currently on fire |
| Hatched cells total | Total hatched (target) cells in the mission |
| Hatched with Blupi | How many hatched cells have a Blupi on them |
| Hatched with planks | How many hatched cells have planks |
| Hatched with tomatoes | How many hatched cells have tomatoes |
| Hatched with metal | How many hatched cells have metal/iron |
| Hatched with robot | How many hatched cells have a disciple |
| Total homes | Total huts built |
| Homes with Blupi | Huts currently occupied |
| Remaining enemies | Total enemy characters still alive |

---

## Internal Counters

```cpp
int m_nbStatHach;           // total hatched cells
int m_nbStatHachBlupi;      // hatched cells with Blupi
int m_nbStatHachPlanche;    // hatched cells with planks
int m_nbStatHachTomate;     // hatched cells with tomatoes
int m_nbStatHachMetal;      // hatched cells with metal
int m_nbStatHachRobot;      // hatched cells with disciple
int m_nbStatHome;           // total homes
int m_nbStatHomeBlupi;      // occupied homes
int m_nbStatRobots;         // remaining enemies
```

---

## Update Mechanism

```cpp
void CDecor::StatisticInit();
// Initialises all counters to zero

void CDecor::StatisticUpdate();
// Recalculates all counters from current world state
// Sets m_bStatRecalc = FALSE after recalculation
// Called every tick when m_bStatRecalc = TRUE

int CDecor::StatisticGetBlupi();
// Returns the current living Blupi count

int CDecor::StatisticGetFire();
// Returns the current active fire count
```

---

## Rendering

```cpp
void CDecor::StatisticDraw();
// Renders the statistics panel using CPixmap
// Uses CHLITTLE channel for small numeric text

void CDecor::GenerateStatictic();
// Generates the full statistics display
// Called when m_bStatRedraw = TRUE
```

---

## Interaction

The statistics panel is clickable — hovering or clicking a stat
can highlight related cells on the map.

```cpp
BOOL CDecor::StatisticDown(POINT pos, int fwKeys);  // mouse press
BOOL CDecor::StatisticMove(POINT pos, int fwKeys);  // mouse move
BOOL CDecor::StatisticUp(POINT pos, int fwKeys);    // mouse release
int  CDecor::StatisticDetect(POINT pos);             // detect which stat is under cursor
```

`m_statHili` holds the index of the currently highlighted statistic row.
`m_statFirst` is the index of the first visible row (for scrolling).
`m_bStatUp/m_bStatDown` indicate whether scroll arrows are visible.
