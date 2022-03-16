from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    n = 9
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range(n)]

    for r in range(n):
        for c in range(n):
            current = board[r][c]

            if current == ".":
                continue
            if current in rows[r]:
                return False
            rows[r].add(current)
            if current in cols[c]:
                return False
            cols[c].add(current)

            index = (r // 3) * 3 + c // 3
            if current in boxes[index]:
                return False
            boxes[index].add(current)
    return True


print(isValidSudoku(board=
                    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(isValidSudoku(board=
                    [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
