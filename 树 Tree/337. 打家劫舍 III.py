# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *


class Solution:
    # 无需额外空间，直接递归中处理
    def rob(self, root: TreeNode) -> int:
        def _rob(r: TreeNode) -> (int, int):
            if not r:
                return 0, 0
            ls, ln = _rob(r.left)
            rs, rn = _rob(r.right)
            return r.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))

    # 双存储结构
    # def rob(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     memo_y, memo_n = {}, {}
    #     memo_n[None] = memo_y[None] = 0
    #
    #     def rob_squad(r: TreeNode) -> int:
    #         if not r:
    #             return 0
    #         rob_squad(r.left)
    #         rob_squad(r.right)
    #         memo_y[r] = r.val + memo_n[r.left] + memo_n[r.right]
    #         memo_n[r] = max(memo_y[r.left], memo_n[r.left]) + max(memo_y[r.right], memo_n[r.right])
    #
    #     rob_squad(root)
    #     return max(memo_y[root], memo_n[root])
