from typing import List


def letterCasePermutation(s: str) -> List[str]:
    def backtrack(string: str, word: str, out: List[str]):
        if not string:
            out.append(word)
            return None

        if string[0].isalpha():
            backtrack(string[1:], word + string[0].lower(), out)
            backtrack(string[1:], word + string[0].upper(), out)
        else:
            backtrack(string[1:], word + string[0], out)

    output = []
    backtrack(s, '', output)
    return output


print(letterCasePermutation(s="a1b2"))
