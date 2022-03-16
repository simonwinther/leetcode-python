from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0:
        return False

    m = len(matrix)
    n = len(matrix[0])

    left, right = 0, m * n - 1

    while left <= right:
        pivot_index = (left + right) // 2
        pivot_element = matrix[pivot_index // n][pivot_index % n]
        if pivot_element == target:
            return True
        else:
            if pivot_element > target:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
    return False


print(searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
