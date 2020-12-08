# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.List import *


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # find medium
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse
        pre, cnt = None, slow.next
        slow.next = None
        while cnt:
            tmp = cnt.next
            cnt.next = pre
            pre, cnt = cnt, tmp
        ptr1, ptr2 = head, pre
        while ptr2:
            p1_next = ptr1.next
            ptr1.next = ptr2
            ptr2 = ptr2.next
            ptr1.next.next = p1_next
            ptr1 = p1_next


h = toLinkedList([1, 2, 3, 4, 5])
Solution().reorderList(h)
printLinkedList(h)
