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
        # my solution
        # def dfs(_root, _depth):
        #     if not _root:
        #         return _depth
        #     _depth += 1
        #     _depth = max(dfs(_root.left, _depth), dfs(_root.right, _depth))
        #     return _depth
        #
        # return dfs(root, 0)

        # 参考的解法
        # if not root:
        #     return 0
        # left_height = self.maxDepth(root.left)
        # right_height = self.maxDepth(root.right)
        # return max(left_height, right_height) + 1

        # 栈的解法
        if not root:
            return 0
        max_height = 1
        stk = [(root, 1)]
        while stk:
            _root, height = stk.pop()
            if height > max_height:
                max_height = height
            if _root.left:
                stk.append((_root.left, height + 1))
            if _root.right:
                stk.append((_root.right, height + 1))
        return max_height


root = TreeNode(3)
print(Solution().maxDepth(root))
