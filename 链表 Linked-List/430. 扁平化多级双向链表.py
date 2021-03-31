"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        ptr = head
        if head and head.child:
            child_list = self.flatten(head.child)
            head.child = None
            next = head.next
            head.next = child_list
            child_list.prev = head
            ptr = head.next
            while ptr.next:
                ptr = ptr.next
            ptr.next = next
            if next:
                next.prev = ptr
        if ptr:
            self.flatten(ptr.next)
        return head


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node7.next = node8
node8.next = node9
node9.next = node10
node11.next = node12

node6.prev = node5
node5.prev = node4
node4.prev = node3
node3.prev = node2
node2.prev = node1

node10.prev = node9
node9.prev = node8
node8.prev = node7
node12.prev = node11

node3.child = node7
node8.child = node11

node = Solution().flatten(node1)
a = 1
