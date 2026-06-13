# Cheat Codes

## Overview

Two cheat modes are available via `CDecor::BlupiCheat(cheat)`.
The cheat sequence is tracked by `CEvent::m_rankCheat` / `m_posCheat`.

---

## Cheat Modes

| Mode | Field | Effect |
|------|-------|--------|
| Invincible | `m_bInvincible = TRUE` | Blupi cannot die, be poisoned, or burn |
| Super | `m_bSuper = TRUE` | Unlimited energy, enhanced abilities |

---

## API

```cpp
void CDecor::BlupiCheat(int cheat);
// cheat=1 → toggle invincible mode
// cheat=2 → toggle super mode

BOOL CDecor::GetInvincible();
void CDecor::SetInvincible(BOOL bInvincible);

BOOL CDecor::GetSuper();
void CDecor::SetSuper(BOOL bSuper);
```

---

## Activation

The cheat codes are activated by a hidden keyboard sequence tracked in
`CEvent`. `m_rankCheat` counts how many correct keys have been pressed,
and `m_posCheat` is the current position in the cheat key sequence.
When the full sequence is entered, `BlupiCheat()` is called.

The exact key sequence is not documented in the source headers.
