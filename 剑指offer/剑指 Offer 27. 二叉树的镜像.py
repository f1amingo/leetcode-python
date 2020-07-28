# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 栈写法
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stk = [root]
        while stk:
            top = stk.pop()
            top.left, top.right = top.right, top.left
            if top.left:
                stk.append(top.left)
            if top.right:
                stk.append(top.right)
        return root

    # 递归写法
    # def mirrorTree(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return None
    #     tmp = root.left
    #     root.left = self.mirrorTree(root.right)
    #     root.right = self.mirrorTree(tmp)
    #     return root
