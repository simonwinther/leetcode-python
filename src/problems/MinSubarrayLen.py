import sys
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    """
    Given an array of positive integers nums and a positive integer target,
    return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
    of which the sum is greater than or equal to target.
    If there is no such subarray, return 0 instead.
    """
    windowStart: int = 0
    windowEnd: int = 0
    windowSum: int = 0
    minArraySize: int = sys.maxsize

    if sum(nums) < target:
        return 0

    while len(nums) > windowEnd >= windowStart:
        windowSum += nums[windowEnd]

        while windowSum >= target:
            minArraySize = min(minArraySize, windowEnd - windowStart + 1)
            windowSum -= nums[windowStart]
            windowStart += 1

        windowEnd += 1

    return minArraySize

print(minSubArrayLen(7, [2,3,1,2,4,3]))