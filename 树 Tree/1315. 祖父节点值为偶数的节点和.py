# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(r: TreeNode, parent: TreeNode, grand_parent: TreeNode):
            if not r:
                return
            if grand_parent:
                nonlocal res
                res = res + r.val if grand_parent.val % 2 == 0 else res
            dfs(r.left, r, parent)
            dfs(r.right, r, parent)

        res = 0
        dfs(root, None, None)
        return res
