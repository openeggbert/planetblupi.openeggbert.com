# Build System

## Overview

The project uses **CMake** with optional third-party submodules providing
the Windows API compatibility layer.

---

## Directory Structure

```
CMakeLists.txt
cmake/
└── ThirdPartySDL.cmake      ← SDL3 integration
third_party/
├── SDL/                     ← SDL3 (windowing, input, audio)
├── SDL_image/               ← BLP image loading
└── SDL_mixer/               ← audio mixing
```

---

## Build Targets

| Target | How to build |
|--------|-------------|
| **Linux / Desktop** | `cmake -S . -B build && cmake --build build` |
| **Web (Emscripten)** | `emcmake cmake -S . -B build-web && cmake --build build-web` |
| **Android** | See `ANDROID.md` |
| **Windows** | Visual Studio: open `planetblupi.sln`, or CMake with MSVC |

The main executable is named `PLANET_BLUPI_WINDOWS` (name kept for compatibility).

---

## Dependencies

| Library | Purpose |
|---------|---------|
| SDL3 | Window creation, input handling, timing, 2D rendering surface |
| SDL_image | Loading BLP image files (Epsitec format) |
| SDL_mixer | Audio mixing for WAV sound effects |
| [Free Direct](https://github.com/openeggbert/free-direct) | DirectDraw/DirectSound → SDL3 wrapper |
| [Free API](https://github.com/openeggbert/free-api) | Win32 API → cross-platform wrapper |

---

## Compatibility Layer Architecture

```
Planet Blupi source code
        │
        │ uses Win32 API + DirectX API
        │
Free API + Free Direct (wrapper layer)
        │
        │ implements Win32/DirectX calls using:
        │
SDL3 + SDL_image + SDL_mixer
        │
        │ runs on:
        │
Linux / Web (Emscripten) / Android / Windows
```

---

## Platform Notes

### Windows
Native build using Visual Studio solution (`planetblupi.sln`, `planetblupi.vcxproj`).
DirectDraw and DirectSound run natively without the compatibility layer.

### Linux
Requires the Free Direct / Free API layer. SDL3 provides windowing and audio.

### Web (Emscripten)
- Uses Emscripten SDK (`emcmake`, `emmake`)
- MIDI music **does not work** (MCI API unavailable)
- AVI movies **do not work** (MCI API unavailable)
- Save games use IndexedDB via IDBFS — see [Web Persistence](web.md)

### Android
Experimental. See `ANDROID.md` for platform-specific build instructions.
