# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s

