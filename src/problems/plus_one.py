from typing import List


def plusOne(digits: List[int]) -> List[int]:
    digit_string = ''.join([str(e) for e in digits])
    result = int(digit_string) + 1
    return [int(i) for i in str(result)]


print(plusOne(digits=[1, 2, 3]))
print(plusOne(digits=[4, 3, 2, 1]))
print(plusOne(digits=[9]))
