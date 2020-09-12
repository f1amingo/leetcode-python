# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *
from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue, res = deque([root]), []
        while queue:
            this_size, this_sum = len(queue), 0
            for i in range(this_size):
                this_node = queue.popleft()
                this_sum += this_node.val
                if this_node.left:
                    queue.append(this_node.left)
                if this_node.right:
                    queue.append(this_node.right)
            res.append(this_sum / this_size)
        return res

print(Solution().averageOfLevels())
