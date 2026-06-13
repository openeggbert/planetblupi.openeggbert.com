# Vehicles

## Overview

Vehicles modify Blupi's movement, passability, and combat properties.
The `vehicule` field in the `Blupi` struct identifies the current vehicle.

| `vehicule` | Vehicle | Sprite actions |
|-----------|---------|----------------|
| 0 | On foot | `ACTION_STOP`, `ACTION_MARCHE`, etc. |
| 1 | Boat (bateau) | `ACTION_STOPb`, `ACTION_MARCHEb` |
| 2 | Jeep | `ACTION_STOPj`, `ACTION_MARCHEj`, `ACTION_SAUTE1` |
| 3 | Armour (armure) | `ACTION_STOPa`, `ACTION_MARCHEa`, `ACTION_ARMUREOPEN/CLOSE` |

---

## Boat (vehicule=1)

**Effect**: Allows Blupi to navigate water cells. On land, the boat is an
object on the map and cannot be driven.

**Terrain**: Only passable on water cells. Cannot enter land cells
(except for embarking/disembarking at the water's edge).

**Sounds**: `SOUND_BATEAU` (44) — boat movement

**Boarding**: `WM_ACTION_BATEAUAE/AS/AO/AN` (+100–103) — embark from each direction
**Disembarking**: `WM_ACTION_BATEAUDE/DS/DO/DN` (+96–99) — disembark to each direction
**Movement in boat**: `WM_ACTION_BATEAUE/S/O/N` (+92–95) — move in each direction

**Passability checks**:
- `IsFreeCelEmbarque(cel, rank, action, limit)` — can Blupi board here?
- `IsFreeCelDebarque(cel, rank, action, limit)` — can Blupi land here?
- `SearchOtherBateau(rank, initCel, distMax, foundCel, foundIcon)` — find a boat

**Notes**: A boat on the map appears as an object (`CHOBJECT`). When Blupi boards it,
the object is removed and `vehicule=1` is set. When Blupi disembarks, the object
is placed back and `vehicule=0` is restored.

---

## Jeep (vehicule=2)

**Effect**: Faster movement than on foot. Can cross terrain that is slower or
harder on foot.

**Boarding**: `WM_ACTION_MJEEP` (+104) — board a jeep from adjacent cell
**Disembarking**: `WM_ACTION_DJEEP` (+105) — exit the jeep

**Sounds**: `SOUND_JEEP` (45) — jeep engine

**Building a jeep**: `WM_ACTION_FABJEEP` (+110) — factory manufactures a jeep
(`GOAL_USINEBUILD` + `GOAL_USINEFREE`)

**Notes**: Like the boat, the jeep exists as a map object until boarded.
`ACTION_SAUTE1` (59) is the jump animation for leaping into the jeep.

---

## Armour (vehicule=3, Armure)

**Effect**: Makes Blupi nearly invulnerable to enemy attacks. Most enemy attacks
are blocked while Blupi is in armour. Energy is consumed faster.

**Boarding**: `WM_ACTION_MARMURE` (+129) — enter armour
**Disembarking**: `WM_ACTION_DARMURE` (+130) — exit armour
**Building armour**: `WM_ACTION_FABARMURE` (+128) — factory manufactures armour

**Sounds**: `SOUND_ARMUREOPEN` (81) — opening, `SOUND_ARMURECLOSE` (82) — closing

**Animation sequence**:
1. `ACTION_ARMUREOPEN` (57) — armour opens
2. Blupi enters, `vehicule=3` set
3. `ACTION_STOPa` (55) / `ACTION_MARCHEa` (56) — movement in armour
4. `ACTION_ARMURECLOSE` (58) — armour closes when exiting

**Notes**: The armour suit is manufactured in a factory. It appears as a map object
until Blupi boards it. While in armour, most `GOAL_*` operations work normally
but combat-related enemies are less effective.
