from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


print(findMin(nums=[3, 4, 5, 1, 2]))
print(findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(findMin(nums=[11, 13, 15, 17]))
