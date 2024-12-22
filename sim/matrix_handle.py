import random
from typing import List


def get_random_matrix(x: int, y: int) -> List[int]:
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
