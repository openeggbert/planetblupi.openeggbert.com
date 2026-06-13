# Terrain & Auto-tiling

## Floor Tiles

The floor is stored in `Cellule.floorChannel` and `Cellule.floorIcon`.
The floor channel is always `CHFLOOR (1)` or `CHGROUND (11)`.
The sprite file depends on the active region:

| Region | `m_region` | Floor file | Object file |
|--------|-----------|------------|------------|
| Normal (green / temperate) | 0 | `floor000.blp` | `obj000.blp` |
| Tropical (palm trees) | 1 | `floor001.blp` | `obj001.blp` |
| Winter (snow / ice) | 2 | `floor002.blp` | `obj002.blp` |
| Pine forest | 3 | `floor003.blp` | `obj003.blp` |

---

## Key Floor Icon Ranges (floor000.blp)

| Icon range | Terrain type | Passability |
|------------|-------------|-------------|
| 0 | Black / empty (world border) | Impassable for all |
| 1–14 | Water↔land transitions (shoreline) | Depends on specific icon |
| 15–19 | Land (grass / normal) | Passable for all ground units |
| 20–32 | Dark soil / moss | Passable |
| Water icons | Water | Passable for boats only |
| Ice icons | Slippery ice | Passable, but causes sliding |
| Snow icons | Snow (winter region) | Passable |

---

## Auto-tiling (arrange.cpp)

Auto-tiling automatically selects the correct floor tile based on neighbouring cells
to make terrain transitions look natural.

### `tableSee` — water transitions

```cpp
// Encodes which quadrants (0-1 / 2-3) of a cell contain water
// 14 patterns × 4 quadrants
static char tableSee[14*4] = {
    0,0,0,0,  // 1 - no water
    0,1,0,1,  // 2
    0,0,1,1,  // 3
    1,0,1,0,  // 4
    1,1,0,0,  // 5
    0,0,0,1,  // 6
    0,0,1,0,  // 7
    1,0,0,0,  // 8
    0,1,0,0,  // 9
    0,1,1,1,  // 10
    1,0,1,1,  // 11
    1,1,1,0,  // 12
    1,1,0,1,  // 13
    1,1,1,1,  // 14 - fully water cell
};
```

### `tableDark` — moss / dark soil transitions

```cpp
// 13 patterns × 4 quadrants (icons 20–32)
static char tableDark[13*4] = { ... };
```

### `ArrangeFloor(cel)`

Main floor auto-tiling function:
1. Examines 8 neighbouring cells
2. Determines terrain types of neighbours (water, grass, moss, ...)
3. Selects the appropriate tile from `tableSee` / `tableDark`
4. Applies the icon to the cell

### `ArrangeMur(cel, icon, index)`

Wall auto-tiling — sets the correct wall icon (corners, straight segments)
based on neighbouring wall cells.

### `ArrangeBuild(cel, channel, icon)`

Building auto-tiling — sets the correct building icon depending on whether
a neighbouring cell is also part of the same building.

### `ArrangeObject(cel)`

Adjusts objects on the cell and its surroundings after placing a new object.

### `ArrangeBlupi()`

Adjusts cell appearance for Blupi's current state
(e.g. if Blupi stands on water in a boat, the cell below gets a water texture).

---

## Flood-fill (ArrangeFill)

`ArrangeFill()` performs a flood-fill with a chosen terrain type:

```cpp
void CDecor::ArrangeFill(POINT pos, int channel, int icon, BOOL bFloor)
// Starts from cell pos
// Spreads to all neighbouring cells of the same type
// Replaces them with the given channel/icon
// Used in the editor for quick area filling
```

Helper functions:
- `ArrangeFillTestFloor(cel1, cel2)` — verify flood-fill eligibility
- `ArrangeFillTest(pos)` — test a single cell for flood-fill
- `ArrangeFillPut(pos, channel, icon)` — place a tile during flood-fill
- `ArrangeFillSearch(pos)` — search neighbouring cells

---

## Floor Passability Table (obstacle.cpp)

```cpp
// tableObstacleFloor[] — passability of each floor icon index
// 0 = passable, 1 = obstacle
// Indexed by floor icon (0..N)
// Each icon has 5×5 = 25 passability bits (for different character types)
static char tableObstacleFloor[] = {
    1,1,1,1,1,  // icon 0 (black border) — all blocked
    1,1,1,1,1,
    ...
    0,0,0,0,0,  // icon 1 (land) — all passable
    ...
};
```
