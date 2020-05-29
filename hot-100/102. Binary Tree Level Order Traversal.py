# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def traversal(node, level):
            if not node:
                return
            if level > len(res):
                res.append([])
            res[level - 1].append(node.val)
            traversal(node.left, level + 1)
            traversal(node.right, level + 1)

        traversal(root, 1)
        return res


root = TreeNode(3)
left = TreeNode(9)
right = TreeNode(20)
rightLeft = TreeNode(15)
rightRight = TreeNode(7)

root.left = left
root.right = right

right.left = rightLeft
right.right = rightRight

print(Solution().levelOrder(root))
