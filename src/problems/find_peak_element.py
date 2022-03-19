from typing import List


def findPeakElement(nums: List[int]) -> int:
    """
    A peak element is an element that is strictly greater than its neighbors.
    Given an integer array nums, find a peak element, and return its index.
    If the array contains multiple peaks, return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞.
    You must write an algorithm that runs in O(log n) time.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return left


# print(findPeakElement(nums=[1, 2, 3, 1]))
# print(findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]))
print(findPeakElement(nums=[1, 3, 2, 1]))
