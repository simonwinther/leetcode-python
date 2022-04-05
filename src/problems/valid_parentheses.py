def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            current_element = stack.pop() if stack else '#'
            if mapping[char] != current_element:
                return False
        else:
            stack.append(char)
    return not stack


print(isValid(s="()"))
print(isValid(s="()[]{}"))
print(isValid(s="(]"))
