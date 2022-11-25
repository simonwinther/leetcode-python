from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    res = list()
    for i, j in zip(nums[:n], nums[n:]):
        res += [i, j]
    return res


print(shuffle(nums=[2, 5, 1, 3, 4, 7], n=3))
print(shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4))
print(shuffle(nums=[1, 1, 2, 2], n=2))
