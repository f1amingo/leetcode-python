# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import TreeNode


# 转化为求深度的问题
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 计算深度，并且会更新ans
        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            # 左右孩子的最大深度
            lt, rt = depth(node.left), depth(node.right)
            nonlocal ans
            # 尝试更新结果
            ans = max(ans, lt + rt)
            # 当前节点的最大深度
            return max(lt, rt) + 1

        if not root:
            return 0
        ans = 0
        depth(root)
        return ans
