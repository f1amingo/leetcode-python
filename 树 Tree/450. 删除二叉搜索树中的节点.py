# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from util.ZTree import *


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def successor(r):
            r = r.right
            while r.left:
                r = r.left
            return r.val

        def predecessor(r):
            r = r.left
            while r.right:
                r = r.right
            return r.val

        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = successor(root)
                root.right = self.deleteNode(root.right, root.val)
        return root


roo = buildTreeFromList([5, 3, 6, 2, 4, None, 7])
new_root = Solution().deleteNode(roo, 7)
a = 1
