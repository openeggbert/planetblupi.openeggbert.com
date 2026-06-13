# Source Files Reference

## Header Files (`include/`)

| File | Contents |
|------|---------|
| `def.h` | **Central constants**: window dimensions, image channels, `DIRECT_*` directions, `ACTION_*` animation codes, `SOUND_*` indices, `BUTTON_*` button IDs, `ERROR_*` codes, `SPRITE_*` cursor IDs, `WM_*` messages, `Term` struct |
| `decor.h` | `CDecor` class; `Cellule`, `Blupi`, `Move` structs; defines MAXBLUPI=100, MAXMOVE=100, MAXENERGY=4000 |
| `decgoal.h` | `GOAL_*` opcodes (0–49) for the task interpreter; declares `GetTableGoal()` and `table_goal_nbop[]` |
| `decmove.h` | Icon and movement tables for animated decorations; index declarations |
| `action.h` | Declaration of `CDecor::Action()` — per-frame animation step function (not the same as `actions.h`!) |
| `actions.h` | **Speedy Blupi legacy**: bytecode opcodes (`OPTERM`/`OPLIST`/`OPREPEAT`/`OPSOUND`), `Action`, `Objet`, `Sound` enums for the Speedy Blupi engine |
| `button.h` | `CButton` class — toolbar button widget |
| `ddutil.h` | DirectDraw bitmap utility (MS SDK sample) |
| `event.h` | `CEvent` class — phase manager, input routing, demo, buildmode; `DemoHeader`, `DemoEvent` structs |
| `fifo.h` | `CPileTriee` class — min-heap for A* open list |
| `jauge.h` | `CJauge` class — energy/progress gauge widget |
| `menu.h` | `CMenu` class — context popup menu widget |
| `misc.h` | Utility functions: file paths, random numbers, error reporting |
| `movie.h` | `CMovie` class — MCI AVI player |
| `pixmap.h` | `CPixmap` class — DirectDraw sprite renderer with channel system |
| `resource.h` | String resource IDs (`TX_*`) for `LoadString()` |
| `resrc1.h` | Additional resource IDs |
| `sound.h` | `CSound` class — DirectSound + MIDI playback |
| `text.h` | Sprite-based text rendering functions |
| `wave.h` | `LoadWave()` — load WAV from Win32 resource |

---

## Source Files (`src/`)

| File | Purpose and key functions |
|------|--------------------------|
| `blupi.cpp` | Win32 `WinMain`, `WindowProc`, global variables, initialisation, timer. Creates CEvent, CDecor, CSound, CPixmap, CMovie. |
| `action.cpp` | `CDecor::Action()` — per-frame animation step; sprite and sound tables for each ACTION_* value; maps action+direction → icon sequence. |
| `arrange.cpp` | Auto-tiling and flood-fill. `ArrangeFloor()` adapts floor tiles to neighbours (water, grass, ice). `ArrangeMur()` and `ArrangeBuild()` for walls and buildings. `ArrangeFill()` for flood-fill. |
| `button.cpp` | `CButton::Create()`, `Paint()`, `Test()` — rendering and click detection for toolbar buttons. |
| `chemin.cpp` | A* pathfinding. `CheminFillTerrain()` builds obstacle bitmap; `CheminCherche()` runs the search; `CheminARebours()` reconstructs the path. |
| `ddutil.cpp` | `DDCopyBitmap()` etc. — bitmap copy utilities (MS SDK sample). Does not affect game logic. |
| `decblupi.cpp` | Largest source file. Complete character lifecycle: `BlupiCreate()`, `BlupiDelete()`, `BlupiKill()`, `BlupiNextAction()`, `BlupiNextGoal()`, `GoalNextOp()`, selection, highlight, pathfinding calls. |
| `decgoal.cpp` | Static tables `table_goal_*[]` — opcode sequences for each of 130+ WM_ACTION_* actions. `GetTableGoal()` returns a pointer to the table for a given action. |
| `decio.cpp` | `CDecor::Write()` — binary write of world state to `.blp`. `CDecor::Read()` — binary read. Contains `DescFile` header struct and `OldBlupi` (backward compatibility). |
| `decmap.cpp` | `GenerateMap()` — creates 128×128 colour minimap image from cell data. `MapMove()` — minimap click scrolls viewport. `ConvCelToMap()` / `ConvMapToCel()` — coordinate conversion. |
| `decmove.cpp` | `MoveCreate()` — creates animated decoration. `MoveStep()` — advances animation one step. `MoveFire()` / `MoveProxiFire()` — fire spreading. `tableMoves[]` and `tableIcons[]`. |
| `decor.cpp` | CDecor core: `Create()`, `Init()`, `ConvCelToPos()`, `ConvPosToCel()`, `PutFloor()`, `PutObject()`, `GetFloor()`, `GetObject()`, `Build()`, `BuildGround()`, `UndoOpen/Close/Copy/Back()`. |
| `decstat.cpp` | `StatisticUpdate()` — recalculates statistics from world state. `StatisticDraw()` — renders panel. `StatisticDown/Move/Up()` — click/hover on statistics panel. |
| `event.cpp` | `CEvent::Create()`, `ChangePhase()`, `EventPos()`, `EventButton()`. Phase management, WM_ message routing, demo: `DemoRecStart/Stop()`, `DemoPlayStart()`, `DemoStep()`. |
| `fifo.cpp` | `CPileTriee::put()` / `get()` / `remove()` — min-heap for A* open list sorted by cumulative cost. |
| `fog.cpp` | `GetFogBits()` / `GetFogIcon()` — fog encoding/decoding (15 icons × 4 quadrants). `tableFog[15*4]`. |
| `jauge.cpp` | `CJauge::Create()`, `SetLevel()`, `Draw()` — energy or progress indicator widget. |
| `menu.cpp` | `CMenu::Create()`, `AdjustPos()`, `Draw()`, `Detect()` — context menu for selecting an action by clicking on a character. |
| `misc.cpp` | `AddCDPath()`, `AddUserPath()`, `GetRandom()`, `Trace()`, `DisplayError()`. |
| `movie.cpp` | `CMovie::Play()`, `Stop()`, `IsOver()` — wraps MCI API to play AVI cinematics. |
| `obstacle.cpp` | `tableObstacleFloor[]` / `tableObstacleObject[]` — passability bitmaps. `IsFreeCel()`, `SearchBestBase()`, `SearchOtherObject()`, `SearchSpiderObject()` etc. |
| `pixmap.cpp` | `CPixmap::Cache()` — loads `.blp` image into a channel. `Draw()` / `DrawIcon()` — renders an icon from a channel. `DrawSprite()` — mouse cursor. |
| `sound.cpp` | `CSound::Cache()` — loads PCM WAV. `Play()`, `PlayMusic()`, `StopMusic()`. Wraps DirectSound buffers and MIDI playback. |
| `tablefloor.cpp` | `tableFloor[]` — default floor layout for level editor (empty map). |
| `tableobj.cpp` | `tableObj[]` — default object layout for level editor. |
| `text.cpp` | `DrawText()` / `DrawBignum()` / `DrawLittle()` — renders text using sprite-based fonts. |
| `wave.cpp` | `LoadWave()` — loads WAV file from resource or filesystem. |
| `web_persistence.cpp` | `PlanetBlupi_ExportPersistentData()` / `PlanetBlupi_ImportPersistentData()` — sync save games with IndexedDB via Emscripten IDBFS. |
