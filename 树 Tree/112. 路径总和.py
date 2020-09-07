# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import TreeNode


class Solution:
    # 凡是数字，心中有正负
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            return True
        # 可能有负数
        # elif sum < 0:
        #     return False
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
