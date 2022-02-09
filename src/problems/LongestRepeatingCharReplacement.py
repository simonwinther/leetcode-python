def characterReplacement(s: str, k: int) -> int:
    """
    You are given a string s and an integer k.
    You can choose any character of the string and change it to any other uppercase English character.
    You can perform this operation at most k times.
    Return the length of the longest substring containing
    the same letter you can get after performing the above operations.
    """

    windowStart, windowEnd = 0, 0
    maxRepeatingCounter = 0
    maxLength = 0
    frequencyMap = dict()

    for windowEnd in range(len(s)):

        currentElement = s[windowEnd]
        if currentElement not in frequencyMap:
            frequencyMap[currentElement] = 0
        frequencyMap[currentElement] += 1
        maxRepeatingCounter = max(maxRepeatingCounter, frequencyMap[currentElement])

        if (windowEnd - windowStart + 1 - maxRepeatingCounter) > k:
            charToRemove = s[windowStart]
            frequencyMap[charToRemove] -= 1
            windowStart += 1

        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength
