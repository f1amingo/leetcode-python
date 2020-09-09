# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(r: TreeNode, s: int, path: List):
            if r:
                s -= r.val
                if s == 0 and not r.left and not r.right:
                    res.append(path + [r.val])
                path.append(r.val)
                dfs(r.left, s, path)
                dfs(r.right, s, path)
                path.pop()

        dfs(root, sum, [])
        return res


roo = buildTreeFromList([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
re = Solution().pathSum(roo, 22)
print(re)
