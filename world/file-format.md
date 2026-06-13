# World File Format (.blp)

## Overview

World files use the `.blp` extension (Blupi binary format).
A single file stores the complete state of one mission: all tile positions,
characters, animated decorations, and win conditions.

Read/write: `CDecor::Read()` and `CDecor::Write()` in `src/decio.cpp`.

---

## File Naming

| Pattern | Location | Description |
|---------|----------|-------------|
| `data/world000.blp` … `data/world005.blp` | CD/install | Tutorial / school missions (6 levels) |
| `data/world100.blp` … `data/world137.blp` | CD/install | Campaign episode 1 (normal) |
| `data/world138.blp` … `data/world153.blp` | CD/install | Campaign episode 2 (advanced) |
| `data/world200.blp` … `data/world215.blp` | CD/install | Bonus / advanced missions (16 levels) |
| `data/user000.blp` … `data/user009.blp` | Local | Save game slots (10 slots) |
| `data/demo000.blp` … `data/demo003.blp` | CD/install | Built-in demo recordings (4) |
| `data/enigmes.blp` | CD/install | Special puzzle / enigma world |
| `data/info.blp` | CD/install | Information / credits world |

Files `world100–world199` are read from the CD-ROM path (`AddCDPath()`).
Files `world200+` and `user*` are stored locally.

---

## Mission Numbering

| Range | Episode |
|-------|---------|
| 000–005 | Episode 1: Tutorial / school (6 levels) |
| 100–137 | Episode 2: Normal campaign (~38 levels) |
| 138–153 | Episode 3: Advanced campaign (~16 levels, some numbers skipped) |
| 200–215 | Episode 4: Bonus missions (16 levels) |

Skipped world numbers (e.g. 138 is absent in some builds) indicate cut content.

---

## Binary File Layout

```
[ DescFile header ]    — fixed size
[ Cellule[] data  ]    — lgDecor bytes
[ Blupi[] data    ]    — lgBlupi bytes
[ Move[] data     ]    — lgMove bytes
```

### DescFile Header (detailed)

```cpp
typedef struct {
    short   majRev;              // major format version (e.g. 1)
    short   minRev;              // minor format version (e.g. 0)
    int32_t nbDecor;             // number of Cellule elements (= 100*100 = 10000)
    int32_t lgDecor;             // size of Cellule section in bytes
    int32_t nbBlupi;             // number of Blupi elements (= MAXBLUPI = 100)
    int32_t lgBlupi;             // size of Blupi section in bytes
    int32_t nbMove;              // number of Move elements (= MAXMOVE = 100)
    int32_t lgMove;              // size of Move section in bytes
    short   reserve1[100];       // 200 bytes reserved
    POINT   celCoin;             // scroll position (top-left visible cell)
    short   world;               // world / mission number
    int32_t time;                // game time (in ticks)
    char    buttonExist[40];     // MAXBUTTON=40: which toolbar buttons are available
    Term    term;                // win conditions (see data-structures.md)
    short   music;               // music track 0–9
    short   region;              // visual region 0–3
    int32_t totalTime;           // total time on mission (statistics)
    short   skill;               // difficulty 0–2
    POINT   memoPos[4];          // saved camera positions (F5–F8)
    short   reserve2[29];        // reserved
} DescFile;
```

---

## Write — `CDecor::Write()`

```cpp
BOOL CDecor::Write(int rank, BOOL bUser, int world, int time, int total)
{
    // Build file path:
    if (bUser)  sprintf(filename, "data/user%.3d.blp", rank);
    else        sprintf(filename, "data/world%.3d.blp", rank);

    // Open file for binary write
    // Write DescFile header
    // Write m_decor[100][100] (Cellule data)
    // Write m_blupi[100] (Blupi data) — active entries only
    // Write m_move[100] (Move data) — active entries only
    // Close file
}
```

---

## Read — `CDecor::Read()`

```cpp
BOOL CDecor::Read(int rank, BOOL bUser, int &world, int &time, int &total)
{
    // Build file path (try user/ first, then CD)
    // Read DescFile header
    // Verify nbDecor, nbBlupi, nbMove
    // Read Cellule data → m_decor[][]
    // Read Blupi data → m_blupi[] (convert OldBlupi if needed)
    // Read Move data → m_move[]
    // Apply m_region, m_music, m_skill, m_term etc.
}
```

---

## Backward Compatibility — `OldBlupi`

`src/decio.cpp` defines `OldBlupi` — the older Blupi structure without
`listButton/listCel/listParam/repeatLevel*` fields. When loading `.blp`
files created by an older version, `majRev/minRev` in `DescFile` triggers
automatic conversion from `OldBlupi` to the current `Blupi` layout.

---

## File Existence Check

```cpp
BOOL CDecor::FileExist(int rank, BOOL bUser, int &world, int &time, int &total)
// Opens file, reads only the header, closes — used for UI save slot listing
```
