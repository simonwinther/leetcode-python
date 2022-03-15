def reverseBits(n: int) -> int:
    answer, power = 0, 31

    while n:
        answer += (n & 1) << power
        n = n >> 1
        power -= 1
    return answer
