# Demo Recording & Playback

## Overview

The engine supports recording and replaying gameplay.
Demo files are stored as `data/demo000.blp` … `data/demo003.blp` (4 slots).

Implementation: `src/event.cpp`

---

## Data Structures

```cpp
struct DemoHeader {
    short version;   // demo format version
    short world;     // world number (mission)
    short skill;     // difficulty (0=easy, 1=normal, 2=hard)
    short flags;     // mode flags
};

struct DemoEvent {
    int    time;     // event time in ms from demo start
    UINT   message;  // Windows message (WM_LBUTTONDOWN, WM_MOUSEMOVE, WM_ACTION_*, etc.)
    WPARAM wParam;   // message parameter
    LPARAM lParam;   // message parameter (usually encodes mouse position)
};
```

---

## Recording

```cpp
void CEvent::DemoRecStart();
// Starts recording:
// - Sets m_bDemoRec = TRUE
// - Writes DemoHeader to buffer
// - Saves the initial world state

void CEvent::DemoRecStop();
// Ends recording:
// - Writes recorded DemoEvent[] to demo000.blp etc.
// - Sets m_bDemoRec = FALSE
```

During recording, all relevant input messages (clicks, mouse moves,
toolbar button presses) are captured into `DemoEvent[]` with timestamps.

---

## Playback

```cpp
void CEvent::DemoPlayStart();
// Starts demo playback:
// - Loads DemoHeader and verifies world + difficulty
// - Loads world file (initial state)
// - Sets m_bDemoPlay = TRUE

void CEvent::DemoStep();
// Called every tick:
// - Compares current time with timestamp of next DemoEvent
// - When it is time for an event, injects it into the message loop (PostMessage)
// - Simulates user input exactly as during the original recording
```

---

## Demo Phase

Demo playback runs in the `WM_PHASE_DEMO` phase. After the demo ends,
the game returns to the main menu or shows the intro screen.

---

## Limitations

- A demo is tied to a specific world and difficulty — different settings cause desynchronisation
- The deterministic game engine (same seed, same results) is a prerequisite for demo functionality
- During playback, user input is ignored (`m_bDemoPlay = TRUE`)
