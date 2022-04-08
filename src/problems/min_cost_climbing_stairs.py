from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-2], cost[i-1])

    return min(cost[len(cost) - 2], cost[len(cost) - 1])


print(minCostClimbingStairs(cost=[10, 15, 20]))
print(minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
