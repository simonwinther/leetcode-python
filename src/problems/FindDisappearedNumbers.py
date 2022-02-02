from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    result = set()
    numsSet = set(nums)

    for i in range(1, len(nums) + 1):
        result.add(i)

    for num in numsSet:
        result.remove(num)

    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))
