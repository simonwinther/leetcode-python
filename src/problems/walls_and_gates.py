from typing import List
from collections import deque


def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    if not rooms:
        return

    r, c = len(rooms), len(rooms[0])

    queue = []
    # start by adding all gates to queue
    for i in range(r):
        for j in range(c):
            if rooms[i][j] == 0:
                queue.append((i, j))

    for row, col in queue:
        dist = rooms[row][col] + 1
        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < r and 0 <= new_col < c and rooms[new_row][new_col] == 2147483647:
                rooms[new_row][new_col] = dist
                queue.append((new_row, new_col))
