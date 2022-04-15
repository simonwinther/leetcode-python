# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or not p or not q:
        return None

    if max(p.val, q.val) < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif min(p.val, q.val) > root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root