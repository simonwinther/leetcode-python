from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    You are given an array of integers nums,
    there is a sliding window of size k which is moving from the very
    left of the array to the very right.
    You can only see the k numbers in the window.
    Each time the sliding window moves right by one position.

    Return the max sliding window.
    """
    windowEnd: int = 0
    windowStart: int = 0
    resultList: List[int] = list()
    currentWindow: List[int] = list()

    for windowEnd in range(len(nums)):
        currentWindow.append(nums[windowEnd])
        if windowEnd >= k:
            currentWindow.remove(nums[windowStart])
            windowStart += 1

        if windowEnd >= k - 1:
            resultList.append(max(currentWindow))

    return resultList


def maxSlidingWindowFast(nums: List[int], k: int) -> List[int]:
    window: deque = deque()
    resultList: List[int] = list()

    for index, element in enumerate(nums):
        while window and window[-1][1] <= element:
            window.pop()
        while window and index - window[0][0] >= k:
            window.popleft()
        window.append((index, element))

        if index >= k - 1:
            resultList.append(window[0][1])

    return resultList


print(maxSlidingWindowFast(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
