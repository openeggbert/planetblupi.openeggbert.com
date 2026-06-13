# Planet Blupi — Technical Documentation

This documentation describes the internal workings of **Planet Blupi** (Epsitec SA, 1997).
It is aimed at developers working with this codebase or reverse-engineering related games
(especially Speedy Blupi, which is authored by the same team and shares core design).

---

## Table of Contents

### Overview
- [Game Overview](overview.md) — what is Planet Blupi, technical summary, gameplay pillars
- [History & Relation to Speedy Blupi](history.md) — origin, fork context, shared code

### Architecture
- [System Architecture](architecture/overview.md) — class diagram, subsystem relationships, tick lifecycle
- [Source Files Reference](architecture/source-files.md) — every .cpp/.h file explained

### Engine Internals
- [Data Structures](engine/data-structures.md) — `Cellule`, `Blupi`, `Move`, `Term`, `DescFile` in full detail
- [Game Phases (Screens)](engine/game-phases.md) — `WM_PHASE_*` messages, screen lifecycle, flow diagram
- [Rendering](engine/rendering.md) — image channels, coordinate system, draw order, `CPixmap`
- [Pathfinding (A*)](engine/pathfinding.md) — `CPileTriee`, `CheminCherche()`, obstacle tables
- [Fog of War](engine/fog-of-war.md) — quadrant bit encoding, 15 fog patterns, API
- [Minimap](engine/minimap.md) — generation, colour coding, click-to-scroll
- [Demo Recording & Playback](engine/demo.md) — `DemoHeader`, `DemoEvent`, replay mechanism
- [Undo System](engine/undo.md) — single-step undo in the level editor

### World (Map)
- [World File Format (.blp)](world/file-format.md) — binary layout, `DescFile` header, versioning
- [World Grid](world/grid.md) — 200×200 cells, coordinate system, viewport, scrolling
- [Terrain & Auto-tiling](world/terrain.md) — floor tiles, regions, `arrange.cpp`, tableSee
- [Object Layer](world/objects.md) — object categories, channels, passability

### Characters
- [Character Overview (Blupi struct)](characters/overview.md) — every field of the `Blupi` structure
- [Player Character (Blupi)](characters/blupi.md) — energy, spawning, selection, idle animations
- [Enemies](characters/enemies.md) — spider, virus, tracks, robot, bomb, electro — AI & behaviour
- [Vehicles](characters/vehicles.md) — boat, jeep, armour — boarding, movement, exits
- [Animation Actions (ACTION_*)](characters/actions.md) — all codes for all character types
- [Task Interpreter (GOAL_*)](characters/goals.md) — all opcodes, parameters, `GoalNextOp()`, WM_ACTION_* mapping

### Gameplay
- [Win Conditions (Term)](gameplay/win-conditions.md) — `Term` struct, `IsTerminated()`
- [Toolbar Buttons (BUTTON_*)](gameplay/toolbar.md) — all 35 actions, WM_ACTION_* mapping
- [Movement Directions (DIRECT_*)](gameplay/directions.md) — 8-direction system, GetVector()
- [Skill Levels](gameplay/skill-levels.md) — easy / normal / hard
- [Regions (World Themes)](gameplay/regions.md) — 4 visual themes, sprite sheet swap
- [Cheat Codes](gameplay/cheat-codes.md) — invincible, super

### Assets
- [Image Assets](assets/images.md) — all .blp images, channels CHBACK–CHBIGNUM
- [Sound Effects (SOUND_*)](assets/sounds.md) — all 85 SFX with descriptions
- [Music Tracks](assets/music.md) — 10 MIDI tracks
- [Data Files](assets/data-files.md) — `data/` directory, mission numbering
- [Movie Sequences](assets/movies.md) — AVI files, fallback images

### User Interface
- [Windows Messages (WM_*)](ui/messages.md) — complete WM_ACTION_*, WM_BUTTON_*, WM_PHASE_* tables
- [Mouse Cursor Sprites (SPRITE_*)](ui/cursor-sprites.md) — 14 cursor sprites
- [Statistics Panel](ui/statistics.md) — contents, update, rendering
- [Error Codes (ERROR_*)](ui/error-codes.md) — 8 error states

### Platforms
- [Build System](platform/build.md) — CMake, dependencies, target platforms
- [Configuration File](platform/config.md) — `data/config.def`, all keys
- [Localisation](platform/localisation.md) — language packs, string resources
- [Web (Emscripten)](platform/web.md) — IndexedDB persistence, export/import

### Speedy Blupi Reference
- [Relation to Speedy Blupi](speedy-blupi/overview.md) — fork context, shared elements, key differences
- [actions.h Reference](speedy-blupi/actions-h.md) — complete enum listings for decompilation use
