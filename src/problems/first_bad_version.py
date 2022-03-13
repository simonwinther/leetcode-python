# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    ...


def firstBadVersion(n: int) -> int:
    start = 1
    end = n

    while start <= end:
        middle = start + (end - start) // 2

        if isBadVersion(middle) and not isBadVersion(middle - 1):  # if first bad number
            return middle

        if isBadVersion(middle):
            end = middle - 1
        elif not isBadVersion(middle):
            start = middle + 1

    return -1


