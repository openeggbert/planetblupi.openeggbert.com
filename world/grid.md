# World Grid

## Dimensions

| Constant | Value | Description |
|----------|-------|-------------|
| `MAXCELX` | 200 | Grid width (cells, west→east axis) |
| `MAXCELY` | 200 | Grid height (cells, north→south axis) |
| `DIMCELX` | 60 | Cell width in pixels (isometric) |
| `DIMCELY` | 30 | Cell height in pixels (isometric) |

The world has **200×200 cells** (40 000 cells total).
Internally stored as `Cellule m_decor[100][100]` — accessed via `m_decor[x/2][y/2]`.

---

## Viewport (Visible Area)

| Constant | Value | Description |
|----------|-------|-------------|
| `POSDRAWX` | 144 | X-offset of game area from window left |
| `POSDRAWY` | 15 | Y-offset of game area from window top |
| `DIMDRAWX` | 480 | Game area width in pixels |
| `DIMDRAWY` | 450 | Game area height in pixels |

`m_celCoin` holds the cell corresponding to the top-left of the viewport (scroll position).
`m_celHome` holds the default "Home key" position.

---

## Isometric Projection

Planet Blupi uses a "diamond" isometric view:

```
Viewed from above (schematic):

           N (north)
           ^
    NW     |     NE
      \    |    /
       \   |   /
        \  |  /
    W ---(-+-)--- E
        /  |  \
       /   |   \
      /    |    \
    SW     |     SE
           v
           S (south)
```

Grid axis X points **south-east** (E), grid axis Y points **south-west** (S).

---

## Coordinate Conversion

### Cell → Pixel (ConvCelToPos)

```cpp
POINT CDecor::ConvCelToPos(POINT cel) {
    POINT pos;
    pos.x = (cel.x - m_celCoin.x) * DIMCELX/2
          - (cel.y - m_celCoin.y) * DIMCELX/2
          + POSDRAWX + DIMDRAWX/2;
    pos.y = (cel.x - m_celCoin.x) * DIMCELY/2
          + (cel.y - m_celCoin.y) * DIMCELY/2
          + POSDRAWY;
    return pos;
}
```

### Pixel → Cell (ConvPosToCel)

```cpp
POINT CDecor::ConvPosToCel(POINT pos, BOOL bMap) {
    // Inverse of ConvCelToPos
    // bMap=TRUE: conversion for minimap clicks
    int relX = pos.x - POSDRAWX - DIMDRAWX/2;
    int relY = pos.y - POSDRAWY;
    // (approximate integer arithmetic)
    cel.x = m_celCoin.x + (relX + relY*2) / DIMCELX;
    cel.y = m_celCoin.y + (relY*2 - relX) / DIMCELX;
    return cel;
}
```

`ConvPosToCel2(pos)` — alternative more precise conversion used in the editor.

---

## Cell Validation

```cpp
BOOL IsValid(POINT cel) {
    return (cel.x >= 0 && cel.x < MAXCELX &&
            cel.y >= 0 && cel.y < MAXCELY);
}
```

---

## Scrolling

Scrolling happens by moving the mouse to the screen edge:
- Cursor sprites `SPRITE_ARROWU/D/L/R/UL/UR/DL/DR` indicate scroll direction
- `m_celCoin` is incremented / decremented by cell steps
- Minimum: (0, 0), maximum: (MAXCELX − visible, MAXCELY − visible)

Saved camera positions (`m_memoPos[4]`) are assigned via Shift+F5–F8,
recalled via F5–F8.

---

## Coordinate Helper Functions

```cpp
POINT GetCel(int x, int y);               // create POINT{x, y}
POINT GetCel(POINT cel, int dx, int dy);  // cel + (dx, dy) cell offset
POINT GetVector(int direct);              // convert DIRECT_* → (dx, dy) vector
```

### GetVector — Direction Vectors

| `direct` | dx | dy |
|----------|----|----|
| `DIRECT_E` (0) | +1 | 0 |
| `DIRECT_SE` (16) | +1 | +1 |
| `DIRECT_S` (32) | 0 | +1 |
| `DIRECT_SO` (48) | -1 | +1 |
| `DIRECT_O` (64) | -1 | 0 |
| `DIRECT_NO` (80) | -1 | -1 |
| `DIRECT_N` (96) | 0 | -1 |
| `DIRECT_NE` (112) | +1 | -1 |
