from typing import List, Optional


def tribonacci(n: int) -> int:
    memo: List[Optional[int]] = [0 for _ in range(38)]
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1

    for i in range(3, n + 1):
        memo[i] = memo[i - 3] + memo[i - 2] + memo[i - 1]

    return memo[n]


print(tribonacci(n=4))
print(tribonacci(n=25))
