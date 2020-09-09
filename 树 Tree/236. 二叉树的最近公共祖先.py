# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import *


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 只有某一侧不为空，说明：
        # 1.p或q在这一侧
        # 2.p和q都在这侧（已经找到common ancestor了）
        if not left:
            return right
        if not right:
            return left
        # left, right都不为空，则p, q分布在左右两侧，返回当前节点
        return root


roo = buildTreeFromList([3, 5, 1, 6, 2, 10, 8, None, None, 7, 4])
a = getTreeNodeWithValue(roo, 5)
b = getTreeNodeWithValue(roo, 4)
print(Solution().lowestCommonAncestor(roo, a, b).val)
