def isPowerOfTwo(n: int) -> bool:
    if n == 0:
        return False
    return n & (n - 1) == 0


print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(3))