# actions.h — Complete Reference

This file documents every symbol in `include/actions.h` for use in
reverse-engineering / decompiling Speedy Blupi.

---

## Bytecode Opcodes

```c
#define OPTERM    0   // end of animation sequence
#define OPLIST    1   // OPLIST i, D(i)..D(i-1)  — play frames i to i-1
#define OPREPEAT  2   // OPREPEAT, n, i, D(i)..D(i-1) — repeat n times
#define OPSOUND   3   // OPSOUND s — play sound index s
```

---

## `Action` Enum — All 195 Entries

Each action has 4 directional variants. Naming convention:
- `_E` = East
- `_N` = North
- `_O` = West (Ouest in French)
- `_S` = South

Special entries at the end have no direction variants.

```c
typedef enum {
    // Standing still
    AC_STOP_E,         // 0  — stopped, facing east
    AC_STOP_N,         // 1  — stopped, facing north
    AC_STOP_O,         // 2  — stopped, facing west
    AC_STOP_S,         // 3  — stopped, facing south

    // Walking forward
    AC_MARCHE_E,       // 4  — walking east
    AC_MARCHE_N,       // 5  — walking north
    AC_MARCHE_O,       // 6  — walking west
    AC_MARCHE_S,       // 7  — walking south

    // Walking backward
    AC_RECULE_E,       // 8  — backing up (east)
    AC_RECULE_N,       // 9
    AC_RECULE_O,       // 10
    AC_RECULE_S,       // 11

    // Turning (corner transitions)
    AC_TOURNE_NE,      // 12 — turning from north to east
    AC_TOURNE_ON,      // 13 — turning from west to north
    AC_TOURNE_SO,      // 14 — turning from south to west
    AC_TOURNE_ES,      // 15 — turning from east to south
    AC_TOURNE_SE,      // 16 — turning from south to east
    AC_TOURNE_EN,      // 17 — turning from east to north
    AC_TOURNE_NO,      // 18 — turning from north to west
    AC_TOURNE_OS,      // 19 — turning from west to south

    // Jump over obstacle (phase 1)
    AC_SAUTE1_E,       // 20
    AC_SAUTE1_N,       // 21
    AC_SAUTE1_O,       // 22
    AC_SAUTE1_S,       // 23

    // Jump over obstacle (phase 2)
    AC_SAUTE2_E,       // 24
    AC_SAUTE2_N,       // 25
    AC_SAUTE2_O,       // 26
    AC_SAUTE2_S,       // 27

    // Jump onto detonator
    AC_SAUTEDET_E,     // 28
    AC_SAUTEDET_N,     // 29
    AC_SAUTEDET_O,     // 30
    AC_SAUTEDET_S,     // 31

    // Falling into hole
    AC_TOMBE_E,        // 32
    AC_TOMBE_N,        // 33
    AC_TOMBE_O,        // 34
    AC_TOMBE_S,        // 35

    // Tank falling into hole
    AC_TOMBE_TANK_E,   // 36
    AC_TOMBE_TANK_N,   // 37
    AC_TOMBE_TANK_O,   // 38
    AC_TOMBE_TANK_S,   // 39

    // Tank falling into hole (variant B)
    AC_TOMBE_TANKB_E,  // 40
    AC_TOMBE_TANKB_N,  // 41
    AC_TOMBE_TANKB_O,  // 42
    AC_TOMBE_TANKB_S,  // 43

    // Drinking (good potion)
    AC_BOIT_E,         // 44
    AC_BOIT_N,         // 45
    AC_BOIT_O,         // 46
    AC_BOIT_S,         // 47

    // Drinking (bad potion — boitx = bad drink)
    AC_BOITX_E,        // 48
    AC_BOITX_N,        // 49
    AC_BOITX_O,        // 50
    AC_BOITX_S,        // 51

    // Getting hit by pie/tourte
    AC_TOURTE_E,       // 52
    AC_TOURTE_N,       // 53
    AC_TOURTE_O,       // 54
    AC_TOURTE_S,       // 55

    // Resting
    AC_REPOS_E,        // 56
    AC_REPOS_N,        // 57
    AC_REPOS_O,        // 58
    AC_REPOS_S,        // 59

    // Sleeping
    AC_DORT_E,         // 60
    AC_DORT_N,         // 61
    AC_DORT_O,         // 62
    AC_DORT_S,         // 63

    // Celebrating / youpie
    AC_YOUPIE_E,       // 64
    AC_YOUPIE_N,       // 65
    AC_YOUPIE_O,       // 66
    AC_YOUPIE_S,       // 67

    // Saying no
    AC_NON_E,          // 68
    AC_NON_N,          // 69
    AC_NON_O,          // 70
    AC_NON_S,          // 71

    // Pushing object
    AC_POUSSE_E,       // 72
    AC_POUSSE_N,       // 73
    AC_POUSSE_O,       // 74
    AC_POUSSE_S,       // 75

    // Cannot push (blocked)
    AC_NPOUSSE_E,      // 76
    AC_NPOUSSE_N,      // 77
    AC_NPOUSSE_O,      // 78
    AC_NPOUSSE_S,      // 79

    // Pushing a crate (wooden)
    AC_CAISSE_E,       // 80
    AC_CAISSE_N,       // 81
    AC_CAISSE_O,       // 82
    AC_CAISSE_S,       // 83

    // Pushing a crate (glass)
    AC_CAISSEV_E,      // 84
    AC_CAISSEV_N,      // 85
    AC_CAISSEV_O,      // 86
    AC_CAISSEV_S,      // 87

    // Pushing a crate (explosive)
    AC_CAISSEO_E,      // 88
    AC_CAISSEO_N,      // 89
    AC_CAISSEO_O,      // 90
    AC_CAISSEO_S,      // 91

    // Pushing an explosive crate (declining / decelerated)
    AC_CAISSEOD_E,     // 92
    AC_CAISSEOD_N,     // 93
    AC_CAISSEOD_O,     // 94
    AC_CAISSEOD_S,     // 95

    // Pushing a magnetic crate
    AC_CAISSEG_E,      // 96
    AC_CAISSEG_N,      // 97
    AC_CAISSEG_O,      // 98
    AC_CAISSEG_S,      // 99

    // Crates falling into hole
    AC_CAISSE_T,       // 100
    AC_CAISSEV_T,      // 101
    AC_CAISSEO_T,      // 102
    AC_CAISSEG_T,      // 103

    // Vision / looking (camera effect)
    AC_VISION_E,       // 104
    AC_VISION_N,       // 105
    AC_VISION_O,       // 106
    AC_VISION_S,       // 107

    // Departure (teleporter exit)
    AC_DEPART_E,       // 108

    // Balloon travel
    AC_BALLON_E,       // 109

    // Arrival animations
    AC_ARRIVEE_E,      // 110
    AC_ARRIVEE_N,      // 111
    AC_ARRIVEE_O,      // 112
    AC_ARRIVEE_S,      // 113

    // Arrival with balloon
    AC_ARRIVEE_M,      // 114

    // Balloon ascending
    AC_BALLON_M,       // 115

    // Playing piano
    AC_PIANO_O,        // 116

    // Magic spell (becoming transparent)
    AC_MAGIC_E,        // 117
    AC_MAGIC_N,        // 118
    AC_MAGIC_O,        // 119
    AC_MAGIC_S,        // 120

    // Electrocution
    AC_ELECTRO_O,      // 121

    // Watching TV / television
    AC_TELE_N,         // 122

    // Villain / mean character
    AC_MECHANT_E,      // 123
    AC_MECHANT_N,      // 124
    AC_MECHANT_O,      // 125
    AC_MECHANT_S,      // 126

    // Sliding on banana peel
    AC_GLISSE_E,       // 127
    AC_GLISSE_N,       // 128
    AC_GLISSE_O,       // 129
    AC_GLISSE_S,       // 130

    // Carrying a book
    AC_LIVRE_E,        // 131
    AC_LIVRE_N,        // 132
    AC_LIVRE_O,        // 133
    AC_LIVRE_S,        // 134

    // Playing music / musical instrument
    AC_MUSIQUE_E,      // 135
    AC_MUSIQUE_N,      // 136
    AC_MUSIQUE_O,      // 137
    AC_MUSIQUE_S,      // 138

    // Carrying a key
    AC_CLE_E,          // 139
    AC_CLE_N,          // 140
    AC_CLE_O,          // 141
    AC_CLE_S,          // 142

    // Opening a door
    AC_PORTE_E,        // 143
    AC_PORTE_N,        // 144
    AC_PORTE_O,        // 145
    AC_PORTE_S,        // 146

    // Crouching / lowering
    AC_BAISSE_O,       // 147

    // Overeating explosion
    AC_EXPLOSE_E,      // 148
    AC_EXPLOSE_N,      // 149
    AC_EXPLOSE_O,      // 150
    AC_EXPLOSE_S,      // 151

    // Starting (launching/departure)
    AC_START_E,        // 152
    AC_START_N,        // 153
    AC_START_O,        // 154
    AC_START_S,        // 155

    // Thinking / reflection
    AC_REFLEXION_E,    // 156
    AC_REFLEXION_N,    // 157
    AC_REFLEXION_O,    // 158
    AC_REFLEXION_S,    // 159

    // Shrugging
    AC_HAUSSE_E,       // 160
    AC_HAUSSE_N,       // 161
    AC_HAUSSE_O,       // 162
    AC_HAUSSE_S,       // 163

    // Yo-yo trick
    AC_YOYO_E,         // 164
    AC_YOYO_N,         // 165
    AC_YOYO_O,         // 166
    AC_YOYO_S,         // 167

    // Hit by tank
    AC_TANK,           // 168
} Action;
```

---

## `Objet` Enum — All 18 Entries

Animated decoration state codes for non-character objects:

```c
typedef enum {
    OB_DETONATEURA,    // 0  — detonator lowering (phase A)
    OB_DETONATEURB,    // 1  — detonator (phase B)
    OB_DETONATEURC,    // 2  — detonator (phase C)
    OB_BOMBEA,         // 3  — bomb exploding (phase A)
    OB_BOMBEB,         // 4  — bomb (phase B)
    OB_BOMBEC,         // 5  — bomb (phase C)
    OB_SENSUNIO,       // 6  — one-way sign rising (west)
    OB_SENSUNIE,       // 7  — one-way sign (east)
    OB_SENSUNIN,       // 8  — one-way sign (north)
    OB_SENSUNIS,       // 9  — one-way sign (south)
    OB_VITRENS,        // 10 — glass pane shattering (NS)
    OB_VITREEO,        // 11 — glass pane shattering (EO)
    OB_BALLONEX,       // 12 — balloon exploding
    OB_BAISSE,         // 13 — electronic door lowering
    OB_TELE,           // 14 — TV in operation
    OB_UNSEUL,         // 15 — trapdoor opening (hand coming out)
    OB_DEPART,         // 16 — teleporter opening/closing
    OB_TROPBU,         // 17 — floor opening (overeating result)
} Objet;
```

---

## `Sound` Enum — All SFX (1–39) and Music (101–116)

> **Warning**: These values are completely separate from Planet Blupi's `SOUND_*` macros.
> They belong to the Speedy Blupi audio engine only.

```c
typedef enum {
    SOUND_SAUT1         = 1,   // Toto about to jump
    SOUND_SAUT2         = 2,   // Toto landing after jump
    SOUND_TROPBU        = 3,   // Toto drank too much
    SOUND_TOMBE         = 4,   // Toto falling into a hole
    SOUND_TROUVEBALLON  = 5,   // Toto found the balloon
    SOUND_TROUVECLE     = 6,   // Toto found a key
    SOUND_BOIT          = 7,   // Toto drinking from bottle
    SOUND_MAGIE         = 8,   // Toto about to turn transparent (magic)
    SOUND_ELECTRO       = 9,   // Toto getting electrocuted
    SOUND_ARRIVE        = 10,  // Toto arriving from underground on balloon
    SOUND_REPOS         = 11,  // Toto resting
    SOUND_DORT          = 12,  // Toto falling asleep
    SOUND_GLISSE        = 13,  // Toto sliding on banana peel
    SOUND_TOURTE        = 14,  // Toto hit by pie
    SOUND_LUNETTES      = 15,  // Toto putting on glasses
    SOUND_CREVE         = 16,  // villain pops a balloon
    SOUND_LIVRE         = 17,  // Toto reading a book
    SOUND_MALADE        = 18,  // Toto falling sick
    SOUND_POUSSE        = 19,  // Toto pushing a crate
    SOUND_SENSUNI       = 20,  // one-way sign rising
    SOUND_PORTEOUVRE    = 21,  // door opening
    SOUND_PORTEBAISSE   = 22,  // armoured door lowering
    SOUND_UNSEUL        = 23,  // hand coming out of trapdoor
    SOUND_VITRECASSE    = 24,  // glass pane shattering
    SOUND_BOMBE         = 25,  // bomb exploding
    SOUND_NON           = 26,  // Toto saying no
    SOUND_CLIC          = 27,  // button click
    SOUND_CAISSE        = 28,  // wooden crate falling
    SOUND_CAISSEV       = 29,  // glass/light structure falling
    SOUND_CAISSEO       = 30,  // ball/round object falling
    SOUND_ACTION        = 31,  // action in the scenery
    SOUND_MECHANT       = 32,  // Toto becoming a villain
    SOUND_PASSEMUR      = 33,  // Toto walking through wall
    SOUND_AIMANT        = 34,  // Toto landing on magnet
    SOUND_PORTEBAISSE2  = 35,  // armoured door open (variant)
    SOUND_MACHINE       = 36,  // electronic machine
    SOUND_OISEAUX       = 37,  // birds chirping
    SOUND_BURP          = 38,  // Toto burping (drank too much)
    SOUND_CAISSEG       = 39,  // magnetic/machine falling

    // Music tracks (indexed by episode-level):
    SOUND_MUSIC11       = 101, // music episode 1, level 1
    SOUND_MUSIC12       = 102, // music episode 1, level 2
    SOUND_MUSIC13       = 103, // music episode 1, level 3
    SOUND_MUSIC14       = 104, // music episode 1, level 4
    SOUND_MUSIC21       = 105, // music episode 2, level 1
    SOUND_MUSIC22       = 106, // music episode 2, level 2
    SOUND_MUSIC23       = 107, // music episode 2, level 3
    SOUND_MUSIC24       = 108, // music episode 2, level 4
    SOUND_MUSIC31       = 109, // music episode 3, level 1
    SOUND_MUSIC32       = 110, // music episode 3, level 2
    SOUND_MUSIC33       = 111, // music episode 3, level 3
    SOUND_MUSIC34       = 112, // music episode 3, level 4
    SOUND_MUSIC41       = 113, // music episode 4, level 1
    SOUND_MUSIC42       = 114, // music episode 4, level 2
    SOUND_MUSIC43       = 115, // music episode 4, level 3
    SOUND_MUSIC44       = 116, // music episode 4, level 4
} Sound;
```

---

## Helper Function Signatures

```cpp
// Returns sprite frame table for an action + walk type combination:
short* ConvActionToTabIcon(Action action, short typemarche);

// Returns movement delta table for an action:
short* ConvActionToTabMove(Action action);

// Returns sprite frame table for a decoration animation state:
short* ConvObjetToTabIcon(Objet objet);
```

These functions use the `Action` / `Objet` value as an index into
static lookup tables containing the animation frame sequences.

---

## Key Patterns for Binary Reverse Engineering

1. **OPTERM (0)** marks the end of every animation sequence — search for 0x00 terminators in data tables
2. **OPLIST (1)** followed by a count byte then frame indices — common pattern for short animations
3. **OPREPEAT (2)** followed by repeat count, then count byte then frame indices — for looping animations
4. **OPSOUND (3)** followed by a single-byte Sound enum value — finds all sound trigger points in animation data
5. The `Action` enum starts at 0 (AC_STOP_E) and goes to 168 (AC_TANK) — 169 total entries
6. The `Objet` enum has 18 entries (0–17)
7. Look for tables of short* pointers indexed by Action value × direction — the animation lookup tables
