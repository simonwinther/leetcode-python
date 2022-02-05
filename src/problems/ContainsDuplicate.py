from typing import List


def containsDuplicate(nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
