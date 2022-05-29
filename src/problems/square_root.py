def mySqrt(x: int) -> int:
    """
    assume x is non negative, truncate result, do not use built-in functions
    """
    low, high = 0, x

    while low <= high:
        middle = low + (high - low) // 2
        if middle * middle < x:
            low = middle + 1
        elif middle * middle > x:
            high = middle - 1
        else:
            return middle
    return high


print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(1))
print(mySqrt(3))
