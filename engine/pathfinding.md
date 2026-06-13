# Pathfinding (A*)

## Implementation

Pathfinding is implemented in `src/chemin.cpp` using `CPileTriee`
(a min-heap sorted priority queue from `src/fifo.cpp`).

Working area: `CDecor::m_cheminWork[MAXCELX * MAXCELY]` (200×200 bytes = 40 000 bytes).

---

## Search Process

### Step 1: Build terrain bitmap — `CheminFillTerrain(rank)`

Fills `m_cheminWork[]` with a passability bitmap for the given character:

- Uses `tableObstacleFloor[]` and `tableObstacleObject[]` from `obstacle.cpp`
- For Blupi on foot: water = obstacle, ice = passable (but slippery)
- For Blupi in boat: land = obstacle, water = passable
- For Blupi in jeep: different obstacle rules than on foot
- For enemies: each type has its own passability rules

Cells occupied by other characters are marked as temporarily blocked.

### Step 2: Find path — `CheminCherche(rank, action)`

Implements the A* algorithm:

```
1. Initialise open list (CPileTriee) with starting cell
2. Loop:
   a. Pop cell with lowest cost from open list (CPileTriee::get())
   b. If it is the target cell → success
   c. For each of 4 directions (E, S, O, N):
      i.  CheminTestDirection() — verify passability
      ii. Calculate g (cost from start) + h (heuristic = Manhattan distance)
      iii. Insert into open list (CPileTriee::put())
3. Path reconstruction: CheminARebours() walks back through stored parents
```

### Step 3: Direction test — `CheminTestDirection(rank, pos, dir, next, ampli, cout, action)`

For each movement direction, verifies:
- Whether the cell in `m_cheminWork[]` is passable
- Whether another character is blocking the cell (`IsBlupiHereEx()`)
- Whether an obstacle can be jumped over (`IsFreeJump()`)
- Whether the character can slide on ice (`IsFreeGlisse()`)
- Returns the action to use (walk, jump, slide)

### Step 4: Path reconstruction — `CheminARebours(rank)`

After finding the target cell, reconstructs the path back to the start
and stores it as a sequence of directions in the character's command queue.

---

## `CPileTriee` — Min-heap for Open List

Implementation in `src/fifo.cpp`, declaration in `include/fifo.h`.

```cpp
class CPileTriee {
public:
    void put(int pos, int cout);   // insert position with cost
    int  get();                    // pop element with lowest cost
    void remove(int pos);          // remove a specific element
    BOOL isEmpty();
    int  getCout(int pos);         // get cost for a position
};
```

Position is encoded as: `pos = y * MAXCELX + x`

---

## Visited Position Memory

Each character remembers the last `MAXUSED=50` visited cells
in `posUsed[]` and `rankUsed[]`. If pathfinding repeatedly leads
a character through the same cells, an alternative path is sought
via `SearchBestPass()`.

```cpp
void CDecor::FlushUsed(int rank);             // clear position memory
void CDecor::AddUsedPos(int rank, POINT pos); // add a visited cell
BOOL CDecor::IsUsedPos(int rank, POINT pos);  // test if cell was visited
```

---

## Pathfinding Support Functions

| Function | Description |
|----------|-------------|
| `IsFreeDirect(cel, direct, rank)` | Can the character move from `cel` in the given direction? |
| `IsFreeCelObstacle(cel)` | Is the cell passable (ignoring characters)? |
| `IsFreeCelFloor(cel, rank)` | Is the floor passable for this character type? |
| `IsFreeCelGo(cel, rank)` | Can the character enter the cell (including character presence)? |
| `IsFreeCelHili(cel, rank)` | Is the cell suitable for action highlighting? |
| `IsFreeCel(cel, rank)` | Full passability test |
| `IsFreeCelDepose(cel, rank)` | Can an object be put down in the cell? |
| `IsFreeCelEmbarque(cel, rank, action, limit)` | Can the character board a vehicle? |
| `IsFreeCelDebarque(cel, rank, action, limit)` | Can the character disembark from a vehicle? |
| `IsFreeJump(cel, direct, rank, action)` | Can the character jump over an obstacle? |
| `IsFreeGlisse(cel, direct, rank, action)` | Can the character slide on ice? |
| `DirectSearch(cel, goal)` | Find direct direction from `cel` to `goal` |
| `SearchBestBase(rank, action, newCel, direct)` | Find best base position for an action |
| `SearchBestPass(rank, action)` | Find alternative passable cell |
| `IsCheminFree(rank, dest, button)` | Is there any path to the destination at all? |
