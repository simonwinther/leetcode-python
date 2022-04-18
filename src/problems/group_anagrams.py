import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = collections.defaultdict(list)

    for str in sorted(strs):
        key = tuple(sorted(str))
        result[key].append(str)

    return result.values()


print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams(strs=[""]))
print(groupAnagrams(strs=["a"]))
