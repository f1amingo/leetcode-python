# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import TreeNode


class Solution:
    # 官方
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        if not t.left and not t.right:
            return str(t.val)
        if not t.right:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        return str(t.val) + '(' + self.tree2str(t.left) + ')(' + self.tree2str(t.right) + ')'

        # def tree2str(self, t: TreeNode) -> str:
    #     def preOrder(r: TreeNode):
    #         if r:
    #             stk.append(str(r.val))
    #             if r.left and r.right:
    #                 stk.append('(')
    #                 preOrder(r.left)
    #                 stk.append(')')
    #                 stk.append('(')
    #                 preOrder(r.right)
    #                 stk.append(')')
    #             elif r.left:
    #                 stk.append('(')
    #                 preOrder(r.left)
    #                 stk.append(')')
    #             elif r.right:
    #                 stk.append('(')
    #                 stk.append(')')
    #                 stk.append('(')
    #                 preOrder(r.right)
    #                 stk.append(')')
    #
    #     stk = []
    #     preOrder(t)
    #     return ''.join(stk)
