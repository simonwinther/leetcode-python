from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def binarySearchLeft(n, t):
        l, r = 0, len(n) - 1
        while l <= r:
            pivot = (l + r) // 2
            if t > n[pivot]:
                l = pivot + 1
            else:
                r = pivot - 1
        return l

    def binarySearchRight(n, t):
        l, r = 0, len(n) - 1
        while l <= r:
            pivot = (l + r) // 2
            if t >= n[pivot]:
                l = pivot + 1
            else:
                r = pivot - 1
        return r

    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)

    return [left, right] if left <= right else [-1, -1]


print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
