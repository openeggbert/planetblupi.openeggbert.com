# Localisation

## Overview

Planet Blupi is localised for 4 languages. Localisation affects:
1. Voice sound files (WAV audio in `sound/` subdirectories)
2. UI string resources (`resource.h` / `.rc` file)

---

## Voice Sound Packs

Language-specific voice sounds are placed in subdirectories of `sound/`.
They override the base `sound000.blp` … `sound082.blp` files for that language.

| Directory | Language | Files |
|-----------|---------|-------|
| `sound/english/` | English | `sound000.blp`–`sound082.blp` (83 files) |
| `sound/deutsch/` | German | `sound000.blp`–`sound082.blp` (83 files) |
| `sound/francais/` | French | `sound000.blp`–`sound082.blp` (83 files) |
| `sound/us/` | US English | `sound000.blp`–`sound084.blp` (85 files, extended set) |

The active language is selected by `Language=` in `data/config.def`
(`F`=French, `E`=English, `D`=German, `U`=US English).

---

## UI String Resources

UI text (button labels, messages, mission briefing) is stored as Win32 string
resources in the `.rc` file and accessed via `LoadString()` with `TX_*` IDs
defined in `include/resource.h` and `include/resrc1.h`.

```cpp
// Example:
LoadString(hInst, TX_ERROR_GROUND, szBuffer, sizeof(szBuffer));
// → loads the localised string for ERROR_GROUND in the active locale
```

---

## Missing Localisation Support on Cross-Platform Builds

On Linux, Web, and Android builds, the Win32 `LoadString()` is emulated
by the Free API compatibility layer. The string resources are compiled in
from the `.rc` file at build time.

MIDI music track names (displayed on the music selection screen) are also
string resources and are therefore localised.

---

## Adding a New Language

1. Create `sound/newlang/` with localised WAV files named `soundNNN.blp`
2. Add the language code to the `Language=` handler in `misc.cpp`
3. Update the `.rc` file with translated strings for `TX_*` IDs
4. Rebuild
