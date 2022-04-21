from collections import Counter


def minWindow(s: str, t: str):
    need = Counter(t)
    missing = len(t)
    start, end = 0, 0
    window_start = 0
    for window_end, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:
            while window_start < window_end and need[s[window_start]] < 0:
                need[s[window_start]] += 1
                window_start += 1
            need[s[window_start]] += 1
            missing += 1
            if end == 0 or window_end - window_start < end - start:
                start, end = window_start, window_end
            window_start += 1
    return s[start:end]


print(minWindow(s="ADOBECODEBANC", t="ABC"))
print(minWindow(s="a", t="a"))
print(minWindow(s="a", t="aa"))
