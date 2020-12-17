# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import TreeNode


class Solution:
    # 每个节点返回(偷，不偷)
    def rob(self, root: TreeNode) -> int:
        def dfs(r: TreeNode) -> (int, int):
            if not r:
                return 0, 0
            left, right = dfs(r.left), dfs(r.right)
            do_rob = r.val + left[1] + right[1]
            no_rob = max(left) + max(right)
            return do_rob, no_rob

        return max(dfs(root))


Solution().rob()
