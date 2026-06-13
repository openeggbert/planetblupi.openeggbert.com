# Minimap

## Overview

The minimap (128×128 pixels) is positioned in the left part of the HUD:
- Position: `POSMAPX=8, POSMAPY=15`
- Dimensions: `DIMMAPX=128, DIMMAPY=128`
- Image channel: `CHMAP (9)`

Implementation: `src/decmap.cpp`

---

## Map Generation

`CDecor::GenerateMap()` walks the entire world grid and assigns a colour to each cell:

```cpp
BOOL CDecor::GenerateMap();
// Iterates m_decor[0..99][0..99]
// For each cell, calls MapInitColors() to get colour
// Draws a 2×1 pixel dot per cell (horizontal compression for isometric view)
```

`CDecor::MapInitColors()` initialises the colour palette based on:
- Floor icon (grass, water, ice, snow, ...)
- Object icon (trees, buildings, rocks, ...)
- Internal colour table `m_colors[100]`

---

## Viewport Rectangle

An outline rectangle showing the current visible viewport is drawn over the minimap.
Clicking on the minimap scrolls the viewport:

```cpp
BOOL CDecor::MapMove(POINT pos);
// pos = pixel position of click on the minimap
// Converts to grid coordinates and updates m_celCoin (scroll position)
// Returns TRUE if the click was within the minimap area
```

---

## Coordinate Conversion

```cpp
POINT CDecor::ConvCelToMap(POINT cel);
// Grid cell → minimap pixel

POINT CDecor::ConvMapToCel(POINT pos);
// Minimap pixel → grid cell
```

---

## Colour Coding

| Colour | Terrain / object |
|--------|-----------------|
| Dark green | Grass, earth (basic terrain) |
| Blue | Water |
| White | Ice / snow |
| Light green | Trees, vegetation |
| Brown | Rocks, stone |
| Grey | Buildings, structures |
| Yellow | Blupi (player character) |
| Red | Fire |
| Orange | Enemies |
