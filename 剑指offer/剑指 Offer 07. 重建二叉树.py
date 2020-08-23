# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root_inorder = inorder.index(preorder[0])
        node = TreeNode(preorder[0])
        node.left = self.buildTree(preorder[1:1 + root_inorder], inorder[:root_inorder])
        node.right = self.buildTree(preorder[root_inorder + 1:], inorder[root_inorder + 1:])
        return node


node = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(node.val)