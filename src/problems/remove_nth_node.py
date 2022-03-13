from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    ptr = head
    size = 0
    while ptr is not None:
        size += 1
        ptr = ptr.next

    prev = head
    ptr = head.next
    i = 1

    if n >= size:
        head = head.next
        return head

    while i <= size - n:
        if i == size - n:
            prev.next = ptr.next
            ptr.next = prev
            return head
        prev = ptr
        ptr = ptr.next
        i += 1
