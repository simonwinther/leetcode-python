from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    low: int = 0
    high: int = len(numbers) - 1

    while low < high:
        sum = numbers[low] + numbers[high]

        if sum == target:
            return [low + 1, high + 1]
        elif sum < target:
            low += 1
        else:
            high -= 1

    return [-1, -1]


print(twoSum(numbers=[2, 7, 11, 15], target=9))
