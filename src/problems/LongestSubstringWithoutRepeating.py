def lengthOfLongestSubstring(s: str) -> int:
    windowStart, windowEnd = 0, 0
    maxLength = 0
    indexMap = dict()

    for windowEnd in range(len(s)):
        currentElement = s[windowEnd]
        if currentElement not in indexMap:
            indexMap[currentElement] = windowEnd
        else:
            for i in range(windowStart, indexMap[currentElement]):
                del indexMap[s[i]]
            windowStart = indexMap[currentElement] + 1
            indexMap[currentElement] = windowEnd
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength


print(lengthOfLongestSubstring("abcabcbbabcde"))
# print(lengthOfLongestSubstring("pwwkew"))
