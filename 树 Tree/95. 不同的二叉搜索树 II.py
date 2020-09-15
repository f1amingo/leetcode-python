# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from util.ZTree import *


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(start: int, end: int) -> List[TreeNode]:
            if start >= end:
                # 一定要返回None，不然后面不会进循环
                return [None]
            # 返回一个列表
            res = []
            for i in range(start, end):
                lt_children = dfs(start, i)
                rt_children = dfs(i + 1, end)
                for lt in lt_children:
                    for rt in rt_children:
                        node = TreeNode(i)
                        node.left = lt
                        node.right = rt
                        res.append(node)
            return res

        return dfs(1, n + 1) if n else []


r = Solution().generateTrees(3)
a = 1
