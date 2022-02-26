from typing import List


def moveZeroesExtraArray(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    array = [0] * len(nums)
    inserted = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        else:
            array[inserted] = nums[i]
            inserted += 1

    nums[:] = array


nums = [0, 1, 0, 3, 12]
moveZeroesExtraArray(nums)
print(nums)
