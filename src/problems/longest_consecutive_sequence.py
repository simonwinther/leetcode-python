from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    sorted_nums = sorted(nums)

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if sorted_nums[i] == sorted_nums[i - 1] :
            continue
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1
    return max(longest_streak, current_streak)


print(longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
