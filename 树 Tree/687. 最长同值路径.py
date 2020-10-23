# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import *


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 计算以r为根的最长同值路径，并返回
        # 在此过程中记录下整棵树的最大值
        def dfs(r: TreeNode) -> int:
            if not r:
                return 0
            # 递归先往下走
            lt_len = dfs(r.left)
            rt_len = dfs(r.right)
            lt_arrow = rt_arrow = 0
            if r.left and r.val == r.left.val:
                lt_arrow = lt_len + 1
            if r.right and r.val == r.right.val:
                rt_arrow = rt_len + 1
            self.ans = max(self.ans, lt_arrow + rt_arrow)
            return max(lt_arrow, rt_arrow)

        self.ans = 0
        dfs(root)
        return self.ans

    # 下面实现错的，不知道写了个啥
    # def longestUnivaluePath(self, root: TreeNode) -> int:
    #     def dfs(r: TreeNode) -> int:
    #         if not r:
    #             return 0
    #         lt_path, rt_path = 0, 0
    #         if r.left and r.val == r.left.val:
    #             lt_path = dfs(r.left) + 1
    #         if r.right and r.val == r.right.val:
    #             rt_path = dfs(r.right) + 1
    #         return max(lt_path, rt_path)
    #
    #     lt = self.longestUnivaluePath(root.left) if root.left else 0
    #     rt = self.longestUnivaluePath(root.right) if root.right else 0
    #
    #     return max(dfs(root), lt, rt)


print(Solution().longestUnivaluePath(buildTreeFromList([5, 4, 5, 1, 1, 5])))
