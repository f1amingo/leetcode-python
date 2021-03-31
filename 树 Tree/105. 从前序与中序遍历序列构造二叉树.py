# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from util.ZTree import TreeNode


class Solution:
    # 递归
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        mid_in = 0  # 根在中序中的索引
        for i in inorder:
            if i == preorder[0]:
                break
            mid_in += 1
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:mid_in + 1], inorder[:mid_in])
        root.right = self.buildTree(preorder[mid_in + 1:], inorder[mid_in + 1:])
        return root
