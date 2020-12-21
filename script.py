# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(r: TreeNode) -> TreeNode:
            if r:
                lt, rt = r.left, r.right
                r.left, r.right = None, None
                r.right = dfs(lt)
                ptr = r
                while ptr and ptr.right:
                    ptr = ptr.right
                ptr.right = dfs(rt)
            return r

        dfs(root)
