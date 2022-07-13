from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    previous = set()
    result = list()

    for num in nums:
        if num in previous:
            result.append(num)
        previous.add(num)

    return result


def find_all_duplicates(nums):
    duplicateNumbers = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])
    return duplicateNumbers


print(find_all_duplicates([3, 4, 4, 5, 5]))
print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
