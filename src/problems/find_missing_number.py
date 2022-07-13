def find_missing_number(nums):
    n = len(nums)

    expected_sum = sum([i for i in range(n + 1)])
    actual_sum = sum(nums)

    return expected_sum - actual_sum


print(find_missing_number([4, 0, 3, 1]))
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


def find_missing_number_simple(nums):
    n = len(nums)
    expected_sum = 0
    actual_sum = 0

    for i in range(n + 1):
        expected_sum += i

    for n in nums:
        actual_sum += n

    return expected_sum - actual_sum


print(find_missing_number_simple([4, 0, 3, 1]))
print(find_missing_number_simple([8, 3, 5, 2, 4, 6, 0, 1]))
