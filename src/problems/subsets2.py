from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []

    def backtrack(first=0, curr=[]):
        ans.append(curr[:])

        for i in range(first, len(nums)):
            if i > first and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    backtrack()
    return ans


print(subsetsWithDup([1, 2, 2]))
print(subsetsWithDup([0]))
