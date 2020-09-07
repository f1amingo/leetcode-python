# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(_root: TreeNode, _path: List):
            if not _root:
                return
            _path.append(str(_root.val))
            if not _root.left and not _root.right:
                res.append('->'.join(_path))
                _path.pop()
                return
            dfs(_root.left, _path)
            dfs(_root.right, _path)
            _path.pop()

        dfs(root, [])
        return res


print(Solution().binaryTreePaths())
