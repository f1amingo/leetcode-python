# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import *


class Solution:
    # 别人的
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

    # 自己琢磨出来的解法
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # P, Q是否存在当前树下
    #     def findPQ(r: 'TreeNode') -> (bool, bool):
    #         if not r:
    #             return False, False
    #         hasP, hasQ = (r.val == p.val), (r.val == q.val)
    #         ltP, ltQ = findPQ(r.left)
    #         hasP, hasQ = hasP or ltP, hasQ or ltQ
    #         # 左子树和当前节点已经含有P, Q
    #         # 则没有必要再递归右子树
    #         if not hasP or not hasQ:
    #             rtP, rtQ = findPQ(r.right)
    #             hasP, hasQ = hasP or rtP, hasQ or rtQ
    #         # 第一次同时找到P, Q，更新结果
    #         if hasP and hasQ:
    #             nonlocal ans
    #             if not ans:
    #                 ans = r
    #         return hasP, hasQ
    #
    #     ans = None
    #     findPQ(root)
    #     return ans


roo = buildTreeFromList([3, 5, 1, 6, 2, 10, 8, None, None, 7, 4])
a = getTreeNodeWithValue(roo, 5)
b = getTreeNodeWithValue(roo, 4)
print(Solution().lowestCommonAncestor(roo, a, b).val)
