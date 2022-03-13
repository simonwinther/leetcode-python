from typing import List


def majorityElement(nums: List[int]) -> int:
    """
    Given an array nums of size n,
    return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

    Will be using Boyer-Moore Maj. Voting Algorithm
    """
    m: int = 0
    i: int = 0

    for num in nums:
        if i == 0:
            m = num
            i = 1
        elif num == m:
            i += 1
        else:
            i -= 1

    return m


print(majorityElement(nums=[3, 3, 4]))
