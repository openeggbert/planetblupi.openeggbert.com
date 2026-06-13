# Configuration File

## Location

`data/config.def` — plain-text key=value format, created and read by `src/misc.cpp`.

---

## All Configuration Keys

| Key | Example values | Description |
|-----|----------------|-------------|
| `CD-Rom` | `D:\`, `/media/cdrom/` | Path to the CD-ROM data directory. On modern installs this is the game's own `data/` directory. |
| `FullScreen` | `0`, `1` | `0` = windowed, `1` = full-screen |
| `MouseType` | `1`, `2`, `3` | Cursor rendering mode: `1`=GDI (software sprite), `2`=Windows cursor, `3`=Windows cursor with position tracking |
| `SpeedRate` | `1`, `2`, `3` | Game speed multiplier: `1`=normal, `2`=fast, `3`=very fast |
| `Timer` | `50` | Timer interval in milliseconds (one game tick). Default=50ms (20 ticks/sec) |
| `Language` | `F`, `E`, `D`, `U` | Active voice language: `F`=French, `E`=English, `D`=German, `U`=US English |

---

## Format

```
CD-Rom=D:\
FullScreen=0
MouseType=1
SpeedRate=1
Timer=50
Language=E
```

Lines starting with `#` are comments (if supported). Each key appears once.

---

## Language Codes

| Code | Language | Sound subdirectory |
|------|---------|-------------------|
| `F` | French (français) | `sound/francais/` |
| `E` | English | `sound/english/` |
| `D` | German (deutsch) | `sound/deutsch/` |
| `U` | US English | `sound/us/` |

The US English pack (`sound/us/`) has 85 sound files (000–084)
while other packs have 83 files (000–082).

---

## Access in Code

```cpp
// misc.cpp:
void AddCDPath(char *filename);
// Prepends the CD-Rom= path to filename

// Sound language selection:
// CSound reads the Language= key and loads from the appropriate subdirectory
```
