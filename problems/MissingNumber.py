from typing import List


def missingNumber(nums: List[int]) -> int:
    """Pattern: Array"""
    expected: int = 0
    actual: int = 0
    for i in range(len(nums) + 1):  # can replace with sum
        expected += i

    for num in nums:
        actual += num

    return expected - actual


def missingNumberGauss(nums: List[int]) -> int:
    expected = len(nums) * (len(nums) + 1) // 2
    actual = sum(nums)
    return expected - actual


numbers = [3, 0, 1]
print(missingNumber(numbers))
