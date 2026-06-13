# Fog of War

## Overview

Fog of war is implemented in `src/fog.cpp` and integrated into
`CDecor::BlupiPushFog()` in `decblupi.cpp`.

Each world tile `Cellule` stores a `fog` field — an icon index (0–14) encoding
which of the 4 quadrants of the cell are hidden.

---

## Quadrant System

Each cell is divided into **4 quadrants**:

```
┌───┬───┐
│ 0 │ 1 │   0 = top-left
├───┼───┤   1 = top-right
│ 2 │ 3 │   2 = bottom-left
└───┴───┘   3 = bottom-right
```

Each quadrant is either visible (0) or hidden (1).

---

## 15 Fog Icons

The table `tableFog[15*4]` in `fog.cpp` encodes 15 possible patterns:

| Icon | Q0 | Q1 | Q2 | Q3 | Description |
|------|----|----|----|----|----|
| 0 | 0 | 0 | 0 | 0 | Fully visible (no fog) |
| 1 | 1 | 0 | 0 | 0 | Only top-left hidden |
| 2 | 0 | 1 | 0 | 0 | Only top-right hidden |
| 3 | 0 | 0 | 1 | 0 | Only bottom-left hidden |
| 4 | 0 | 0 | 0 | 1 | Only bottom-right hidden |
| 5 | 1 | 1 | 0 | 0 | Top half hidden |
| 6 | 0 | 0 | 1 | 1 | Bottom half hidden |
| 7 | 1 | 0 | 1 | 0 | Left half hidden |
| 8 | 0 | 1 | 0 | 1 | Right half hidden |
| 9 | 1 | 1 | 1 | 0 | All except bottom-right hidden |
| 10 | 1 | 1 | 0 | 1 | All except bottom-left hidden |
| 11 | 1 | 0 | 1 | 1 | All except top-right hidden |
| 12 | 0 | 1 | 1 | 1 | All except top-left hidden |
| 13 | 1 | 0 | 0 | 1 | Diagonal hidden (TL and BR) |
| 14 | 0 | 1 | 1 | 0 | Diagonal hidden (TR and BL) |

An icon value `≥ FOGHIDE (4)` means the cell is mostly hidden and is not rendered.

---

## API

```cpp
// fog.cpp:
void GetFogBits(int icon, char *pBits);  // icon → 4 quadrant flags
int  GetFogIcon(char *pBits);            // 4 flags → icon

// decblupi.cpp:
void CDecor::BlupiPushFog(int rank);     // update fog around this Blupi
void CDecor::ClearFog();                 // remove all fog (editor)
void CDecor::EnableFog(BOOL bEnable);    // enable/disable fog
```

---

## Update Mechanism

Each tick, for every living Blupi:

1. `BlupiPushFog(rank)` removes fog from all cells within the visible radius
2. The radius depends on the character type and position
3. Cells behind obstacles may remain hidden (line-of-sight calculation)
4. Fog does not regenerate — once uncovered, a cell stays visible

---

## Performance Notes

Fog is stored directly in each `Cellule` (1 short per cell).
Updates only happen for cells within range of each Blupi.
In build mode (`m_bBuild = TRUE`) fog is disabled entirely.
