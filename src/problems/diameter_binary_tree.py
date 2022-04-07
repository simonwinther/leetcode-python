from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def height(root):
        nonlocal diameter
        if not root:
            return 0

        left = height(root.left)
        right = height(root.right)

        diameter = max(diameter, left + right)
        return max(left, right) + 1

    diameter = 0
    height(root)
    return diameter
