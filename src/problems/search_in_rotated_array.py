from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        pivot = (left + right) // 2

        if nums[pivot] == target:
            return pivot

        if nums[pivot] >= nums[left]:
            if nums[left] <= target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        else:
            if nums[right] >= target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
    return - 1

print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(search(nums=[1], target=0))
print(search(nums=[1, 3], target=3))
