# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from util.ZTree import *


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key < root.val:
            # 左子树中删除
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # 右子树中删除
            root.right = self.deleteNode(root.right, key)
        else:
            # 删除当前节点
            if not root.left:
                # 没有左子树，返回右子树
                root = root.right
            elif not root.right:
                # 没有右子树，返回左子树
                root = root.left
            else:
                # 左右子树都存在，右子树作为新的根
                # 左子树挂到右子树中最小节点上（作为最小节点的左子树）
                min_node = root.right
                while min_node.left:
                    min_node = min_node.left
                min_node.left = root.left
                root = root.right
        return root

    # def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    #     def successor(r):
    #         r = r.right
    #         while r.left:
    #             r = r.left
    #         return r.val
    #
    #     def predecessor(r):
    #         r = r.left
    #         while r.right:
    #             r = r.right
    #         return r.val
    #
    #     if not root:
    #         return root
    #     if key < root.val:
    #         root.left = self.deleteNode(root.left, key)
    #     elif key > root.val:
    #         root.right = self.deleteNode(root.right, key)
    #     else:
    #         if not root.left and not root.right:
    #             root = None
    #         elif root.left:
    #             root.val = predecessor(root)
    #             root.left = self.deleteNode(root.left, root.val)
    #         else:
    #             root.val = successor(root)
    #             root.right = self.deleteNode(root.right, root.val)
    #     return root


roo = buildTreeFromList([5, 3, 6, 2, 4, None, 7])
new_root = Solution().deleteNode(roo, 7)
a = 1
