import collections
from idlelib.tree import TreeNode
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        to_right = True
        while queue:
            tmp, new_queue = [], collections.deque()
            while queue:
                node = queue.popleft() if to_right else queue.pop()
                tmp.append(node.val)
                if to_right:
                    if node.left:
                        new_queue.append(node.left)
                    if node.right:
                        new_queue.append(node.right)
                else:
                    if node.right:
                        new_queue.appendleft(node.right)
                    if node.left:
                        new_queue.appendleft(node.left)
            to_right = not to_right
            queue = new_queue
            res.append(tmp)
        return res


root = TreeNode(1)
left = TreeNode(2)
left.left = TreeNode(4)
right = TreeNode(3)
right.right = TreeNode(5)
root.left = left
root.right = right

print(Solution().levelOrder(root))
