# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *


class Solution:
    # 非递归
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        cur, stk, res = root, [], []
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            res.append(cur.val)
            cur = cur.right
        return res
