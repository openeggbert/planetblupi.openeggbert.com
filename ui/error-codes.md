# Error Codes (ERROR_*)

Displayed as tooltip or highlight messages when an action cannot be performed.
All constants defined in `include/def.h`.

The error highlight `ICON_HILI_ERR` (119 in CHHILI) is shown on the target cell
when an action is rejected.

---

## Error Reference

| Constant | Code | When triggered | Description |
|----------|------|---------------|-------------|
| `ERROR_MISC` | 1 | Generic rejection | Miscellaneous error — action not possible here |
| `ERROR_GROUND` | 2 | Wrong terrain | Floor type is not suitable for this action |
| `ERROR_FREE` | 3 | Cell occupied | Target cell is blocked by an object or character |
| `ERROR_PONTOP` | 4 | Bridge blocked | Bridge: the cell on the opposite bank is blocked |
| `ERROR_PONTTERM` | 5 | Bridge: no terminus | Bridge: no valid terminus cell found in that direction |
| `ERROR_TOURISOL` | 6 | Tower: not on land | Watchtower must be built on dry land |
| `ERROR_TOUREAU` | 7 | Tower: not by water | Watchtower must be adjacent to water |
| `ERROR_TELE2` | 8 | No second teleporter | Teleporter: no matching partner teleporter found |

---

## Usage

```cpp
int CDecor::CelOkForAction(POINT cel, int action, int rank)
// Returns:
//   0   → action is valid at this cell
//   1–8 → ERROR_* code explaining why not valid

// If an error is returned, CEvent shows ICON_HILI_ERR at the cell
// and optionally a localised error string (TX_* resource)
```

---

## Error Display

Error messages are shown as in-game tooltip text using the `CHTEXT` font.
The text content comes from string resources (Win32 `LoadString()` with `TX_*` IDs
defined in `include/resource.h`).
