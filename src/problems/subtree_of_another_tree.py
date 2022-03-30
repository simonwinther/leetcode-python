from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        return p is q
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)