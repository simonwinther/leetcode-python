from typing import List


def maxProfit(prices: List[int]) -> int:
    minPrice = float('inf')
    maxProf = 0

    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProf:
            maxProf = prices[i] - minPrice
    return maxProf


print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
