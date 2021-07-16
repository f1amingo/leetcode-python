# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.ZList import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ptr1, ptr2 = headA, headB
        while ptr1 != ptr2:
            ptr1 = headB if ptr1 is None else ptr1.next
            ptr2 = headA if ptr2 is None else ptr2.next
        return ptr1
