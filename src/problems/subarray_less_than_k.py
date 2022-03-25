from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    result = 0
    product = 1
    window_start = 0

    for window_end, num in enumerate(nums):
        product *= num
        while product >= k:
            product //= nums[window_start]
            window_start += 1

        result += window_end - window_start + 1

    return result


print(numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
