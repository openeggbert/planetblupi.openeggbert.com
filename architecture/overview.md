# System Architecture

## Class Diagram

```
blupi.cpp          ← Win32 WinMain, main message loop, global state
  │
  ├─ CEvent        ← Phase manager, input router, toolbar, demo rec/play
  │    ├─ CButton[]  ← Toolbar buttons (up to 40)
  │    ├─ CJauge[]   ← HUD gauges (energy, progress)
  │    └─ CMenu      ← Context-action popup menu
  │
  ├─ CDecor        ← Game world: grid, characters, animations, I/O
  │    ├─ Cellule[100][100]  ← World tile grid
  │    ├─ Blupi[100]         ← Characters (player + enemies)
  │    ├─ Move[100]          ← Animated decoration elements
  │    ├─ arrange.cpp        ← Auto-tiling
  │    ├─ obstacle.cpp       ← Passability / pathfinding helpers
  │    ├─ decblupi.cpp       ← Character lifecycle & goal interpreter
  │    ├─ decmove.cpp        ← Animated decoration steps & fire spread
  │    ├─ decio.cpp          ← Save/load world files
  │    ├─ decmap.cpp         ← Minimap
  │    ├─ decstat.cpp        ← Statistics panel
  │    ├─ chemin.cpp         ← A* pathfinding (CPileTriee)
  │    └─ decor.cpp          ← Rendering, coordinate transforms, undo
  │
  ├─ CPixmap       ← DirectDraw sprite renderer (image channels)
  ├─ CSound        ← DirectSound audio manager (WAV + MIDI)
  └─ CMovie        ← MCI AVI video player (cinematics)
```

---

## Single Tick Lifecycle

```
WM_TIMER (every 50 ms)
  │
  ├─ CDecor::BlupiStep(bFirst=FALSE)
  │     for each rank 0..MAXBLUPI-1:
  │       BlupiNextAction(rank)   ← animation step, icon update
  │       BlupiNextGoal(rank)     ← advance GOAL_* sequence
  │       BlupiPushFog(rank)      ← fog of war update
  │
  ├─ CDecor::MoveStep(bFirst=FALSE)
  │     for each slot 0..MAXMOVE-1:
  │       advance decoration animation, fire spread
  │
  ├─ CDecor::StatisticUpdate()    ← recalculate stats (if m_bStatRecalc)
  │
  └─ redraw scene
        BuildGround(clip)         ← floor layer
        BuildMoveObject(…)        ← object layer (lower)
        BlupiDrawHili()           ← selection highlight
        BuildMoveObject(…)        ← object layer (upper overlay)
        StatisticDraw()           ← statistics panel
        minimap draw              ← minimap
        HUD draw                  ← gauges, buttons, text
```

---

## Subsystem Dependencies

```
CEvent ─────────────────────→ CDecor (owns instance)
  │                               │
  │                               ├─ CSound* (shared reference)
  │                               └─ CPixmap* (shared reference)
  │
  ├─ CSound* (shared reference)
  ├─ CPixmap* (shared reference)
  └─ CMovie* (owns instance)
```

Global instances declared in `blupi.cpp`:
```cpp
CEvent*   pEvent;
CDecor*   pDecor;
CSound*   pSound;
CPixmap*  pPixmap;
CMovie*   pMovie;
HWND      g_hWnd;
```

---

## CDecor Split Across Translation Units

`CDecor` is a single class distributed across several `.cpp` files for clarity:

| Translation unit | Responsibility |
|-----------------|----------------|
| `decor.cpp` | Creation, init, rendering, coordinate helpers, undo, misc utilities |
| `decblupi.cpp` | Complete character lifecycle, GOAL interpreter, selection, highlight |
| `decgoal.cpp` | Static opcode tables for 130+ action types (WM_ACTION_*) |
| `decio.cpp` | Binary read/write of `.blp` world files |
| `decmap.cpp` | Minimap generation and rendering |
| `decmove.cpp` | Animated decorations, fire spread, icon tables |
| `decstat.cpp` | Statistics panel (Blupi counts, fires, homes, enemies) |
| `arrange.cpp` | Auto-tiling: flood-fill, terrain transitions, walls, buildings |
| `obstacle.cpp` | Passability tables, enemy target search helpers |
| `chemin.cpp` | A* pathfinding with CPileTriee open-list |
| `fog.cpp` | Fog of war quadrant bit encoding/decoding |
