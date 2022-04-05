import re


def isPalindrome(s: str) -> bool:
    t = ''.join(c for c in s if c.isalnum())
    t = t.lower()
    left, right = 0, len(t) - 1

    while left <= right:
        if t[left] != t[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome(s="A man, a plan, a canal: Panama"))
print(isPalindrome(s="race a car"))
print(isPalindrome(s=" "))
print(isPalindrome(s="0P"))
