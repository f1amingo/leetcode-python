# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.ZList import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        ptr1, ptr2 = dummy, head
        for i in range(n):
            ptr2 = ptr2.next
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr1.next.next
        return dummy.next
