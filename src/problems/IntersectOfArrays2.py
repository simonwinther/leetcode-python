from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        intersect(nums2, nums1)

    hashMap = {}

    for num in nums1:
        if num not in hashMap:
            hashMap[num] = 0
        hashMap[num] += 1

    ans = []

    for num in nums2:
        count = hashMap.get(num, 0)

        if count > 0:
            ans.append(num)
            hashMap[num] -= 1
    return ans


print(intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
