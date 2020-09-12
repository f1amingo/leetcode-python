# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import *


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(r: TreeNode) -> int:
            if not r:
                return 0
            lt, rt = dfs(r.left), dfs(r.right)
            nonlocal res
            this_res = max(lt + r.val, rt + r.val, r.val)
            res = max(res, lt + rt + r.val, this_res)
            return this_res

        res = float('-inf')
        dfs(root)
        return res
