from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    """
    Given an integer array nums sorted in non-decreasing order,
    return an array of the squares of each number sorted in non-decreasing order.

    (can also be solved with two squares)
    """
    squared = [pow(e, 2) for e in nums]
    return sorted(squared)


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))
