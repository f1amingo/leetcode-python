# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from util.ZTree import *
from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue, res = deque([root]), []
        while queue:
            this_max = float('-inf')
            for i in range(len(queue)):
                node = queue.popleft()
                this_max = max(this_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(this_max)
        return res
