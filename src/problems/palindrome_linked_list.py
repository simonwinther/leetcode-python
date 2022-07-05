class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow)
    copy_second_half = head_second_half

    head_first_half = head
    while head_first_half is not None and head_second_half is not None:
        if head_first_half.value != head_second_half.value:
            return False
        head_first_half = head_first_half.next
        head_second_half = head_second_half.next

    reverse(copy_second_half)

    return True


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)

print("Is palindrome: " + str(is_palindromic_linked_list(head)))

head.next.next.next.next.next = Node(2)
print("Is palindrome: " + str(is_palindromic_linked_list(head)))
