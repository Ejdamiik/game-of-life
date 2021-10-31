from typing import List

# │ State │Living neighbours│  Result  │
# ├───────┼─────────────────┼──────────┤
# │ alive │       0–1       │    dead  │
# │ alive │       2–3       │    alive │
# │ alive │       4–8       │    dead  │
# │┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│
# │ dead  │       0–2       │    dead  │
# │ dead  │        3        │    alive │
# │ dead  │       4-8       │    dead  │

Grid = List[List[int]]


def cell_value(grid: Grid, x: int, y: int) -> int:
    """
    Function to return value of cell with coords x y in grid
    if cell is out-of-bounds it returns 0
    """
    if 0 <= x < len(grid) and 0 <= y < len(grid):
        return grid[x][y]
    return 0


def live_neighbour_count(grid: Grid, x: int, y: int) -> int:
    assert x < len(grid) and y < len(grid)

    res = 0
    for row in range(x - 1, x + 2):
        for col in range(y - 1, y + 2):
            res += cell_value(grid, row, col)
    return res - grid[x][y]


def eval_life(data: Grid) -> Grid:
    """
    Evaluating based on rules
    """

    res = [[0 for i in range(len(data[0]))] for j in range(len(data))]

    for i in range(len(data)):

        for j in range(len(data[0])):

            living = live_neighbour_count(data, i, j)
            if data[i][j] == 1: # Living cell
                if living <= 1:
                    res[i][j] = 0

                elif 2 <= living <= 3:
                    res[i][j] = 1

                else:
                    res[i][j] = 0

            else:   # Dead cell

                if living == 3:
                    res[i][j] = 1
                else:
                    res[i][j] = 0

    return res


def life(initial: Grid, generations: int) -> Grid:
    """
    Simulates n- generations of initial setup
    """

    for i in range(generations):
        initial = eval_life(initial)

    return initial
