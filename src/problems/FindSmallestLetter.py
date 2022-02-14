from typing import List


def nextGreatestLetter(letters: List[str], target: str) -> str:
    start = 0
    end = len(letters) - 1

    while start <= end:

        middle = start + (end - start) // 2

        if letters[middle] > target:
            end = middle - 1
        else:
            start = middle + 1

    return letters[start % len(letters)]


print(nextGreatestLetter(letters=["c", "f", "j"], target="q"))
