from typing import List


def find_averages_of_subarray(k: int, arr: List) -> float:
    result = list()
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            result.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result


def max_k_subarray(k, arr):
    maxSum = 0
    windowSum, windowStart = 0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowSum > maxSum:
            maxSum = windowSum
        if windowEnd >= k - 1:
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum


def smallest_subarray_with_sum(s, arr):
    """"""
    windowSum, windowStart, windowEnd = 0, 0, 0
    minWindowSize = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowSum >= s:
            pass


