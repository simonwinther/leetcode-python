from typing import List


def rotateExtraArray(nums: List[int], k: int) -> None:
    """
    Given an array, rotate the array to the right by k steps, where k is non-negative.

    Do not return anything, modify nums in-place instead.
    """

    array = [0] * len(nums)

    for i in range(len(nums)):
        array[(i + k) % len(nums)] = nums[i]

    nums[:] = array


def rotate(nums: List[int], k: int) -> None:
    start = count = 0
    n = len(nums)

    while count < n:
        current, prev = start, nums[start]
        while True:
            nextIdx = (current + k) % n
            nums[nextIdx], prev = prev, nums[nextIdx]
            current = nextIdx
            count += 1

            if start == current:
                break
        start += 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)


