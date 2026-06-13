# Movie Sequences

## Overview

AVI video files for in-game cinematics are played via `CMovie` / Windows MCI.
Each AVI file has a matching `.blp` thumbnail/still image used as a fallback
when the movie cannot be played (e.g. in Web/Emscripten builds).

> **Note**: AVI playback does not work in the Web (Emscripten) build.
> The `.blp` thumbnails are displayed instead.

---

## Movie Files (`movie/` directory)

| Pattern | Description |
|---------|-------------|
| `play101.avi` / `play101.blp` | Mission briefing movie for world 101 |
| `play*.avi` / `play*.blp` | Mission briefing movies (shown before specific worlds) |
| `win005.avi` / `win005.blp` | Victory cinematic for world 005 |
| `win129.avi` / `win129.blp` | Victory cinematic for milestone world 129 |
| `history2.avi` / `history2.blp` | Story / history chapter 2 cinematic |

---

## Playback

```cpp
class CMovie {
public:
    BOOL Play(HWND hWnd, const char* filename);
    void Stop();
    BOOL IsOver();  // returns TRUE when playback ended
};
```

`CMovie` wraps the Windows MCI API (`mciSendCommand` with `MCI_OPEN`, `MCI_PLAY`, etc.).

---

## Phase Integration

Movies are triggered during phase transitions:
- `WM_PHASE_PLAYMOVIE` (+513) — plays a pre-mission briefing movie
- `WM_PHASE_WINMOVIE` (+514) — plays a victory cinematic
- `WM_PHASE_H0MOVIE`/`H1MOVIE`/`H2MOVIE` (+525–527) — story chapter movies

When a movie ends (`CMovie::IsOver()` returns TRUE), `CEvent` automatically
transitions to the next phase via `PostMessage(g_hWnd, WM_NEXT, 0, 0)`.
