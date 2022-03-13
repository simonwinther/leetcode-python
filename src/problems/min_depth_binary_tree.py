from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    depth: int = 0
    queue = deque()
    queue.append(root)

    while queue:
        depth += 1
        for _ in range(len(queue)):
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            if current_node.left is None and current_node.right is None:
                return depth
