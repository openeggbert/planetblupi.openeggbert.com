# History & Relation to Speedy Blupi

## Epsitec and the Blupi Universe

**Epsitec SA** (Switzerland) created a series of games featuring the character Blupi:

| Game | Genre | Year | Engine style |
|------|-------|------|-------------|
| Speedy Blupi | Side-scrolling platformer | ~1995 | Automaton state machine (`actions.h`) |
| Planet Blupi | Isometric RTS / puzzle | 1997 | Goal-based task interpreter (`decgoal.h`) |

Both games share the same character (yellow creature Blupi, called "Toto" in Speedy Blupi),
but use completely different game engines.

---

## Code-Level Relationship

The file `include/actions.h` in this repository is a **direct remnant of the Speedy Blupi engine**.
It defines:

- **Bytecode opcodes** for the animation interpreter (`OPTERM`, `OPLIST`, `OPREPEAT`, `OPSOUND`)
- The **`Action` enum** — all directional movement / behaviour codes for animated objects
  (characters, crates, balloons etc.), each action has 4 directional variants `_E/_N/_O/_S`
- The **`Objet` enum** — animated decoration state codes (detonator, bomb, one-way sign etc.)
- The **`Sound` enum** (Speedy Blupi variant) — SFX identifiers 1–39, music indices 101–116
- Helper functions: `ConvActionToTabIcon()`, `ConvActionToTabMove()`, `ConvObjetToTabIcon()`

> **These types are NOT used by Planet Blupi's own engine.** They belong to the Speedy Blupi
> animation subsystem that was imported / referenced during development.

Name-space conflict: the `Sound` enum values in `actions.h` **collide** with the `SOUND_*`
macros in `def.h`. They are two completely separate systems.

---

## Key Engine Differences

| Property | Speedy Blupi | Planet Blupi |
|----------|-------------|--------------|
| Movement model | Physics-based (jumps, falls, gravity) | Grid-based (cell by cell) |
| Character control | Bytecode automaton state machine | GOAL_* opcode interpreter |
| View | Side-scrolling 2D | Isometric 3D |
| Enemies | Simpler, fixed patterns | Autonomous AI with pathfinding |
| Vehicles | No | Yes (boat, jeep, armour) |
| Fog of war | No | Yes (quadrant bit system) |
| Save format | Simple | Binary `.blp` files with complete world state |

---

## Files Shared Between Games

| File | Origin | Use in Planet Blupi |
|------|--------|---------------------|
| `include/actions.h` | Speedy Blupi engine | Reference only; types not called by PB code |
| `include/decmove.h` | Carried over from Speedy Blupi | Fully used for animated decorations |
| General architecture | Epsitec in-house | Redesigned for isometric engine |

---

## Why Is actions.h in This Repository?

When **decompiling Speedy Blupi**, `actions.h` serves as the **primary starting point**
for understanding the character animation state machine. It contains the complete enumeration
of all actions (`Action` enum) and decorations (`Objet` enum) that the Speedy Blupi animation
system uses.

See [actions.h Reference](speedy-blupi/actions-h.md) for a full annotated listing.
