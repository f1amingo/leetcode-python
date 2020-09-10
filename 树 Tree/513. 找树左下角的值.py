# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

from util.ZTree import *


class Solution:
    # 从右到左遍历，最后一个元素就是最左元素
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue, node = deque([root]), None
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return node.val

    # 从左到右层次遍历，使用一个leftmost变量记录每层最左元素
    # def findBottomLeftValue(self, root: TreeNode) -> int:
    #     if not root:
    #         return -1
    #     queue, leftmost = deque([root]), None
    #     while queue:
    #         leftmost = None
    #         for i in range(len(queue)):
    #             node = queue.popleft()
    #             if not leftmost:
    #                 leftmost = node
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #     return leftmost.val
