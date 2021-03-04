# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from util.ZTree import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # 增加孩子到父亲的连接
        def addEdge(node):
            if not node:
                return
            if node == target:
                return node
            lt = addEdge(node.left)
            if lt:
                lt.par = node
                return node
            rt = addEdge(node.right)
            if rt:
                rt.par = node
                return node

        # 从target开始深度搜索
        def dfs(node, depth):
            if not node or node in visit:
                return
            visit.add(node)
            if depth == K:
                ans.append(node.val)
                return
            # 判断一下是否存在par
            for nei in (node.left, node.right, node.par if hasattr(node, 'par') else None):
                dfs(nei, depth + 1)

        ans = []
        visit = set()

        addEdge(root)
        dfs(target, 0)

        return ans
