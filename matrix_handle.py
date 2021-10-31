import random

def get_random_matrix(x = 6, y = 6):
	"""
	Returns matrix with x rows y columns
	randomly valued with values in options
	"""

    res = []
    options = [0, 1]

    for i in range(x):

        row = []
        for j in range(y):
            row.append(random.choice(options))

        res.append(row)

    return res
