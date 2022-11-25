from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    return nums + nums


def getConcatenation_fast(nums: List[int]) -> List[int]:
    size = 2 * len(nums)
    ans = [0] * size

    for i in range(len(nums)):
        ans[i] = nums[i]
        ans[i + len(nums)] = nums[i]
    return ans


print(getConcatenation_fast([1, 2, 1]))
print(getConcatenation_fast([1, 3, 2, 1]))
