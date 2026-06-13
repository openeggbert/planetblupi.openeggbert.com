# Image Assets

All images are stored in the `image/` directory as `.blp` files
(Epsitec's proprietary palette-based bitmap format).

---

## Gameplay Sprite Sheets

| File | Channel | Contents |
|------|---------|---------|
| `blupi.blp` | CHBLUPI (4) | All Blupi animation frames: stop, walk, build, jump, boat, jeep, armour, teleport, plus all enemy sprites (spider, virus, tracks, robot, bomb, electro, disciple) |
| `floor000.blp` | CHFLOOR (1) | Floor tiles — normal region (grass, earth, water, rock, ice, shore transitions) |
| `floor001.blp` | CHFLOOR (1) | Floor tiles — tropical region |
| `floor002.blp` | CHFLOOR (1) | Floor tiles — winter region (snow, ice) |
| `floor003.blp` | CHFLOOR (1) | Floor tiles — pine forest region |
| `obj000.blp` | CHOBJECT (2) | Objects layer — normal region: trees, rocks, buildings, items |
| `obj001.blp` | CHOBJECT (2) | Objects layer — tropical |
| `obj002.blp` | CHOBJECT (2) | Objects layer — winter |
| `obj003.blp` | CHOBJECT (2) | Objects layer — pine |
| `obj-o000.blp` | CHOBJECTo (3) | Objects overlay — normal (upper parts of tall objects) |
| `obj-o001.blp` | CHOBJECTo (3) | Objects overlay — tropical |
| `obj-o002.blp` | CHOBJECTo (3) | Objects overlay — winter |
| `obj-o003.blp` | CHOBJECTo (3) | Objects overlay — pine |
| `hili.blp` | CHHILI (5) | Highlight / selection overlay icons (hover, select, error, go, build, stat) |
| `fog.blp` | CHFOG (6) | 15 fog-of-war tile patterns |
| `mask1.blp` | CHMASK1 (7) | Alpha mask for Blupi sprite blending |
| `little.blp` | CHLITTLE (8) | Small pixel font (10 px characters) |
| `button.blp` | CHBUTTON (10) | Toolbar action-button icons (all 35 BUTTON_* types) |
| `button00.blp` | CHBUTTON (10) | Button 0 (Go) variant |
| `jauge.blp` | CHJAUGE (12) | Energy / progress gauge sprites |
| `text.blp` | CHTEXT (13) | Main text font (16×16 px), white, red and slim variants |
| `bignum.blp` | CHBIGNUM (14) | Large digit sprites for score / timer display |

---

## Screen Background Images

These are loaded into `CHBACK (0)` when the corresponding phase is active.

| File | Phase |
|------|-------|
| `play.blp` | `WM_PHASE_PLAY` — main HUD frame |
| `build.blp` | `WM_PHASE_BUILD` — level editor |
| `read.blp` | `WM_PHASE_READ` — load game |
| `write.blp` | `WM_PHASE_WRITE` — save game |
| `win.blp` | `WM_PHASE_WIN` |
| `lost.blp` | `WM_PHASE_LOST` |
| `stop000.blp` | `WM_PHASE_STOP` (variant 0) |
| `stop001.blp` | `WM_PHASE_STOP` (variant 1) |
| `stop002.blp` | `WM_PHASE_STOP` (variant 2) |
| `setup.blp` | `WM_PHASE_SETUP` |
| `music.blp` | `WM_PHASE_MUSIC` |
| `region.blp` | `WM_PHASE_REGION` |
| `term.blp` | `WM_PHASE_TERM` |
| `help.blp` | `WM_PHASE_HELP` |
| `bye.blp` | `WM_PHASE_BYE` |
| `init.blp` | Startup / loading screen |
| `insert.blp` | `WM_PHASE_INSERT` — CD-ROM prompt |
| `intro1.blp` | `WM_PHASE_INTRO1` |
| `intro2.blp` | `WM_PHASE_INTRO2` |
| `history0.blp` | `WM_PHASE_HISTORY0` |
| `history1.blp` | `WM_PHASE_HISTORY1` |
| `last000.blp` | `WM_PHASE_LASTWIN` (frame 0) |
| `last001.blp` | `WM_PHASE_LASTWIN` (frame 1) |
| `last002.blp` | `WM_PHASE_LASTWIN` (frame 2) |
| `movie.blp` | Fallback image for any movie phase when AVI is unavailable |

---

## Mission Info Images

| File | Description |
|------|-------------|
| `info000.blp` | Mission info / briefing panel style 0 |
| `info001.blp` | Mission info / briefing panel style 1 |
| `info002.blp` | Mission info / briefing panel style 2 |

---

## Channel Loading

```cpp
// CPixmap loads images via:
pPixmap->Cache(CHBLUPI, "image/blupi.blp");
pPixmap->Cache(CHFLOOR, "image/floor000.blp");  // changes per region
pPixmap->Cache(CHOBJECT, "image/obj000.blp");    // changes per region

// Drawing an icon from a channel:
pPixmap->DrawIcon(hdc, channel, icon, x, y);
```
