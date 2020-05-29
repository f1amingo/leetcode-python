# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def mergeTrees(self, t1, t2):
    #     """
    #     :type t1: TreeNode
    #     :type t2: TreeNode
    #     :rtype: TreeNode
    #     """
    #     root = TreeNode(0)
    #     if not t1 and not t2:
    #         return None
    #     if t1 and not t2:
    #         root.val = t1.val
    #         root.left = self.mergeTrees(t1.left, t2)
    #         root.right = self.mergeTrees(t1.right, t2)
    #     elif t2 and not t1:
    #         root.val = t2.val
    #         root.left = self.mergeTrees(t1, t2.left)
    #         root.right = self.mergeTrees(t1, t2.right)
    #     else:
    #         root.val = t1.val + t2.val
    #         root.left = self.mergeTrees(t1.left, t2.left)
    #         root.right = self.mergeTrees(t1.right, t2.right)
    #     return root

    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root


t1 = TreeNode(1)
t1left = TreeNode(3)
t1right = TreeNode(2)
t1leftleft = TreeNode(5)

t1.left = t1left
t1.right = t1right
t1left.left = t1leftleft

t2 = TreeNode(2)
t2left = TreeNode(1)
t2right = TreeNode(3)
t2leftright = TreeNode(4)
t2rightright = TreeNode(7)

t2.left = t2left
t2.right = t2right
t2left.right = t2leftright
t2right.right = t2rightright

Solution().mergeTrees(t1, t2)

a = 1
