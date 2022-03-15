from typing import List, Optional


def rob(nums: List[int]) -> int:
    """You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed,
    the only constraint stopping you from robbing each of them is that adjacent
    houses have security systems connected and it will automatically contact the
    police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob tonight without alerting the police.
    """
    if not nums:
        return 0

    N = len(nums)
    max_robbed_amount: List[Optional[int]] = [None for _ in range(N + 1)]
    max_robbed_amount[N], max_robbed_amount[N - 1] = 0, nums[N - 1]

    for i in range(N - 2, -1, -1):
        max_robbed_amount[i] = max(max_robbed_amount[i + 1], max_robbed_amount[i + 2] + nums[i])

    return max_robbed_amount[0]


print(rob(nums=[2, 7, 9, 3, 1]))
