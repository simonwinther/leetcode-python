def hammingWeight(n: int) -> int:
    answer = 0

    while n > 0:
        if n & 1:
            answer += 1
        n >>= 1

    return answer

# Missing test because of leetcode input format
