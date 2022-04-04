from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board and not board[0]:
        return
    row, col = len(board), len(board[0])
    visited = set()

    def dfs(r, c):
        if (r, c) not in visited and 0 <= r < row and 0 <= c < col and board[r][c] == "O":
            visited.add((r, c))
            board[r][c] = '#'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        return

    for c in range(col):
        dfs(0, c)
        dfs(row - 1, c)

    for r in range(row):
        dfs(r, 0)
        dfs(r, col - 1)

    for r in range(row):
        for c in range(col):
            flag = True
            if board[r][c] == '#':
                board[r][c] = 'O'
                flag = False
            if board[r][c] == 'O' and flag:
                board[r][c] = 'X'
