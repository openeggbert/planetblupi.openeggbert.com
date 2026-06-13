# Rendering

## Image Channels (CPixmap)

`CPixmap` manages a set of named **channels** (0–14), each holding one `.blp`
image with its own palette and icon set.

```cpp
// Load an image into a channel:
pPixmap->Cache(channel, "image/blupi.blp");

// Draw an icon from a channel:
pPixmap->DrawIcon(hdc, channel, icon, x, y);
```

### Channel Reference

| Constant | Value | Image file | Contents |
|----------|-------|-----------|---------|
| `CHBACK` | 0 | various (phase background) | Current screen background |
| `CHFLOOR` | 1 | `floor000–003.blp` | Floor tiles (region 0–3) |
| `CHOBJECT` | 2 | `obj000–003.blp` | Objects — lower part (region 0–3) |
| `CHOBJECTo` | 3 | `obj-o000–003.blp` | Objects — upper overlay (region 0–3) |
| `CHBLUPI` | 4 | `blupi.blp` | All animation frames: Blupi + all enemies |
| `CHHILI` | 5 | `hili.blp` | Selection / action highlight overlays |
| `CHFOG` | 6 | `fog.blp` | 15 fog-of-war tile patterns |
| `CHMASK1` | 7 | `mask1.blp` | Alpha mask for Blupi sprite blending |
| `CHLITTLE` | 8 | `little.blp` | Small pixel font (10 px characters) |
| `CHMAP` | 9 | — (generated) | Minimap (128×128 px, generated from world data) |
| `CHBUTTON` | 10 | `button.blp` | Toolbar button icons (35 BUTTON_* types) |
| `CHGROUND` | 11 | `floor000–003.blp` | Floor — second channel (for layering) |
| `CHJAUGE` | 12 | `jauge.blp` | Energy / progress gauge sprites |
| `CHTEXT` | 13 | `text.blp` | Main text font (16×16 px), white, red and slim variants |
| `CHBIGNUM` | 14 | `bignum.blp` | Large digit sprites for score / timer |

---

## Draw Order (Z-order)

Each game tick renders the scene in this order:

```
1. Background (CHBACK) — fixed HUD frame
2. Minimap (CHMAP) — 128×128 px top-left
3. Floor tiles (CHFLOOR/CHGROUND) — for each cell in the viewport
4. Objects lower part (CHOBJECT) — overlaid on top of floors
5. Characters — Blupi and enemies (CHBLUPI) with correct Z-order
6. Highlight overlays (CHHILI) — selection boxes, action indicators
7. Objects upper part (CHOBJECTo) — parts of objects that overlap the cell above
8. Fog (CHFOG) — overlays everything in hidden cells
9. HUD elements — gauges (CHJAUGE), buttons (CHBUTTON), text (CHTEXT/CHLITTLE)
10. Mouse cursor (SPRITE_*) — always on top
```

---

## Coordinate System

The game uses a "diamond" isometric projection:

```
Grid cell → screen pixel (ConvCelToPos):
  px = (cel.x - celCoin.x) * DIMCELX/2
     - (cel.y - celCoin.y) * DIMCELX/2
     + POSDRAWX + DIMDRAWX/2
  py = (cel.x - celCoin.x) * DIMCELY/2
     + (cel.y - celCoin.y) * DIMCELY/2
     + POSDRAWY

Screen pixel → grid cell (ConvPosToCel): inverse of the above.

ConvPosToCel2(pos): alternative conversion for the editor.
```

`SHIFTBLUPIY=5` shifts Blupi 5 pixels upward for correct Z-order visual effect
(the character appears to stand on the surface of the cell).

---

## Highlight Icons (CHHILI, channel 5)

| Icon index | Constant | Description |
|------------|----------|-------------|
| 112 | `ICON_HILI_STAT` | Statistics highlight |
| 113 | `ICON_HILI_SEL` | Character is selected |
| 114 | `ICON_HILI_ANY` | General hover |
| 115 | `ICON_HILI_OP` | Operation is available |
| 117 | `ICON_HILI_GO` | Movement target |
| 118 | `ICON_HILI_BUILD` | Build location |
| 119 | `ICON_HILI_ERR` | Error (action not possible) |

---

## BLP Image Format

Files with `.blp` extension in `image/` are Epsitec's proprietary palette-based
bitmap format (BLP = Blupi image Package). Each file contains:
- A 256-colour palette
- A sequence of named "icons" (frame sprites)
- Each icon has its own dimensions and pixel data (8-bit indexed)

Loading is handled by `CPixmap::Cache()` (via `SDL_image` in the cross-platform build).
