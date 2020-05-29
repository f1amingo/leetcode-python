# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)


root = TreeNode(10)
left = TreeNode(5)
right = TreeNode(15)
right_left = TreeNode(6)
right_right = TreeNode(20)

root.left = left
root.right = right
right.left = right_left
right.right = right_right

print(Solution().isValidBST(root))

a = 1
