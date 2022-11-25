from typing import List


def sort(array: List[int]):
    for i in range(1, len(array)):
        insert(array, i, array[i])


def insert(array, position, value):
    i = position - 1
    while i > 0 and array[i] > value:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = value

