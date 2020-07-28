# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(a: TreeNode, b: TreeNode) -> bool:
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return symmetric(a.left, b.right) and symmetric(a.right, b.left)

        return symmetric(root.left, root.right) if root else True
