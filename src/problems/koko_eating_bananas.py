from typing import List
import math


def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if sum(math.ceil(1.0 * pile / mid) for pile in piles) > h:
            left = mid + 1
        else:
            right = mid
    return left


print(minEatingSpeed([3, 6, 7, 11], 8))
print(minEatingSpeed([30, 11, 23, 4, 20], 5))
print(minEatingSpeed([30, 11, 23, 4, 20], 6))
