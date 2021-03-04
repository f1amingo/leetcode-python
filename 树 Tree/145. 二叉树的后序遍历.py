# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import *


class Solution:
    # 后序LRN -> NRL遍历，再反转
    # 类似前序遍历
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, stk = [], [root]
        while stk:
            node = stk.pop()
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
            res.insert(0, node.val)  # 头插
        return res

    # recursion
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #
    #     def dfs(r: TreeNode):
    #         if r:
    #             nonlocal res
    #             dfs(r.left)
    #             dfs(r.right)
    #             res.append(r.val)
    #
    #     res = []
    #     dfs(root)
    #     return res


print(Solution().postorderTraversal())
