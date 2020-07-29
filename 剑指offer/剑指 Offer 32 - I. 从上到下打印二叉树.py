import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Krahets
    # deque() popleft时间效率为O(1)
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    # my solution list.pop(0)时间复杂度为O(n)
    # def levelOrder(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     queue, res = [root], []
    #     while queue:
    #         node = queue.pop(0)
    #         res.append(node.val)
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     return res
