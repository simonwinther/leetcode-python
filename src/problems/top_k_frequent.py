import heapq
from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return nums

    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(topKFrequent(nums=[1], k=1))
