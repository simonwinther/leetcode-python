from typing import List
from collections import deque


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def get_neighbors(row: int, col: int):
        for row_difference, col_difference in directions:
            new_row = row + row_difference
            new_col = col + col_difference
            if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                continue
            if grid[new_row][new_col] != 0:
                continue
            yield new_row, new_col

    if grid[0][0] != 0 or grid[max_row][max_col] != 0:
        return -1

    queue = deque()
    queue.append((0, 0))
    visited = {(0, 0)}
    current_distance = 1

    while queue:
        current_level = len(queue)
        for _ in range(current_level):
            row, col = queue.popleft()
            if (row, col) == (max_row, max_col):
                return current_distance
            for new_row, new_col in get_neighbors(row, col):
                if (new_row, new_col) in visited:
                    continue
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
        current_distance += 1
    return -1
