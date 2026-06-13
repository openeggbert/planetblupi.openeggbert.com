# Game Phases (Screens)

## Overview

Each phase corresponds to a `WM_PHASE_*` Windows message. The active phase determines
which background image, buttons, and event handlers are active. A phase switch is triggered
by sending `WM_PHASE_*` to the window, caught by `CEvent::ChangePhase()`.

---

## Complete Phase Table

| Constant | Value (WM_USER+) | Description |
|----------|-----------------|-------------|
| `WM_PHASE_INIT` | +500 | Startup initialisation |
| `WM_PHASE_PLAY` | +501 | **Main gameplay** (play mode) — most important phase |
| `WM_PHASE_BUILD` | +502 | Level editor / build mode |
| `WM_PHASE_READ` | +503 | Load-game screen (10 slots) |
| `WM_PHASE_WRITE` | +504 | Save-game screen (10 slots) |
| `WM_PHASE_INFO` | +505 | Mission briefing (goal description) |
| `WM_PHASE_BUTTON` | +506 | Action selection via button strip |
| `WM_PHASE_TERM` | +507 | Mission-end statistics |
| `WM_PHASE_WIN` | +508 | Victory screen |
| `WM_PHASE_LOST` | +509 | Defeat screen |
| `WM_PHASE_STOP` | +510 | Pause / stop |
| `WM_PHASE_SETUP` | +511 | Settings screen |
| `WM_PHASE_MUSIC` | +512 | Music selection screen |
| `WM_PHASE_PLAYMOVIE` | +513 | Pre-mission cinematic |
| `WM_PHASE_WINMOVIE` | +514 | Victory cinematic |
| `WM_PHASE_SCHOOL` | +515 | Tutorial / school mission selection |
| `WM_PHASE_MISSION` | +516 | Main campaign mission selection |
| `WM_PHASE_LASTWIN` | +517 | Final victory screen (game completed) |
| `WM_PHASE_WRITEp` | +518 | Save-game from pause |
| `WM_PHASE_SETUPp` | +519 | Settings from pause |
| `WM_PHASE_REGION` | +520 | Region / visual theme selection |
| `WM_PHASE_INSERT` | +521 | CD-ROM insert prompt |
| `WM_PHASE_HISTORY0` | +522 | Story history screen 0 |
| `WM_PHASE_HISTORY1` | +523 | Story history screen 1 |
| `WM_PHASE_HELP` | +524 | In-game help overlay |
| `WM_PHASE_H0MOVIE` | +525 | Story chapter 0 cinematic |
| `WM_PHASE_H1MOVIE` | +526 | Story chapter 1 cinematic |
| `WM_PHASE_H2MOVIE` | +527 | Story chapter 2 cinematic |
| `WM_PHASE_TESTCD` | +528 | CD-ROM access test |
| `WM_PHASE_MANUEL` | +529 | Manual / help document |
| `WM_PHASE_PRIVATE` | +530 | Private / special phase |
| `WM_PHASE_UNDO` | +531 | Undo operation |
| `WM_PHASE_BYE` | +532 | Quit confirmation |
| `WM_PHASE_SKILL1` | +533 | Skill level selection — screen 1 |
| `WM_PHASE_SKILL2` | +534 | Skill level selection — screen 2 |
| `WM_PHASE_DEMO` | +535 | Demo playback |
| `WM_PHASE_INTRO1` | +536 | Introduction animation — screen 1 |
| `WM_PHASE_INTRO2` | +537 | Introduction animation — screen 2 |

---

## Typical Phase Flow for One Mission

```
WM_PHASE_INIT
    → WM_PHASE_INTRO1 / WM_PHASE_INTRO2   (intro animation, first run only)
    → WM_PHASE_SKILL1 / WM_PHASE_SKILL2   (difficulty selection)
    → WM_PHASE_REGION                      (visual theme selection)
    → WM_PHASE_SCHOOL or WM_PHASE_MISSION  (mission selection)
    → WM_PHASE_INFO                        (mission briefing)
    → WM_PHASE_PLAYMOVIE                   (pre-mission cinematic)
    → WM_PHASE_PLAY                        (gameplay!)
        ↓ (during play)
        WM_PHASE_STOP → WM_PHASE_PLAY      (pause and resume)
        WM_PHASE_HELP → WM_PHASE_PLAY      (help overlay)
        ↓ (mission end)
    → WM_PHASE_WIN or WM_PHASE_LOST
    → WM_PHASE_WINMOVIE                    (victory cinematic)
    → WM_PHASE_TERM                        (mission statistics)
    → WM_PHASE_MISSION                     (select next mission)
```

---

## How Phase Switching Works

```cpp
// Send message to trigger a phase switch:
PostMessage(g_hWnd, WM_PHASE_PLAY, 0, 0);

// Handled in WindowProc:
case WM_PHASE_PLAY:
    pEvent->ChangePhase(WM_PHASE_PLAY);
    break;

// ChangePhase() in event.cpp:
// 1. Clears current toolbar (buttons, gauges)
// 2. Loads the appropriate background image into CHBACK channel
// 3. Creates phase-specific buttons
// 4. Initialises phase state
```

---

## Navigation Messages

| Constant | Value | Description |
|----------|-------|-------------|
| `WM_PREV` | WM_USER+600 | Go to previous item / page |
| `WM_NEXT` | WM_USER+601 | Go to next item / page |
| `WM_MOVIE` | WM_USER+602 | Start cinematic playback |

---

## Background Images per Phase

| Phase | Background image |
|-------|----------------|
| `WM_PHASE_PLAY` | `image/play.blp` |
| `WM_PHASE_BUILD` | `image/build.blp` |
| `WM_PHASE_READ` | `image/read.blp` |
| `WM_PHASE_WRITE` | `image/write.blp` |
| `WM_PHASE_WIN` | `image/win.blp` |
| `WM_PHASE_LOST` | `image/lost.blp` |
| `WM_PHASE_STOP` | `image/stop000.blp` / `stop001.blp` / `stop002.blp` |
| `WM_PHASE_SETUP` | `image/setup.blp` |
| `WM_PHASE_MUSIC` | `image/music.blp` |
| `WM_PHASE_REGION` | `image/region.blp` |
| `WM_PHASE_TERM` | `image/term.blp` |
| `WM_PHASE_HELP` | `image/help.blp` |
| `WM_PHASE_BYE` | `image/bye.blp` |
| `WM_PHASE_INTRO1` | `image/intro1.blp` |
| `WM_PHASE_INTRO2` | `image/intro2.blp` |
| `WM_PHASE_HISTORY0` | `image/history0.blp` |
| `WM_PHASE_HISTORY1` | `image/history1.blp` |
| `WM_PHASE_LASTWIN` | `image/last000.blp` / `last001.blp` / `last002.blp` |
| `WM_PHASE_INSERT` | `image/insert.blp` |
| Any movie phase | `image/movie.blp` (fallback when AVI unavailable) |
