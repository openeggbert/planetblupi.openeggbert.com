# Mouse Cursor Sprites (SPRITE_*)

Custom cursor sprites are drawn by `CPixmap` directly onto the back buffer,
overlaying everything else. They are never OS-managed hardware cursors.

All `SPRITE_*` constants are defined in `include/def.h`.

---

## Sprite Reference

| Constant | Code | Description |
|----------|------|-------------|
| `SPRITE_ARROW` | 1 | Standard arrow cursor |
| `SPRITE_POINTER` | 2 | Targeting / action pointer (hand / crosshair) |
| `SPRITE_MAP` | 3 | Minimap hand cursor |
| `SPRITE_ARROWU` | 4 | Scroll upward |
| `SPRITE_ARROWD` | 5 | Scroll downward |
| `SPRITE_ARROWL` | 6 | Scroll left |
| `SPRITE_ARROWR` | 7 | Scroll right |
| `SPRITE_ARROWUL` | 8 | Scroll upper-left (diagonal) |
| `SPRITE_ARROWUR` | 9 | Scroll upper-right (diagonal) |
| `SPRITE_ARROWDL` | 10 | Scroll lower-left (diagonal) |
| `SPRITE_ARROWDR` | 11 | Scroll lower-right (diagonal) |
| `SPRITE_WAIT` | 12 | Busy / loading cursor |
| `SPRITE_EMPTY` | 13 | Empty (hidden cursor area) |
| `SPRITE_FILL` | 14 | Flood-fill cursor (editor) |

---

## Cursor Selection Logic

The active sprite is determined by context:
- **In game play area**: `SPRITE_POINTER` (over a cell) or a scroll arrow (at edge)
- **Over minimap**: `SPRITE_MAP`
- **Edge of screen**: `SPRITE_ARROWU/D/L/R/UL/UR/DL/DR` based on position
- **Over toolbar/menu**: `SPRITE_ARROW`
- **Loading**: `SPRITE_WAIT`
- **Editor flood-fill tool**: `SPRITE_FILL`

---

## Mouse Type (config.def)

The `MouseType` setting in `data/config.def` controls how the cursor is managed:

| Value | Constant | Description |
|-------|----------|-------------|
| 1 | `MOUSETYPEGRA` | GDI-drawn cursor (using the sprite system above) |
| 2 | `MOUSETYPEWIN` | Standard Windows cursor (OS-managed) |
| 3 | `MOUSETYPEWINPOS` | Windows cursor with position tracking |

In cross-platform builds (Linux, Web), only `MOUSETYPEGRA` is effective.
