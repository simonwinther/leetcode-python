from typing import Optional, List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return None

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level: List[Node] = []
        for _ in range(level_size):
            current_node: Node = queue.popleft()
            current_level.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        for i in range(len(current_level) - 1):
            current_level[i].next = current_level[i + 1]
    return root