# Data Files (`data/` directory)

## Overview

All runtime gameplay data resides in the `data/` directory.
Files originating from the CD-ROM are read via `AddCDPath()`;
user save files are local.

---

## Complete File Listing

| File / Pattern | Location | Description |
|---------------|----------|-------------|
| `config.def` | Local | Runtime configuration — see [Configuration](../platform/config.md) |
| `world000.blp` … `world005.blp` | CD | Tutorial / school missions (6 levels, Episode 1) |
| `world100.blp` … `world137.blp` | CD | Main campaign, Episode 2 (normal, ~38 levels) |
| `world138.blp` … `world153.blp` | CD | Campaign Episode 3 (advanced, ~16 levels) |
| `world200.blp` … `world215.blp` | CD/local | Bonus / advanced missions (16 levels, Episode 4) |
| `user000.blp` … `user009.blp` | Local | Player save game slots (10 slots) |
| `demo000.blp` … `demo003.blp` | CD | Built-in demo recordings (4 demos) |
| `enigmes.blp` | CD | Special puzzle / enigma world |
| `info.blp` | CD | Game information / credits world |

---

## Mission Numbering Scheme

```
000–005  Tutorial (school)
100–137  Campaign Episode 2 (normal)
138–153  Campaign Episode 3 (advanced)
200–215  Bonus Episode 4
```

Some world numbers in the 138–153 range are skipped (cut content or reserved).

---

## File Access Paths

```cpp
// CD path: reads from CD-ROM directory (set by CD-Rom= in config.def)
void AddCDPath(char *filename);
// Used for world100–world199

// User path: reads/writes from local user data directory
void AddUserPath(char *filename);
// Used for user000–user009
```

---

## Save Slot UI

`CDecor::FileExist(rank, bUser, world, time, total)` is called for each of
the 10 save slots to determine whether a save exists and read its `world`
number and `time` for display in the load/save screens.

---

## Demo Files

Demo files (`demo000.blp`–`demo003.blp`) have a different structure than
world files — they begin with `DemoHeader` followed by an array of `DemoEvent`
records, not `DescFile`. See [Demo Recording & Playback](../engine/demo.md).
