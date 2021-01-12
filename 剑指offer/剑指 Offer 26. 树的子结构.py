# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.ZTree import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 节点连续匹配，不可中断
        def dfs(X: TreeNode, Y: TreeNode) -> bool:
            if not Y:
                return True
            if not X:
                return False
            if X.val == Y.val:
                return dfs(X.left, Y.left) and dfs(X.right, Y.right)
            return False

        if not A or not B:
            return False
        if dfs(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
