import math
from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    for row in range(1, len(triangle)):
        for col in range(row + 1):
            smallest_above = math.inf
            if col > 0:
                smallest_above = triangle[row - 1][col - 1]
            if col < row:
                smallest_above = min(smallest_above, triangle[row - 1][col])
            triangle[row][col] += smallest_above
    return min(triangle[-1])


print(minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
