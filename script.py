# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lt, rt = ListNode(-1), ListNode(-1)
        ptr1, ptr2 = lt, rt
        while head:
            if head.val < x:
                ptr1.next = head
                ptr1 = ptr1.next
            else:
                ptr2.next = head
                ptr2 = ptr2.next
            head = head.next
        ptr2.next = None
        ptr1.next = rt.next
        return lt.next
