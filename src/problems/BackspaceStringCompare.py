from collections import deque


def backspaceCompare(s: str, t: str) -> bool:
    """
    :param s: string where # means backspace
    :param t: string where # means backspace
    :return: true if both strings are the same after backspaces
    """
    sQueue = deque()
    tQueue = deque()

    for element in s:
        if element == '#':
            if sQueue:
                sQueue.pop()
        else:
            sQueue.append(element)

    for element in t:
        if element == '#':
            if tQueue:
                tQueue.pop()
        else:
            tQueue.append(element)

    if sQueue == tQueue:
        return True
    return False


print(backspaceCompare(s="y#fo##f", t="y#f#o##f"))
