# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, t: int):
            if not node:
                return
            t = 10 * t + node.val
            if not node.left and not node.right:
                nonlocal ans
                ans += t
            dfs(node.left, t)
            dfs(node.right, t)

        ans = 0
        dfs(root, 0)
        return ans
