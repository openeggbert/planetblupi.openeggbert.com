# Speedy Blupi — Relationship to Planet Blupi

## Context

**Speedy Blupi** is a side-scrolling platformer by Epsitec SA (~1995).
Planet Blupi (1997) was developed by the same team and shares:
- The Blupi character universe
- Some header files (most notably `actions.h`)
- The Epsitec house style and tools

This repository (Planet Blupi open-source) contains `include/actions.h`,
which is a **direct source-level import from Speedy Blupi's engine**.
It is not used by Planet Blupi's own code — it exists for reference.

---

## What actions.h Contains

`include/actions.h` defines three enums and four opcode constants
from the Speedy Blupi animation bytecode engine:

### Bytecode Opcodes

```c
#define OPTERM    0   // end of animation sequence
#define OPLIST    1   // OPLIST i, D(i)..D(i-1) — list of frames
#define OPREPEAT  2   // OPREPEAT, n, i, D(i)..D(i-1) — repeated frames
#define OPSOUND   3   // OPSOUND s — play sound index s
```

These opcodes form the bytecode language for Speedy Blupi's animation interpreter.
Each animated character has a sequence of these opcodes describing its sprite frames.

### `Action` Enum — Character Animations

195+ action codes covering all directional movement and behaviour states.
Each action has 4 directional variants `_E` (east), `_N` (north), `_O` (west/ouest), `_S` (south).

See [actions.h Full Reference](actions-h.md) for the complete annotated listing.

### `Objet` Enum — Decoration Animations

18 states for animated decorations (detonators, bombs, signs, traps, etc.):
`OB_DETONATEURA/B/C`, `OB_BOMBEA/B/C`, `OB_SENSUNIO/E/N/S`, `OB_VITRENS/EO`,
`OB_BALLONEX`, `OB_BAISSE`, `OB_TELE`, `OB_UNSEUL`, `OB_DEPART`, `OB_TROPBU`

### `Sound` Enum — Speedy Blupi SFX

39 sound effect identifiers (1–39) plus 16 music indices (101–116).

> **Important**: These conflict with Planet Blupi's `SOUND_*` macros in `def.h`.
> The two systems must not be mixed.

### Helper Functions

```cpp
short* ConvActionToTabIcon(Action action, short typemarche);
// Returns pointer to sprite frame table for given action and walk type

short* ConvActionToTabMove(Action action);
// Returns pointer to movement table for given action

short* ConvObjetToTabIcon(Objet objet);
// Returns pointer to sprite frame table for given decoration state
```

---

## Key Differences from Planet Blupi Engine

| Aspect | Speedy Blupi | Planet Blupi |
|--------|-------------|--------------|
| Animation system | Bytecode interpreter (OPTERM/OPLIST/OPREPEAT/OPSOUND) | Frame tables in action.cpp |
| Character states | `Action` enum (180+ states with 4 directions each) | `ACTION_*` macros (60+ states) |
| Direction system | 4 directions (`_E/_N/_O/_S`) | 8 directions (`DIRECT_*` × 16) |
| Object animations | `Objet` enum (18 states) | `Move` struct system |
| Movement model | Velocity / physics-based | Cell-by-cell grid |
| Goal system | State machine automaton | GOAL_* opcode interpreter |

---

## Using This for Decompilation

When reverse-engineering Speedy Blupi:

1. **Start with `actions.h`** — the `Action` enum maps directly to animation state IDs
2. The bytecode sequence `OPTERM/OPLIST/OPREPEAT/OPSOUND` appears in binary data tables
3. Each `Action` value is an index into sprite frame and movement tables
4. `ConvActionToTabIcon()` and `ConvActionToTabMove()` resolve an action to its tables
5. The `Sound` enum gives SFX indices (1–39) — note these are **different** from Planet Blupi's SOUND_* values
6. Music indices are 101–116 (SOUND_MUSIC11 through SOUND_MUSIC44)
7. The `Objet` enum covers animated scenery/decoration objects (non-character)

The animation table lookup functions (`ConvActionToTabIcon` etc.) are the core
of the Speedy Blupi sprite rendering pipeline and will be present in the binary.
