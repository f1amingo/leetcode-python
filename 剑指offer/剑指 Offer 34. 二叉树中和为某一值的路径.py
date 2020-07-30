from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(r: TreeNode, s: int, path: List[int]):
            if not r:
                return
            s -= r.val
            path.append(r.val)
            if s == 0 and not r.left and not r.right:
                res.append(path)
            dfs(r.left, s, path.copy())
            dfs(r.right, s, path.copy())

        dfs(root, sum, [])
        return res


root = TreeNode(5)
left = TreeNode(4)
left_left = TreeNode(11)
left_left.left = TreeNode(7)
left_left.right = TreeNode(2)
root.left = left
left.left = left_left

right = TreeNode(8)
right_left = TreeNode(13)
right_right = TreeNode(4)
right_right.left = TreeNode(5)
right_right.right = TreeNode(1)
root.right = right
right.left = right_left
right.right = right_right

print(Solution().pathSum(root, 22))
