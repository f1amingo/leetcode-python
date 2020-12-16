# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # 计算以r开始的路径
        def dfs(r: TreeNode, cur_sum: int) -> int:
            if not r:
                return 0
            cur_sum -= r.val
            return (1 if cur_sum == 0 else 0) + dfs(r.left, sum) + dfs(r.right, sum)

        if not root:
            return 0
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
