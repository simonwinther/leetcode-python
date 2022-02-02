from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    result: List[int] = [1] * len(nums)
    result[0] = 1

    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]

    product: int = 1

    for j in range(len(nums) - 1, -1, -1):
        result[j] = result[j] * product
        product *= nums[j]

    return result
