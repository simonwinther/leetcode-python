from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for t in tokens:
        if t not in '+-*/':
            stack.append(int(t))
        else:
            r, l = stack.pop(), stack.pop()

            if t == '+':
                stack.append(l + r)
            elif t == '-':
                stack.append(l - r)
            elif t == '*':
                stack.append(l * r)
            elif t == '/':
                stack.append(int(float(l) / r))
    return stack.pop()


print(evalRPN(tokens=["2", "1", "+", "3", "*"]))
print(evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
