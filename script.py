# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from util.ZTree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, cur, stk = [], root, []
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
