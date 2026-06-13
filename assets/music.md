# Music Tracks

## Overview

MIDI music files are stored in `sound/music000.blp` … `sound/music009.blp` (10 tracks).
They are played via the Windows MCI MIDI subsystem (`CSound::PlayMusic()`).

Track selection is per-mission, stored in `DescFile.music` (0–9).

> **Note**: MIDI playback does not work in the Web (Emscripten) build.

---

## Music Track Table

| Index | File | Context (typical use) |
|-------|------|----------------------|
| 0 | `sound/music000.blp` | Main menu / neutral |
| 1 | `sound/music001.blp` | Gameplay track 1 |
| 2 | `sound/music002.blp` | Gameplay track 2 |
| 3 | `sound/music003.blp` | Gameplay track 3 |
| 4 | `sound/music004.blp` | Gameplay track 4 |
| 5 | `sound/music005.blp` | Gameplay track 5 |
| 6 | `sound/music006.blp` | Gameplay track 6 |
| 7 | `sound/music007.blp` | Gameplay track 7 |
| 8 | `sound/music008.blp` | Gameplay track 8 |
| 9 | `sound/music009.blp` | Gameplay track 9 |

---

## Playback

```cpp
void CSound::PlayMusic(int music);
// Plays music track music (0–9)
// Stops any currently playing track first

void CSound::StopMusic();
// Stops currently playing music

void CDecor::SetMusic(int music);  // set m_music
int  CDecor::GetMusic();           // get m_music
```

The music selection screen (`WM_PHASE_MUSIC`, background: `image/music.blp`)
lets the player choose which track plays during the mission.

---

## Format

The `.blp` files in `sound/` that contain music are MIDI sequences wrapped in
the Epsitec container format, not PCM audio. They are extracted and passed to
the Windows MCI API (`mciSendCommand`) for playback.
