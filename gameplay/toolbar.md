# Toolbar Buttons (BUTTON_*)

## Overview

Action buttons are defined in `include/def.h` as `BUTTON_*` constants.
Up to `MAXBUTTON=40` buttons populate the right-hand toolbar during play mode.
Which buttons are available depends on the mission (`buttonExist[]` in `DescFile`).

When the player clicks a toolbar button, it sends `WM_BUTTON0`–`WM_BUTTON39`
(WM_USER+200 through WM_USER+239), which `CEvent` converts to a `WM_ACTION_*`
message based on the selected Blupi and target cell.

---

## All Button Types

| Constant | Code | Action | Required resource/condition |
|----------|------|--------|-----------------------------|
| `BUTTON_GO` | 0 | Move Blupi to target cell | — |
| `BUTTON_STOP` | 1 | Stop Blupi immediately | — |
| `BUTTON_MANGE` | 2 | Eat nearby food | Food (tomato) nearby |
| `BUTTON_CARRY` | 3 | Pick up object | Object at target cell |
| `BUTTON_DEPOSE` | 4 | Put down carried object | Blupi carrying something |
| `BUTTON_ABAT` | 5 | Chop down tree (with replant) | Tree at target cell |
| `BUTTON_ROC` | 6 | Mine rock / stone | Rock at target cell |
| `BUTTON_CULTIVE` | 7 | Cultivate / tend crops | Cultivatable plot |
| `BUTTON_BUILD1` | 8 | Build construction type 1 (hut) | Free cells, resources |
| `BUTTON_BUILD2` | 9 | Build construction type 2 (laboratory) | Free cells, resources |
| `BUTTON_BUILD3` | 10 | Build construction type 3 (factory) | Free cells, resources |
| `BUTTON_BUILD4` | 11 | Build construction type 4 (incubator) | Free cells, resources |
| `BUTTON_BUILD5` | 12 | Build construction type 5 | Free cells, resources |
| `BUTTON_BUILD6` | 13 | Build construction type 6 | Free cells, resources |
| `BUTTON_MUR` | 14 | Build wall (mur) | Free cell, stone |
| `BUTTON_PALIS` | 15 | Build palisade / fence | Free cell, planks |
| `BUTTON_ABATn` | 16 | Chop tree (no replant) | Tree at target cell |
| `BUTTON_ROCn` | 17 | Mine rock (no replacement) | Rock at target cell |
| `BUTTON_PONT` | 18 | Build bridge | Water cell, planks |
| `BUTTON_TOUR` | 19 | Build watchtower | Adjacent water, stone |
| `BUTTON_BOIT` | 20 | Drink potion | Potion nearby |
| `BUTTON_LABO` | 21 | Use laboratory | Laboratory built |
| `BUTTON_FLEUR` | 22 | Pick flowers (with replant) | Flowers at cell |
| `BUTTON_FLEURn` | 23 | Pick flowers (no replant) | Flowers at cell |
| `BUTTON_DYNAMITE` | 24 | Place dynamite at cell | Dynamite in inventory |
| `BUTTON_BATEAU` | 25 | Board / disembark boat | Boat adjacent, or in boat |
| `BUTTON_DJEEP` | 26 | Board / disembark jeep | Jeep adjacent, or in jeep |
| `BUTTON_DRAPEAU` | 27 | Place flag waypoint at cell | — |
| `BUTTON_EXTRAIT` | 28 | Extract iron ore | Iron mine at cell |
| `BUTTON_FABJEEP` | 29 | Manufacture jeep | Factory, iron |
| `BUTTON_FABMINE` | 30 | Manufacture mine | Factory, materials |
| `BUTTON_FABDISC` | 31 | Create disciple | Factory, materials |
| `BUTTON_REPEAT` | 32 | Repeat last action | Previous action queued |
| `BUTTON_DARMURE` | 33 | Board / disembark armour | Armour adjacent, or in armour |
| `BUTTON_FABARMURE` | 34 | Manufacture armour | Factory, iron |

---

## Button Availability (`buttonExist`)

The `buttonExist[MAXBUTTON]` array (stored in `DescFile`) controls which buttons
appear in the toolbar. A value of `1` means available, `0` means hidden.

Mission designers set which buttons are available, restricting player options
to match the intended challenge. Early tutorial missions typically only show
`BUTTON_GO` and `BUTTON_ABAT`.

```cpp
char* CDecor::GetButtonExist();
// Returns pointer to m_buttonExist[] — used by CEvent to build the toolbar
```

---

## Button-to-Action Mapping

When a toolbar button is clicked and Blupi is selected at a target cell,
`CEvent` sends the appropriate `WM_ACTION_*` message:

| Button | → WM_ACTION (simplified) |
|--------|--------------------------|
| `BUTTON_GO` | `WM_ACTION_GO` |
| `BUTTON_ABAT` | `WM_ACTION_ABAT1`–`ABAT6` (depends on tree type) |
| `BUTTON_ROC` | `WM_ACTION_ROC1`–`ROC7` (depends on rock type) |
| `BUTTON_BUILD1` | `WM_ACTION_BUILD1` |
| `BUTTON_PONT` | `WM_ACTION_PONTE/S/O/N[L]` (direction detected) |
| `BUTTON_BATEAU` | `WM_ACTION_BATEAUAE/AS/AO/AN` or `BATEAUDE/DS/DO/DN` |
| `BUTTON_DJEEP` | `WM_ACTION_MJEEP` or `WM_ACTION_DJEEP` |
| `BUTTON_FABDISC` | `WM_ACTION_FABDISC` |

`CDecor::CelOkForAction(cel, action, rank)` validates whether the target cell
is suitable for the given button action and returns an error code if not.

---

## Error Feedback

If a button action cannot be performed, an error highlight is shown:
- `ICON_HILI_ERR` (119) — red error cell highlight
- A brief tooltip message (from `ERROR_*` codes) is displayed

See [Error Codes](../ui/error-codes.md) for the full list.

---

## Default Button Determination

`CDecor::GetDefButton(POINT cel)` returns the default button action for
a given cell (used for double-click or right-click action).

`CDecor::BlupiGetButtons(POINT pos, int &nb, int *pButtons, int *pErrors, int &perso)`
returns the list of available buttons for the Blupi / cell at the screen position.
