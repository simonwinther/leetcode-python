from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.
    """

    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output


print(permute(nums=[1, 2, 3]))
print(permute(nums=[0, 1]))
print(permute(nums=[1]))
