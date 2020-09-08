# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from util.ZTree import TreeNode


class Solution:

    # iteration 只入栈右孩子
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        cur, stk, res = root, [], []
        while cur or stk:
            while cur:
                res.append(cur.val)
                stk.append(cur.right)
                cur = cur.left
            cur = stk.pop()
        return res

    # iteration
    # my solution 左右孩子都入栈
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     res = []
    #     stk = [root]
    #     while stk:
    #         node = stk.pop()
    #         res.append(node.val)
    #         if node.right:
    #             stk.append(node.right)
    #         if node.left:
    #             stk.append(node.left)
    #     return res

    # recursion
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #
    #     def dfs(_root: TreeNode):
    #         if not _root:
    #             return
    #         res.append(_root.val)
    #         dfs(_root.left)
    #         dfs(_root.right)
    #
    #     dfs(root)
    #     return res
