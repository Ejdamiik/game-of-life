
# │ State │Living neighbours│  Result  │
# ├───────┼─────────────────┼──────────┤
# │ alive │       0–1       │    dead  │
# │ alive │       2–3       │    alive │
# │ alive │       4–8       │    dead  │
# │┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│
# │ dead  │       0–2       │    dead  │
# │ dead  │        3        │    alive │
# │ dead  │       4-8       │    dead  │

def get_living_neighbours(i, j, data):

    living = 0
    if i == 0 and j == 0:   # Left upper corner
        if data[1][0] == 1:
            living += 1
        if data[0][1] == 1:
            living += 1
        if data[1][1] == 1:
            living += 1

    elif i == 0 and j == len(data[0]) - 1:  # Right upper corner
        if data[0][j - 1] == 1:
            living += 1
        if data[1][j - 1] == 1:
            living += 1
        if data[1][j] == 1:
            living += 1

    elif i == len(data) - 1 and j == 0: # Left lower corner
        if data[i][1] == 1:
            living += 1
        if data[i - 1][0] == 1:
            living += 1
        if data[i - 1][1] == 1:
            living += 1

    elif i == len(data) - 1 and j == len(data[0]) - 1:  # right lower corner
        if data[i][j - 1] == 1:
            living += 1
        if data[i - 1][j - 1] == 1:
            living += 1
        if data[i - 1][j] == 1:
            living += 1

    elif i == 0:    # upper row
        if data[0][j + 1] == 1:
            living += 1
        if data[0][j - 1] == 1:
            living += 1
        if data[1][j] == 1:
            living += 1
        if data[1][j + 1] == 1:
            living += 1
        if data[1][j - 1] == 1:
            living += 1

    elif i == len(data) - 1:    # lower row
        if data[i][j + 1] == 1:
            living += 1
        if data[i][j - 1] == 1:
            living += 1
        if data[i - 1][j] == 1:
            living += 1
        if data[i - 1][j + 1] == 1:
            living += 1
        if data[i - 1][j - 1] == 1:
            living += 1

    elif j == 0:    # left column
        if data[i - 1][0] == 1:
            living += 1
        if data[i + 1][0] == 1:
            living += 1
        if data[i][1] == 1:
            living += 1
        if data[i - 1][1] == 1:
            living += 1
        if data[i + 1][1] == 1:
            living += 1


    elif j == len(data[0]) - 1: # right column
        if data[i + 1][j]:
            living += 1
        if data[i - 1][j]:
            living += 1
        if data[i][j - 1]:
            living += 1
        if data[i + 1][j -1]:
            living += 1
        if data[i - 1][j - 1]:
            living += 1

    else:   # not on edge xd
        if data[i][j + 1] == 1:
            living += 1
        if data [i][j - 1] == 1:
            living += 1
        if data [i + 1][j] == 1:
            living += 1
        if data[i - 1][j] == 1:
            living += 1
        if data[i - 1][j - 1] == 1:
            living += 1
        if data[i - 1][j + 1] == 1:
            living += 1
        if data[i + 1][j - 1] == 1:
            living += 1
        if data[i + 1][j + 1] == 1:
            living += 1

    return living

def eval_life(data):
    """
    Evaluating based on rules
    """
    
    res = [[0 for i in range(len(data[0]))] for j in range(len(data))]

    for i in range(len(data)):

        for j in range(len(data[0])):

            living = get_living_neighbours(i, j, data)
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


def life(initial, generations):
    """
    Simulates n- generations of initial setup
    """
    
    for i in range(generations):
        initial = eval_life(initial)

    return initial



def main():
    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 1) \
        == [[1, 0, 1], [1, 0, 0], [1, 0, 1]]
    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 2) \
        == [[0, 1, 0], [1, 0, 0], [0, 1, 0]]
    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 3) \
        == [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 4) \
        == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 5) \
        == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert life([[0, 1, 1],
                 [1, 1, 1],
                 [0, 1, 1]], 0) \
        == [[0, 1, 1], [1, 1, 1], [0, 1, 1]]

    assert life([[1, 1],
                 [1, 1]], 3) \
        == [[1, 1], [1, 1]]
    assert life([[1, 1],
                 [0, 1]], 1) \
        == [[1, 1], [1, 1]]

    assert life([[1, 0, 1, 0],
                 [0, 1, 0, 1],
                 [1, 0, 0, 1],
                 [0, 0, 1, 1]], 5) \
        == [[0, 0, 1, 0],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 0]]


if __name__ == "__main__":
    main()