from typing import List
import math


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    memo = [[math.inf if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            if i > 0:
                memo[i][j] = min(memo[i][j], 1 + memo[i - 1][j])
            if j > 0:
                memo[i][j] = min(memo[i][j], 1 + memo[i][j - 1])

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i < m - 1:
                memo[i][j] = min(memo[i][j], 1 + memo[i + 1][j])
            if j < n - 1:
                memo[i][j] = min(memo[i][j], 1 + memo[i][j + 1])

    return memo


print(updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
