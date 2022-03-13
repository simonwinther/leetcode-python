from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    numRows = len(mat)
    numCols = len(mat[0])

    if numRows * numCols != r * c:
        return mat

    newMatrix = [[0 for col in range(c)] for row in range(r)]
    count = 0

    for newRow in range(r):
        for newCol in range(c):
            newRow, newCol = divmod(count, c)
            row, col = divmod(count, numCols)

            newMatrix[newRow][newCol] = mat[row][col]
            count += 1

    return newMatrix


print(matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4))
