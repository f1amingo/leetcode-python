# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from util.ZTree import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node: TreeNode):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        ans = []
        dfs(root)
        return ans
