# Undo System

## Overview

The level editor (`WM_PHASE_BUILD`) supports a single-step undo:
at most one world state snapshot exists at any time, and can be restored once.

Implementation: `src/decor.cpp`, `CDecor::Undo*()` methods.

---

## API

```cpp
void CDecor::UndoOpen();
// Begins recording changes — prepares the snapshot slot.
// Called immediately before a destructive operation (place/delete tile, build etc.)

void CDecor::UndoCopy();
// Copies the current m_decor[100][100] state into m_pUndoDecor.
// Allocates heap memory if not yet allocated.

void CDecor::UndoClose();
// Finalises the snapshot — marks it as valid.

void CDecor::UndoBack();
// Restores the world state from the snapshot:
//   memcpy(m_decor, m_pUndoDecor, sizeof(m_decor))
// Invalidates the snapshot (undo cannot be used again).

BOOL CDecor::IsUndo();
// Returns TRUE if a valid snapshot exists.
// Used to enable/disable the Undo button in the editor.
```

---

## Implementation Details

- Snapshot stored in `m_pUndoDecor` — heap-allocated copy of `m_decor[100][100]`
- Only `Cellule` data is copied (floor + object tiles), **not** characters or animations
- Undo is only available in the editor (`m_bBuild = TRUE`), not during gameplay
- After `UndoBack()`, the snapshot is invalidated — no redo is possible
- Total snapshot size: `100 * 100 * sizeof(Cellule)` bytes

---

## Typical Call Sequence

```cpp
// Before a destructive operation in the editor:
pDecor->UndoOpen();
pDecor->UndoCopy();
// ... perform change ...
pDecor->UndoClose();

// On Ctrl+Z / Undo button:
if (pDecor->IsUndo()) {
    pDecor->UndoBack();
}
```
