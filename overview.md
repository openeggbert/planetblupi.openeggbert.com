# Planet Blupi — Game Overview

## What Is Planet Blupi?

**Planet Blupi** is a real-time strategy / puzzle-adventure game developed by
Swiss company **Epsitec SA**, originally released in **1997** for Windows.
Epsitec later open-sourced the game.

The player controls one or more **Blupi** — small yellow creatures — on a
**200×200 isometric grid**. The goal is to build infrastructure, gather
resources, and satisfy mission-specific win conditions while fending off
enemies (spiders, viruses, robots, tanks, electro towers).

---

## Gameplay Pillars

| Pillar | Description |
|--------|-------------|
| **Build** | Construct huts, laboratories, factories, fences, towers, boats, jeeps, armour |
| **Gather** | Chop wood, mine stone / iron ore, pick flowers, cultivate crops |
| **Defend** | Fight spiders, viruses, robots, tanks using dynamite, mines, armour |
| **Complete missions** | Each world file embeds a `Term` struct with win conditions |

---

## Technical Summary

| Property | Value |
|----------|-------|
| **Language** | C++ (ISO C++98 style, Win32 API) |
| **Original engine** | Win32 / DirectDraw / DirectSound / MCI (AVI) |
| **Compatibility layer** | [Free Direct](https://github.com/openeggbert/free-direct) (DirectDraw/DirectSound → SDL3), [Free API](https://github.com/openeggbert/free-api) (Win32 → cross-platform) |
| **Platforms** | Windows (original), Linux (ported), Web/Emscripten (ported), Android (experimental) |
| **Resolution** | Fixed 640×480 pixels |
| **Colour depth** | 8-bit palette (256 colours) on original hardware; 32-bit via SDL3 layer |
| **Grid** | 200×200 cells (isometric projection) |
| **Cell size** | 60×30 pixels in isometric projection |

---

## Main Game Loop

```
WinMain()
  │
  ├─ initialise (CEvent, CDecor, CSound, CPixmap, CMovie)
  │
  └─ Windows message loop
        │
        ├─ WM_TIMER → CEvent::Step()
        │     ├─ CDecor::BlupiStep()   ← character logic (1 tick = 50 ms)
        │     ├─ CDecor::MoveStep()    ← decoration animations
        │     └─ redraw scene
        │
        ├─ WM_LBUTTONDOWN / WM_MOUSEMOVE / WM_LBUTTONUP
        │     └─ CEvent::EventPos() → cell selection, action trigger
        │
        └─ WM_PHASE_* → CEvent::ChangePhase() → screen switch
```

The game tick is driven by a timer with an interval of **50 ms** (configurable via
`Timer=` in `config.def`). Each tick calls `BlupiStep()` and `MoveStep()` once.

---

## Coordinate System

The game uses an isometric projection. Relationship between grid and screen coordinates:

```
Game window: 640×480 px
Drawing surface: 480×450 px, offset (144, 15) from top-left corner

Grid cell (cel.x, cel.y)  →  screen pixel (px, py):
  px = (cel.x - celCoin.x) * DIMCELX/2 - (cel.y - celCoin.y) * DIMCELX/2 + POSDRAWX + DIMDRAWX/2
  py = (cel.x - celCoin.x) * DIMCELY/2 + (cel.y - celCoin.y) * DIMCELY/2 + POSDRAWY

Functions:
  CDecor::ConvCelToPos(cel)   → pixel position
  CDecor::ConvPosToCel(pos)   → grid cell
```

`m_celCoin` holds the cell at the top-left corner of the visible viewport (scroll position).

---

## Key Constants

```cpp
LXIMAGE    = 640    // game window width
LYIMAGE    = 480    // game window height

POSDRAWX   = 144   // x-offset of game drawing area
POSDRAWY   = 15    // y-offset of game drawing area
DIMDRAWX   = 480   // width of game drawing area
DIMDRAWY   = 450   // height of game drawing area

POSMAPX    = 8     // minimap x position
POSMAPY    = 15    // minimap y position
DIMMAPX    = 128   // minimap width
DIMMAPY    = 128   // minimap height

MAXCELX    = 200   // grid width (cells)
MAXCELY    = 200   // grid height (cells)

DIMCELX    = 60    // cell width in pixels
DIMCELY    = 30    // cell height in pixels

DIMOBJX    = 120   // max object sprite width
DIMOBJY    = 120   // max object sprite height

DIMBLUPIX  = 60    // Blupi sprite width
DIMBLUPIY  = 60    // Blupi sprite height
SHIFTBLUPIY = 5    // Blupi upward shift (z-order correction)

DIMBUTTONX = 40    // toolbar button width
DIMBUTTONY = 40    // toolbar button height

POSSTATX   = 12    // statistics panel x position
POSSTATY   = 220   // statistics panel y position

MAXBLUPI   = 100   // max simultaneous characters (Blupi + all enemies)
MAXMOVE    = 100   // max simultaneous animated decorations
MAXBUTTON  = 40    // max toolbar buttons
MAXUSED    = 50    // max visited cells remembered per character
MAXLIST    = 10    // max queued commands per character

MAXENERGY  = 4000  // maximum Blupi energy
MAXFIRE    = 400   // maximum fire intensity

FOGHIDE    = 4     // fog icon threshold below which cell is hidden
```
