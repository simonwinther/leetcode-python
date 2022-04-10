from typing import List


def generateParenthesis(n: int) -> List[str]:
    if n == 0:
        return []
    stack = [('(', 1, 0)]
    ans = []
    while stack:
        cur_ans, n_left, n_right = stack.pop()

        if len(cur_ans) == 2 * n:
            ans.append(cur_ans)
            continue
        if n_left < n:
            stack.append((cur_ans + '(', n_left + 1, n_right))
        if n_right < n_left:
            stack.append((cur_ans + ')', n_left, n_right + 1))
    return ans


print(generateParenthesis(3))
print(generateParenthesis(1))
