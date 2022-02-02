from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        previous = set()
        result = list()

        for num in nums:
            if num in previous:
                result.append(num)
            previous.add(num)

        return result

