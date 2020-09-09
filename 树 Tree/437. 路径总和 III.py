# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import *


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # 以r为起点，路径上path_sum == s的path
        def dfs(r: TreeNode, s: int):
            if not r:
                return 0
            s += r.val
            res = 1 if s == sum else 0
            return res + dfs(r.left, s) + dfs(r.right, s)

        if not root:
            return 0
        return dfs(root, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


roo = buildTreeFromList([])
print(Solution().pathSum(roo, 8))
