# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
from typing import List

from util.ZTree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        ans = []
        flag = False
        while queue:
            tmp_list = [0] * len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                tmp_list[i] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag:
                tmp_list.reverse()
            flag = not flag
            ans.append(tmp_list)
        return ans
