# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from util.ZTree import *


# 基于栈的中序遍历
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = []
        while root:
            self.stk.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.stk.pop()
        cur = res.right
        while cur:
            self.stk.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stk) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
