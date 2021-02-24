# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import ListNode


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4

Solution().deleteNode(node2)

a = 1
