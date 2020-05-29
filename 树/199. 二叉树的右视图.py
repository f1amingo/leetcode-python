# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            cur_n = len(queue)
            for i in range(cur_n):
                top_ele = queue.pop(0)
                if top_ele.left:
                    queue.append(top_ele.left)
                if top_ele.right:
                    queue.append(top_ele.right)
                if i == cur_n - 1:
                    ans.append(top_ele.val)
        return ans


r = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node5 = TreeNode(5)
node4 = TreeNode(4)
r.left = node2
r.right = node3
node2.right = node5
node3.left = node4

print(Solution().rightSideView(r))
