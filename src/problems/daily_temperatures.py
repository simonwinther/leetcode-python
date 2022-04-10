from typing import List


def dailyTemperaturesBruteForce(temperatures: List[int]) -> List[int]:
    result = []
    for i in range(len(temperatures)):
        if i == len(temperatures) - 1:
            result.append(0)
        for j in range(1, len(temperatures) - i):
            if temperatures[i + j] > temperatures[i]:
                result.append(j)
                break
            if i + j == len(temperatures) - 1:
                result.append(0)
                break
    return result


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            curr = stack.pop()
            result[curr] = i - curr
        stack.append(i)
    return result


print(dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures(temperatures=[30, 40, 50, 60]))
print(dailyTemperatures(temperatures=[30, 60, 90]))
