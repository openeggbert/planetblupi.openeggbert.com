# Movement Directions (DIRECT_*)

## Overview

Planet Blupi uses an 8-direction system. Direction values are multiples of 16,
a design inherited from the animation phase counter (historically the direction
was encoded in the high bits of an action+phase counter).

All direction constants are defined in `include/def.h`.

---

## Direction Compass

```
        DIRECT_NO (80)
   DIRECT_O (64)    DIRECT_N (96)
         \    |    /
          \   |   /
           \  |  /
DIRECT_SO(48)--o--DIRECT_NE (112)
           /  |  \
          /   |   \
         /    |    \
   DIRECT_S(32)    DIRECT_E (0)
        DIRECT_SE (16)
```

Note: In the isometric view, "East" (DIRECT_E) visually points toward
the bottom-right, and "North" (DIRECT_N) toward the upper-right.

---

## Direction Constants

| Constant | Value | Compass | Grid delta (dx, dy) |
|----------|-------|---------|---------------------|
| `DIRECT_E` | 0 | East | (+1, 0) |
| `DIRECT_SE` | 16 | South-East | (+1, +1) |
| `DIRECT_S` | 32 | South | (0, +1) |
| `DIRECT_SO` | 48 | South-West | (-1, +1) |
| `DIRECT_O` | 64 | West | (-1, 0) |
| `DIRECT_NO` | 80 | North-West | (-1, -1) |
| `DIRECT_N` | 96 | North | (0, -1) |
| `DIRECT_NE` | 112 | North-East | (+1, -1) |

---

## Direction in Blupi Struct

```cpp
short aDirect;   // current direction (DIRECT_*)
short sDirect;   // desired direction (the character will rotate toward it)
```

`CDecor::BlupiRotate(rank)` advances `aDirect` one step toward `sDirect`
each tick, creating smooth rotation animation.

---

## Direction Helper Functions

```cpp
POINT GetVector(int direct);
// Converts a DIRECT_* value to a (dx, dy) cell offset vector.
// Example: GetVector(DIRECT_NE) = {+1, -1}

int CDecor::DirectSearch(POINT cel, POINT goal);
// Returns the DIRECT_* value that best points from cel toward goal.
// Uses Manhattan distance heuristic, returns the closest cardinal/diagonal direction.
```

---

## Direction in Action Codes

Animation sprites use direction as part of the action sprite selection.
For example, `ACTION_MARCHE` in direction `DIRECT_E` uses different sprite frames
than `ACTION_MARCHE` in direction `DIRECT_S`.

The `action.cpp` sprite tables are indexed by `(action, aDirect / 16)` to get
the correct frame sequence.

---

## 4-direction vs 8-direction

Most movement uses all 8 directions, but some actions only have 4 directional variants
(the cardinal directions only: E, S, O, N). Diagonal movement for such actions
falls back to the nearest cardinal direction.
