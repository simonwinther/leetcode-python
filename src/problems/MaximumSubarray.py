from typing import List


def maxSubArray(nums: List[int]) -> int:
    """
    Given an integer array nums,
    find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    We use Kadane's algorithm
    """
    bestSubarray = float('-inf')
    currentSubarray = 0

    for i in range(len(nums)):
        currentSubarray = max(nums[i], currentSubarray + nums[i])
        bestSubarray = max(bestSubarray, currentSubarray)

    return bestSubarray


print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
