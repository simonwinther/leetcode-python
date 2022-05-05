from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:
    index = len(nums) - 1
    curr_sum = 0

    def dp(nums, target, index, curr_sum):
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0

        positive = dp(nums, target, index - 1, curr_sum + nums[index])
        negative = dp(nums, target, index - 1, curr_sum + -nums[index])

        return positive + negative

    return dp(nums, target, index, curr_sum)


print(findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
print(findTargetSumWays(nums=[1], target=1))
