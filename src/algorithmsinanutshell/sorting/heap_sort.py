from typing import List


def sort(array: List[int]):
    build_heap(array)

    for i in range(len(array) - 1, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)


def build_heap(array):
    for i in range(len(array) / 2 - 1, 0, -1):
        heapify(array, i, len(array))


def heapify(array, idx, max):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < max and array[left] > array[idx]:
        largest = left
    if right < max and array[right] > array[largest]:
        largest = right
    if largest != idx:
        array[idx], array[largest] = array[largest], array[idx]
        heapify(array, largest, max)
