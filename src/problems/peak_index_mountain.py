from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    """
    :param arr: guaranteed to be a mountain array
    :return: return index of peak
    """
    for i in range((len(arr))):
        if arr[i] > arr[i + 1]:
            return i


def peakIndexInMountainArrayBinary(arr: List[int]) -> int:
    """
    :param arr: guaranteed to be a mountain array
    :return: return index of peak
    """
    low = 0
    high = len(arr) - 1

    while low < high:

        middle = low + (high - low) // 2

        if arr[middle] < arr[middle + 1]:
            low = middle + 1
        else:
            high = middle
    return low


print(peakIndexInMountainArrayBinary(arr=[0, 10, 6, 5, 2]))
