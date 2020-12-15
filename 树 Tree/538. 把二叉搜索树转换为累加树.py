# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(r: TreeNode):
            if r:
                dfs(r.right)
                nonlocal total
                total += r.val
                r.val = total
                dfs(r.left)
        total = 0
        dfs(root)
        return root
