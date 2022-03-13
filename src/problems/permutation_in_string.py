from collections import defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.
    """
    expectedDictionary = defaultdict(int)
    actualDictionary = defaultdict(int)

    for c in s1:
        expectedDictionary[c] += 1

    for windowEnd in range(len(s2)):
        actualDictionary[s2[windowEnd]] += 1
        if windowEnd >= len(s1):
            removeElement = s2[windowEnd - len(s1)]
            actualDictionary[removeElement] -= 1
            if actualDictionary[removeElement] == 0:
                del actualDictionary[removeElement]
        if actualDictionary == expectedDictionary:
            return True

    return False


s1 = "a"
s2 = "ab"
print(checkInclusion(s1, s2))
