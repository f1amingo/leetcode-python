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
    # 使用已建立的next指针
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost:
            head = leftmost
            leftmost = ptr = None
            while head:
                if head.left:
                    if not leftmost:
                        leftmost = head.left
                    if ptr:
                        ptr.next = head.left
                    ptr = head.left
                if head.right:
                    if not leftmost:
                        leftmost = head.right
                    if ptr:
                        ptr.next = head.right
                    ptr = head.right
                head = head.next
        return root
