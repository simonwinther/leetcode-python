from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:

    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            out_pair = isMirror(left.left, right.right)
            in_pair = isMirror(left.right, right.left)
            return out_pair and in_pair
        else:
            return False

    if not root:
        return True
    else:
        return isMirror(root.left, root.right)


root_right_left = TreeNode(4)
root_right_right = TreeNode(3)
root_left_left = TreeNode(3)
root_left_right = TreeNode(4)
root_left = TreeNode(2, root_left_left, root_left_right)
root_right = TreeNode(2, root_right_left, root_right_right)
root = TreeNode(1, root_left, root_right)

print(isSymmetric(root))
