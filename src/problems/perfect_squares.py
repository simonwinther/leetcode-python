import math


def num_squares(n: int) -> int:
    square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
    dp = [(1 if i in square_nums else 0) for i in range(0, n + 1)]

    squaresLessThanI = []
    for i in range(1, n + 1):
        if dp[i] == 0:
            if not squaresLessThanI:
                squaresLessThanI = [square for square in square_nums if i > square]
            elif (i - 1) in square_nums:
                squaresLessThanI.append(i - 1)
            possibleWays = [dp[square] + dp[i - square] for square in squaresLessThanI]
            dp[i] = min(possibleWays)

    return dp[-1]