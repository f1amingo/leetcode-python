# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import *


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        prev, stk = None, [root]
        while stk:
            node = stk.pop()
            if prev:
                prev.left = None
                prev.right = node
            prev = node
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)

    # 递归
    # def flatten(self, root: TreeNode) -> None:
    #     pre = None
    #
    #     def dfs(node: TreeNode):
    #         if not node:
    #             return
    #         nonlocal pre
    #         if pre:
    #             pre.right = node
    #         pre = node
    #         left, right = node.left, node.right
    #         dfs(left)
    #         node.left = None
    #         dfs(right)
    #
    #     dfs(root)


root = buildTreeFromList([1, 2, 5, 3, 4, None, 6])
Solution().flatten(root)
a = 1
