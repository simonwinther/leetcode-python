from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = defaultdict(int)
    t_dict = defaultdict(int)

    for c in s:
        s_dict[c] += 1
    for c in t:
        t_dict[c] += 1

    return s_dict == t_dict


print(isAnagram(s="anagram", t="nagaram"))
print(isAnagram(s="rat", t="car"))
