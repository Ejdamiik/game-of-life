import random

def get_random_matrix(x = 6, y = 6):

    res = []
    options = [0, 1]

    for i in range(x):

        row = []
        for j in range(y):
            row.append(random.choice(options))

        res.append(row)

    return res


def cool_start(x, y):

	res = [[0 for i in range(y)] for j in range(x)]
	mid_x = x // 2
	mid_y = y // 2
	res[mid_x][mid_y] = 1
	res[mid_x][mid_y + 1] = 1
	res[mid_x][mid_y + 2] = 1
	res[mid_x][mid_y + 3] = 1
	res[mid_x][mid_y + 4] = 1
	res[mid_x][mid_y + 5] = 1
	res[mid_x][mid_y + 6] = 1
	res[mid_x][mid_y + 7] = 1
	res[mid_x][mid_y + 8] = 1

	return res