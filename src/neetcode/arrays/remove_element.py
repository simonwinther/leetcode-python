from typing import List


def removeElement(nums: List[int], val: int) -> int:
    pointer = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[pointer] = nums[i]
            pointer += 1

    return pointer


print(removeElement(nums=[3, 2, 2, 3], val=3))
print(removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
