# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.ZList import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        ptr1, ptr2 = head, head
        for i in range(k):
            if not ptr2:
                return None
            ptr2 = ptr2.next
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
