# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from util.ZTree import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stk = [root]
        ans = []
        while stk:
            cur = stk.pop()
            ans.append(cur.val)
            if cur.left:
                stk.append(cur.left)
            if cur.right:
                stk.append(cur.right)
        ans.reverse()
        return ans
