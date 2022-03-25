from typing import List


def numIslands(grid: List[List[str]]) -> int:
    islands: int = 0

    def dfs(row, col):
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()

            if grid[r][c] == "1":
                grid[r][c] = "-1"
                if r > 0:
                    stack.append((r - 1, c))
                if r + 1 < len(grid):
                    stack.append((r + 1, c))
                if c > 0:
                    stack.append((r, c - 1))
                if c + 1 < len(grid[0]):
                    stack.append((r, c + 1))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)
    return islands


print(numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
