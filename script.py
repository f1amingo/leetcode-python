# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.ZTree import TreeNode


class Solution:

    # 迭代，LNR
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if pre >= root.val:
                return False
            pre = root.val
            root = root.right
        return True


    # BST中序遍历有序，递归
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def inOrder(node: TreeNode) -> bool:
    #         if node:
    #             lt = inOrder(node.left)
    #             nonlocal pre
    #             if not lt or pre >= node.val:  # BST不允许重复值！
    #                 return False
    #             pre = node.val  # 注意更新
    #             return inOrder(node.right)
    #         return True
    #
    #     pre = float('-inf')
    #     return inOrder(root)  # 默认返回True
