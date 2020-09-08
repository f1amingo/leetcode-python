# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.ZTree import *


class Solution:

    # 抄来的
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def getDepth(r: TreeNode) -> int:
            depth = 0
            while r:
                depth += 1
                r = r.left
            return depth

        ld = getDepth(root.left)
        rd = getDepth(root.right)
        if ld == rd:
            return (1 << ld) + self.countNodes(root.right)
        else:
            return (1 << rd) + self.countNodes(root.left)

    # 无脑递归
    # def countNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     return self.countNodes(root.left) + self.countNodes(root.right) + 1


roo = buildTreeFromList([1, 2, 3, 4, 5, 6, None])
print(Solution().countNodes(roo))
