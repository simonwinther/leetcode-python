def find_next_index(arr, is_forward, index):
    direction = arr[index] >= 0
    if is_forward != direction:
        return -1
    next_index = (index + arr[index]) % len(arr)
    if next_index == index:
        next_index = -1
    return next_index


def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow, fast = i, i

        while True:
            slow = find_next_index(arr, is_forward, slow)
            fast = find_next_index(arr, is_forward, fast)

            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True
    return False


print(circular_array_loop_exists([1, 2, -1, 2, 2]))
print(circular_array_loop_exists([2, 2, -1, 2]))
print(circular_array_loop_exists([2, 1, -1, -2]))
