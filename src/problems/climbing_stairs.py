def climbStairs(n: int) -> int:
    if n == 1:
        return 1

    first: int = 1
    second: int = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second


print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
