from typing import List


def singleNumber(nums: List[int]) -> int:
    numsSet = set(nums)
    expected = 2 * sum(numsSet)
    actual = sum(nums)

    return expected - actual


def singleNumberBit(nums: List[int]) -> int:
    a: int = 0
    for i in nums:
        a ^= i
    return a


nums = [2, 2, 1]
print(singleNumberBit(nums))
