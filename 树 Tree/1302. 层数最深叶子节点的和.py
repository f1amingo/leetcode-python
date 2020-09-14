# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(r: TreeNode, d: int):
            nonlocal res, depth
            if not r.left and not r.right:
                if d == depth:
                    res += r.val
                elif d > depth:
                    depth = d
                    res = r.val
            if r.left:
                dfs(r.left, d + 1)
            if r.right:
                dfs(r.right, d + 1)

        res = depth = 0
        dfs(root, 0)
        return res
