from typing import List
from collections import defaultdict


def findAnagrams(s: str, p: str) -> List[int]:
    result: List = []
    window_start, window_end = 0, 0
    current_window: defaultdict = defaultdict(int)

    compare_dict = defaultdict(int)
    for e in p:
        compare_dict[e] += 1

    for window_end in range(len(s)):
        current_window[s[window_end]] += 1
        if window_end - window_start == len(p) - 1:
            if current_window == compare_dict:
                result.append(window_start)
            current_window[s[window_start]] -= 1
            if current_window[s[window_start]] == 0:
                del current_window[s[window_start]]
            window_start += 1
    return result


print(findAnagrams(s="cbaebabacd", p="abc"))
