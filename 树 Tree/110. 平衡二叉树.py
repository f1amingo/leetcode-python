# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 如何理解这个递归函数
        # 返回树的高度，max(L, R) + 1
        # 但是当节点不平衡时，返回 -1
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            L = dfs(node.left)
            # 小细节，提前判断
            # 而不等左右两边都计算完再判断
            # 可以提前终止
            if L == -1:
                return -1
            R = dfs(node.right)
            if R == -1:
                return -1
            return -1 if abs(L - R) > 1 else max(L, R) + 1

        return dfs(root) != -1
