"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        found = {}
        dummy = Node(-1)
        new_head = dummy
        while head:
            copy_node = found.get(head, None)
            if not copy_node:
                copy_node = Node(head.val)
                found[head] = copy_node
            copy_random_node = found.get(head.random, None)
            if head.random:
                if not copy_random_node:
                    copy_random_node = Node(head.random.val)
                    found[head.random] = copy_random_node
            new_head.next = copy_node
            copy_node.random = copy_random_node
            new_head = new_head.next
            head = head.next
        return dummy.next

