# Sound Effects (SOUND_*)

All sound constants are defined in `include/def.h`.
Each maps to `sound/soundNNN.blp` (zero-padded three-digit index).
Sound files are raw PCM WAV data stored in the `.blp` container.

---

## Sound Effect Reference

| Constant | Index | File | Description |
|----------|-------|------|-------------|
| `SOUND_CLICK` | 0 | `sound000.blp` | UI button click |
| `SOUND_BOING` | 1 | `sound001.blp` | Blupi bouncy acknowledgement (happy) |
| `SOUND_OK1` | 2 | `sound002.blp` | Blupi confirms command (voice 1) |
| `SOUND_OK2` | 3 | `sound003.blp` | Blupi confirms command (voice 2) |
| `SOUND_OK3` | 4 | `sound004.blp` | Blupi confirms command (voice 3) |
| `SOUND_GO1` | 5 | `sound005.blp` | Blupi starts moving (voice 1) |
| `SOUND_GO2` | 6 | `sound006.blp` | Blupi starts moving (voice 2) |
| `SOUND_GO3` | 7 | `sound007.blp` | Blupi starts moving (voice 3) |
| `SOUND_TERM1` | 8 | `sound008.blp` | Blupi finishes task (voice 1) |
| `SOUND_TERM2` | 9 | `sound009.blp` | Blupi finishes task (voice 2) |
| `SOUND_TERM3` | 10 | `sound010.blp` | Blupi finishes task (voice 3) |
| `SOUND_COUPTERRE` | 11 | `sound011.blp` | Digging earth |
| `SOUND_COUPTOC` | 12 | `sound012.blp` | Hitting wood / chopping |
| `SOUND_SAUT` | 13 | `sound013.blp` | Blupi jumping |
| `SOUND_HOP` | 14 | `sound014.blp` | Blupi hop (small jump over obstacle) |
| `SOUND_SCIE` | 15 | `sound015.blp` | Sawing wood |
| `SOUND_FEU` | 16 | `sound016.blp` | Fire burning |
| `SOUND_BRULE` | 17 | `sound017.blp` | Blupi burning / on fire |
| `SOUND_TCHAO` | 18 | `sound018.blp` | Blupi disappearing (death) |
| `SOUND_MANGE` | 19 | `sound019.blp` | Blupi eating |
| `SOUND_NAISSANCE` | 20 | `sound020.blp` | Birth of new Blupi (hatching from egg) |
| `SOUND_A_SAUT` | 21 | `sound021.blp` | Spider jumping |
| `SOUND_A_HIHI` | 22 | `sound022.blp` | Spider laugh / attack hiss |
| `SOUND_PLOUF` | 23 | `sound023.blp` | Splash (falling into water) |
| `SOUND_BUT` | 24 | `sound024.blp` | Goal / target reached |
| `SOUND_RAYON1` | 25 | `sound025.blp` | Electro ray beam start |
| `SOUND_RAYON2` | 26 | `sound026.blp` | Electro ray beam sustained |
| `SOUND_VIRUS` | 27 | `sound027.blp` | Virus spreading / infecting |
| `SOUND_GLISSE` | 28 | `sound028.blp` | Blupi sliding on ice |
| `SOUND_BOIT` | 29 | `sound029.blp` | Blupi drinking (potion) |
| `SOUND_LABO` | 30 | `sound030.blp` | Laboratory working |
| `SOUND_DYNAMITE` | 31 | `sound031.blp` | Dynamite explosion |
| `SOUND_PORTE` | 32 | `sound032.blp` | Door opening / closing |
| `SOUND_FLEUR` | 33 | `sound033.blp` | Picking flowers |
| `SOUND_T_MOTEUR` | 34 | `sound034.blp` | Tracks / tank engine |
| `SOUND_T_ECRASE` | 35 | `sound035.blp` | Tracks / tank crushing object |
| `SOUND_PIEGE` | 36 | `sound036.blp` | Trap triggered |
| `SOUND_AIE` | 37 | `sound037.blp` | Blupi hurt ("ouch!") |
| `SOUND_A_POISON` | 38 | `sound038.blp` | Spider poisoned / killed |
| `SOUND_R_MOTEUR` | 39 | `sound039.blp` | Robot motor running |
| `SOUND_R_APLAT` | 40 | `sound040.blp` | Robot flattening |
| `SOUND_R_ROTATE` | 41 | `sound041.blp` | Robot rotating |
| `SOUND_R_CHARGE` | 42 | `sound042.blp` | Robot recharging |
| `SOUND_B_SAUT` | 43 | `sound043.blp` | Bomb bouncing / hopping |
| `SOUND_BATEAU` | 44 | `sound044.blp` | Boat / water movement |
| `SOUND_JEEP` | 45 | `sound045.blp` | Jeep driving |
| `SOUND_MINE` | 46 | `sound046.blp` | Mine exploding |
| `SOUND_USINE` | 47 | `sound047.blp` | Factory operating |
| `SOUND_E_RAYON` | 48 | `sound048.blp` | Electro tower ray firing |
| `SOUND_E_TOURNE` | 49 | `sound049.blp` | Electro tower rotating |
| `SOUND_ARROSE` | 50 | `sound050.blp` | Blupi watering plants |
| `SOUND_BECHE` | 51 | `sound051.blp` | Blupi digging with spade |
| `SOUND_D_BOING` | 52 | `sound052.blp` | Disciple acknowledgement |
| `SOUND_D_OK` | 53 | `sound053.blp` | Disciple confirms command (voice) |
| `SOUND_D_GO` | 54 | `sound054.blp` | Disciple starts moving (voice) |
| `SOUND_D_TERM` | 55 | `sound055.blp` | Disciple finishes task (voice) |
| `SOUND_BOING1` | 56 | `sound056.blp` | Alternative boing 1 |
| `SOUND_BOING2` | 57 | `sound057.blp` | Alternative boing 2 |
| `SOUND_BOING3` | 58 | `sound058.blp` | Alternative boing 3 |
| `SOUND_OK4` | 59 | `sound059.blp` | OK voice 4 |
| `SOUND_OK5` | 60 | `sound060.blp` | OK voice 5 |
| `SOUND_OK6` | 61 | `sound061.blp` | OK voice 6 |
| `SOUND_OK1f` | 62 | `sound062.blp` | OK voice 1 (tired variant) |
| `SOUND_OK2f` | 63 | `sound063.blp` | OK voice 2 (tired variant) |
| `SOUND_OK3f` | 64 | `sound064.blp` | OK voice 3 (tired variant) |
| `SOUND_OK1e` | 65 | `sound065.blp` | OK voice 1 (enemy / electro variant) |
| `SOUND_OK2e` | 66 | `sound066.blp` | OK voice 2 (enemy variant) |
| `SOUND_OK3e` | 67 | `sound067.blp` | OK voice 3 (enemy variant) |
| `SOUND_GO4` | 68 | `sound068.blp` | Go voice 4 |
| `SOUND_GO5` | 69 | `sound069.blp` | Go voice 5 |
| `SOUND_GO6` | 70 | `sound070.blp` | Go voice 6 |
| `SOUND_TERM4` | 71 | `sound071.blp` | Term voice 4 |
| `SOUND_TERM5` | 72 | `sound072.blp` | Term voice 5 |
| `SOUND_TERM6` | 73 | `sound073.blp` | Term voice 6 |
| `SOUND_COUPSEC` | 74 | `sound074.blp` | Dry impact (stone on stone) |
| `SOUND_COUPPIERRE` | 75 | `sound075.blp` | Mining stone / rock |
| `SOUND_COUPSOURD` | 76 | `sound076.blp` | Muffled impact |
| `SOUND_COUPBREF` | 77 | `sound077.blp` | Brief impact |
| `SOUND_OPEN` | 78 | `sound078.blp` | Something opening |
| `SOUND_CLOSE` | 79 | `sound079.blp` | Something closing |
| `SOUND_TELEPORTE` | 80 | `sound080.blp` | Teleporter activating |
| `SOUND_ARMUREOPEN` | 81 | `sound081.blp` | Armour opening (entering) |
| `SOUND_ARMURECLOSE` | 82 | `sound082.blp` | Armour closing (exiting) |
| `SOUND_WIN` | 83 | `sound083.blp` | Mission victory fanfare |
| `SOUND_LOST` | 84 | `sound084.blp` | Mission defeat sound |
| `SOUND_MOVIE` | 99 | `sound099.blp` | Cinematic / AVI movie start sound |

---

## Localised Voice Sounds

Language-specific voice sounds override the base files.
Overriding sounds (indices 0–82 or 84 depending on language) are placed in:

| Directory | Language | Override count |
|-----------|---------|----------------|
| `sound/english/` | English | 83 files (000–082) |
| `sound/deutsch/` | German | 83 files (000–082) |
| `sound/francais/` | French | 83 files (000–082) |
| `sound/us/` | US English | 85 files (000–084) |

The active language is set by `Language=` in `data/config.def`.

---

## Sound Playback

```cpp
void CDecor::BlupiSound(int rank, int sound, POINT pos, BOOL bStop=FALSE)
// Plays a SOUND_* effect at the character's position
// bStop=TRUE: stop any currently playing sound for this character first

// CSound methods:
void CSound::Cache(int channel, const char* filename);  // load WAV
void CSound::Play(int sound, POINT pos, BOOL bStop);    // play
void CSound::PlayMusic(int music);                       // play MIDI
void CSound::StopMusic();                                // stop MIDI
```
