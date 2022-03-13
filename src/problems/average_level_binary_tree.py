from collections import deque
from typing import Optional, List
import statistics


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if root is None:
        return None

    queue = deque()
    queue.append(root)
    result = list()
    while queue:
        current_level = []
        for _ in range(len(queue)):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(statistics.mean(current_level))
    return result
