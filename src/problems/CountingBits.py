from typing import List


def countBits(n: int) -> List[int]:
    """
    :param n: integer
    :return: return an array ans of length n + 1 such that for each i (0 <= i <= n),
    ans[i] is the number of 1's in the binary representation of i
    """
    result: List[int] = list()

    result.append(0)
    for i in range(1, n + 1):
        result.append(result[i & (i - 1)] + 1)

    return result


print(countBits(1))
print(countBits(5))
print(countBits(19))
