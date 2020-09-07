"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    # 迭代 利用父节点的next
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

    # 递归 利用父节点的next
    # def connect(self, root: 'Node') -> 'Node':
    #     if root and root.left and root.right:
    #         root.left.next = root.right
    #         if root.next:
    #             root.right.next = root.next.left
    #         self.connect(root.left)
    #         self.connect(root.right)
    #     return root
