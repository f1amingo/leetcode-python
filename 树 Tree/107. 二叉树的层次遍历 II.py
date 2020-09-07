# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level_list = []
            for i in range(len(queue)):
                front_node = queue.pop(0)
                level_list.append(front_node.val)
                if front_node.left:
                    queue.append(front_node.left)
                if front_node.right:
                    queue.append(front_node.right)
            res.append(level_list)
        res.reverse()
        return res
