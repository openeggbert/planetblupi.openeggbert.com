# Web (Emscripten) Build & Persistence

## Overview

The Web build compiles Planet Blupi to WebAssembly using Emscripten.
Save games are persisted in the browser's **IndexedDB** via Emscripten's
IDBFS (IndexedDB File System) virtual filesystem.

Implementation: `src/web_persistence.cpp`

---

## Save Game Persistence

Two C functions are exported to JavaScript for IndexedDB synchronisation:

```c
// Flush in-memory save files to IndexedDB:
EMSCRIPTEN_KEEPALIVE void PlanetBlupi_ExportPersistentData();

// Load save files from IndexedDB into the virtual filesystem:
EMSCRIPTEN_KEEPALIVE void PlanetBlupi_ImportPersistentData();
```

From JavaScript:
```javascript
// Export (flush saves to IndexedDB):
Module.ccall('PlanetBlupi_ExportPersistentData', null, [], []);

// Import (restore saves from IndexedDB):
Module.ccall('PlanetBlupi_ImportPersistentData', null, [], []);
```

---

## How It Works

```
Game write (CDecor::Write)
    → writes to IDBFS virtual filesystem (in-memory)
    → PlanetBlupi_ExportPersistentData() called
        → FS.syncfs(false, callback)  ← flushes to IndexedDB

Game read (CDecor::Read)
    → PlanetBlupi_ImportPersistentData() called first
        → FS.syncfs(true, callback)   ← loads from IndexedDB
    → reads from IDBFS virtual filesystem
```

---

## Limitations in Web Build

| Feature | Status |
|---------|--------|
| Save/load games | Works (via IndexedDB) |
| MIDI music | **Not supported** — MCI API unavailable |
| AVI movies | **Not supported** — MCI API unavailable; `.blp` fallback images shown |
| Full-screen mode | Works via Emscripten canvas fullscreen |

---

## Data Reset

Clearing browser site data (cookies, storage) deletes all save games.
There is no built-in export/import of saves from the browser.

---

## Build Commands

```bash
# Configure:
emcmake cmake -S . -B build-web

# Build:
cmake --build build-web
```

The output is a `.html` + `.js` + `.wasm` bundle that can be served
from any static web server.
