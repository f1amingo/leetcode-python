"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    # 中序遍历
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.head = self.pre = None

        def dfs(r: 'Node') -> 'Node':
            if not r:
                return
            dfs(r.left)
            if self.pre:
                self.pre.right = r
                r.left = self.pre
            else:  # 如果有pre那么一定有head
                self.head = r
            self.pre = r
            dfs(r.right)

        if not root:
            return None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
