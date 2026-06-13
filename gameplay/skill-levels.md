# Skill Levels

## Overview

Three skill levels adjust enemy difficulty, energy drain rate, and enemy speed.
Stored as `m_skill` in `CDecor`; set via `WM_PHASE_SKILL1` / `WM_PHASE_SKILL2`.

---

## Levels

| `m_skill` | Level | Description |
|-----------|-------|-------------|
| 0 | **Easy** | Slower enemies, less energy drain, more forgiving timing |
| 1 | **Normal** | Balanced difficulty |
| 2 | **Hard** | Faster enemies, faster energy drain, more aggressive AI |

---

## Effect on Gameplay

The skill level affects:
- Energy drain rate per tick
- Enemy movement speed
- Enemy search radius for targets
- Some GOAL_* sequences have skill-based branches via `GOAL_SKIPSKILL`

---

## `GOAL_SKIPSKILL` Opcode

```
GOAL_SKIPSKILL, skill, d
```
- `skill` = level to match (0, 1, or 2)
- `d` = number of opcodes to skip if current `m_skill` matches `skill`

This allows mission designers to create skill-specific behaviour in goal sequences.
For example, on Easy difficulty, an enemy might skip an aggressive attack step.

---

## API

```cpp
void CDecor::SetSkill(int skill);  // set skill level (0–2)
int  CDecor::GetSkill();           // get current skill level
```

The skill level is saved in `DescFile.skill` in the world file.

---

## Selection Screen

The player selects difficulty before starting a mission:

1. `WM_PHASE_SKILL1` — first selection screen (typically Easy/Normal options)
2. `WM_PHASE_SKILL2` — second screen (typically Hard option or confirmation)

These phases display the background image `image/stop000.blp` (or similar)
with the appropriate buttons.
