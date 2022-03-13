from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    """You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.
    If this is impossible, return -1.
    """
    queue = deque()
    fresh_oranges = 0
    m, n = len(grid), len(grid[0])

    for row in range(m):
        for col in range(n):
            if grid[row][col] == 2:
                queue.append((row, col))
            elif grid[row][col] == 1:
                fresh_oranges += 1

    queue.append((-1, -1))
    minutes_elapsed = -1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        row, col = queue.popleft()
        if row == -1:
            minutes_elapsed += 1
            if queue:
                queue.append((-1, -1))
        else:
            for d in directions:
                neighbor_row, neighbor_col = row + d[0], col + d[1]
                if m > neighbor_row >= 0 and n > neighbor_col >= 0:
                    if grid[neighbor_row][neighbor_col] == 1:
                        grid[neighbor_row][neighbor_col] = 2
                        fresh_oranges -= 1
                        queue.append((neighbor_row, neighbor_col))
    return minutes_elapsed if fresh_oranges == 0 else -1


print(orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(orangesRotting(grid=[[0, 2]]))
print(orangesRotting(grid=[[1, 2]]))
