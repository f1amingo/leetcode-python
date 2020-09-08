# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import *


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        def dfs(node: TreeNode, cur_sum: int):
            nonlocal res
            cur_sum = cur_sum * 10 + node.val
            if node.left:
                dfs(node.left, cur_sum)
            if node.right:
                dfs(node.right, cur_sum)
            if not node.left and not node.right:
                res += cur_sum

        dfs(root, 0)
        return res


root = buildTreeFromList([1, 2, 3])
print(Solution().sumNumbers(root))
