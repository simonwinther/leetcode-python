from typing import List


def calPoints(ops: List[str]) -> int:
    stack = []
    for op in ops:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)


print(calPoints(ops=["5", "2", "C", "D", "+"]))
print(calPoints(ops=["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(calPoints(ops=["1", "C"]))
