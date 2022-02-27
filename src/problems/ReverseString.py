from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        temp = s[i]
        s[i] = s[len(s) - i - 1]
        s[len(s) - i - 1] = temp


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)
