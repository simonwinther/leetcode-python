def find_first_k_missing_numbers(nums, k):
    missing_numbers = []

    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if len(nums) >= nums[i] > 0 and nums[i] != nums[j]:
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)
            if len(missing_numbers) == k:
                return missing_numbers

    if len(missing_numbers) < k:
        for i in range(max(nums), max(nums) + (k - len(missing_numbers))):
            missing_numbers.append(i + 1)

    return missing_numbers


print(find_first_k_missing_numbers([3, -1, 4, 5, 5], k=3))
print(find_first_k_missing_numbers([2, 3, 4], k=3))
print(find_first_k_missing_numbers([-2, -3, 4], k=2))
