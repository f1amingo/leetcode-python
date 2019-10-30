# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(_root, _depth):
            if not _root:
                return _depth
            _depth += 1
            _depth = max(dfs(_root.left, _depth), dfs(_root.right, _depth))
            return _depth

        return dfs(root, 0)


root = TreeNode(3)
print(Solution().maxDepth(root))
