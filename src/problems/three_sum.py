from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    :param nums:
    :return: all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
    and j != k, and nums[i] + nums[j] + nums[k] == 0
    """
    nums.sort()
    n = len(nums)
    triplets = list()

    for i in range(0, n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                triplets.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
    return triplets


print(threeSum([-1, 0, 1, 2, -1, -4]))
