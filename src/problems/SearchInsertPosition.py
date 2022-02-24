from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = start + (end - start) // 2

        if nums[middle] == target:
            return middle

        if nums[middle] > target:
            end = middle - 1
        else:
            start = middle + 1

    return start


# print(searchInsert([1, 3, 5, 6], 5))
# print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
