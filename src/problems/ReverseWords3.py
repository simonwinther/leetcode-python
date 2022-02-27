def reverseWords(s: str) -> str:
    result: str = ""
    for word in s.split(" "):
        result += word[::-1]  # Reverse string
        result += " "
    return result.strip()


print(reverseWords(s="Let's take LeetCode contest"))
