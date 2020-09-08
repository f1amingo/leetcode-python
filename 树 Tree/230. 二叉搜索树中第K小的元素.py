# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from util.ZTree import *


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        seq, target = 1, None

        def in_order(node: TreeNode):
            if node:
                in_order(node.left)
                nonlocal seq, target
                if not target and seq == k:
                    target = node.val
                if target:
                    return
                seq += 1
                in_order(node.right)

        in_order(root)
        return target


roo = buildTreeFromList([3, 1, 4, None, 2])
print(Solution().kthSmallest(roo, 1))
