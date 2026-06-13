# Player Character (Blupi)

## Identity

`perso=0` — the main playable character.
A yellow humanoid creature. Up to `MAXBLUPI=100` Blupi can exist simultaneously
(shared with all enemy slots), but only a subset are player-controlled.

---

## Birth

New Blupi are hatched from eggs. The incubator building produces eggs.
Blupi hatches via `ACTION_NAISSANCE` (14), with sound `SOUND_NAISSANCE` (20).
`WM_ACTION_NEWBLUPI` triggers the hatching sequence via `GOAL_NEWBLUPI`.

---

## Energy

- Starting energy: `MAXENERGY = 4000`
- Drains each tick (rate depends on `m_skill` difficulty level)
- Replenished by eating food (`ACTION_MANGE`) or drinking potions (`ACTION_BOIT`)
- Sources: tomatoes (food from cultivated plots), potions (from laboratory)
- At ~25% energy (`MAXENERGY/4 = 1000`): transitions to tired animations
  (`ACTION_STOPf`, `ACTION_MARCHEf`, `ACTION_MISC1f`)
- At 0% energy: Blupi dies (plays `ACTION_TCHAO`)

---

## Movement

Blupi moves cell by cell. The GOAL interpreter calls `GoalStart()` with
a movement goal, which triggers pathfinding (`CheminCherche()`) and then
walks the path one cell per tick using `ACTION_MARCHE`.

Blupi automatically jumps over small obstacles with `ACTION_SAUTE1`–`ACTION_SAUTE5`.
On ice cells, Blupi slides with `ACTION_GLISSE`.

---

## Idle Animations

When Blupi stands idle, the engine occasionally plays one of the idle animations:

| Action | Code | Description |
|--------|------|-------------|
| `ACTION_MISC1` | 20 | Shrugging |
| `ACTION_MISC2` | 21 | Scratching |
| `ACTION_MISC3` | 22 | Yo-yo trick |
| `ACTION_MISC4` | 40 | Closing eyes |
| `ACTION_MISC5` | 51 | Waving / calling |
| `ACTION_MISC6` | 60 | Diabolo trick |
| `ACTION_MISC1f` | 23 | Tired: bof-bof (if energy < 25%) |

---

## Voice Sounds

Blupi reacts to commands with voice lines. Six variants per call type
allow for varied responses:

| Event | Sound constants |
|-------|----------------|
| Acknowledges command | `SOUND_OK1`–`SOUND_OK6` (2–4, 59–61) |
| Starts moving | `SOUND_GO1`–`SOUND_GO6` (5–7, 68–70) |
| Finishes task | `SOUND_TERM1`–`SOUND_TERM6` (8–10, 71–73) |
| Hurt | `SOUND_AIE` (37) |
| Burning | `SOUND_BRULE` (17) |
| Jumping | `SOUND_SAUT` (13) |
| Eating | `SOUND_MANGE` (19) |
| Drinking | `SOUND_BOIT` (29) |
| Born | `SOUND_NAISSANCE` (20) |
| Disappearing | `SOUND_TCHAO` (18) |

Tired variants: `SOUND_OK1f`–`SOUND_OK3f` (62–64), enemy electro: `SOUND_OK1e`–`SOUND_OK3e` (65–67)

---

## Sick State (bMalade)

When poisoned by a spider, `bMalade=TRUE`:
- Energy drains faster
- `GOAL_ISNOMALADE` can be used in goal sequences to wait for recovery
- Recovery happens over time or via drinking a potion

---

## Cheat Mode

`CDecor::BlupiCheat(cheat)` activates cheat modes:
- `m_bInvincible=TRUE` → Blupi cannot die or be poisoned
- `m_bSuper=TRUE` → Blupi has unlimited energy and enhanced abilities

---

## Key Blupi Operations

```cpp
int  CDecor::BlupiCreate(POINT cel, int action, int direct, int perso, int energy);
BOOL CDecor::BlupiDelete(POINT cel, int perso=-1);
void CDecor::BlupiDelete(int rank);
void CDecor::BlupiKill(int exRank, POINT cel, int type);
void CDecor::BlupiActualise(int rank);   // refresh sprite
void CDecor::BlupiAdaptIcon(int rank);   // adapt icon for current state
void CDecor::BlupiPushFog(int rank);     // update fog of war
void CDecor::BlupiSound(int rank, int sound, POINT pos, BOOL bStop=FALSE);
void CDecor::BlupiInitAction(int rank, int action, int direct=-1);
void CDecor::BlupiChangeAction(int rank, int action, int direct=-1);
BOOL CDecor::BlupiNextAction(int rank);  // advance one animation frame
void CDecor::BlupiNextGoal(int rank);    // advance one GOAL step
BOOL CDecor::BlupiRotate(int rank);      // rotate to desired direction
void CDecor::BlupiStep(BOOL bFirst);     // tick all characters
BOOL CDecor::BlupiGoal(int rank, int button, POINT cel, POINT cMem);
void CDecor::BlupiGetRect(int rank, RECT &rect);
int  CDecor::GetTargetBlupi(POINT pos);  // find Blupi at screen position
```
