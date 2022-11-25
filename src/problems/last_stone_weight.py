import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    # we use negative numbers because heapq is min heap
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)

        if first == second:
            continue
        else:
            heapq.heappush(heap, -(first - second))
    if len(heap) == 0:
        return 0
    else:
        return -heap[0]


print(lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
