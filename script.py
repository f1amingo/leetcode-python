# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(r: TreeNode) -> int:
            if not r:
                return 0
            a = getHeight(r.left)
            if a == -1:
                return -1
            b = getHeight(r.right)
            if b == -1 or abs(a - b) > 1:
                return -1
            return max(a, b) + 1

        return getHeight(root) != -1
