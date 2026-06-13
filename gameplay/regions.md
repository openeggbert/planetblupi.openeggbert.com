# Regions (World Themes)

## Overview

The world region selects which set of floor and object sprite sheets to load,
changing the visual theme of the entire terrain without affecting gameplay.
Stored as `m_region` in `CDecor`.

---

## Region Table

| `m_region` | Theme | Floor sheet | Object sheet | Object overlay |
|-----------|-------|------------|-------------|----------------|
| 0 | **Normal** (green / temperate) | `floor000.blp` | `obj000.blp` | `obj-o000.blp` |
| 1 | **Tropical** (palm trees, sand) | `floor001.blp` | `obj001.blp` | `obj-o001.blp` |
| 2 | **Winter** (snow, ice) | `floor002.blp` | `obj002.blp` | `obj-o002.blp` |
| 3 | **Pine forest** | `floor003.blp` | `obj003.blp` | `obj-o003.blp` |

---

## Effect

When the region changes:
1. `CDecor::LoadImages()` reloads `CHFLOOR`, `CHOBJECT`, `CHOBJECTo` with the
   correct region-specific `.blp` files
2. All floor and object icons remain the same indices — only the visual appearance changes
3. The minimap colours are recomputed via `MapInitColors()`

---

## Region Selection Screen

Players select the visual theme at `WM_PHASE_REGION` (background: `image/region.blp`).
The selected region is stored in `DescFile.region` in the world file.

---

## API

```cpp
void CDecor::SetRegion(int region);  // set region (0–3)
int  CDecor::GetRegion();            // get current region
```

---

## Impact on Gameplay

The region has **no gameplay impact** — passability, enemy behaviour, and win
conditions are identical across all regions. It is a purely cosmetic choice.
Winter tiles (ice) in `floor002.blp` still behave like ice gameplay-wise in
all regions, because ice passability is determined by icon index, not visual theme.
