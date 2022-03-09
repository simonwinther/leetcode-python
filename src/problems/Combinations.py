from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    """
    Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
    You may return the answer in any order.
    """

    def backtrack(first=1, current=[]):
        if len(current) == k:
            output.append(current[:])
        for i in range(first, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    output = []
    backtrack()
    return output


print(combine(n=4, k=2))
