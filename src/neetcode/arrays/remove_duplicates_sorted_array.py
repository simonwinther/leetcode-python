from typing import List


def removeDuplicates(nums: List[int]) -> int:
    duplicates = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            duplicates += 1
        else:
            nums[i - duplicates] = nums[i]

    return len(nums) - duplicates


print(removeDuplicates(nums=[1, 1, 2]))
print(removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
