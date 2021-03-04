# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.ZList import *


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(a, b) -> ListNode:
            dummy = ptr = ListNode(-1)
            while a or b:
                if not a:
                    ptr.next = b
                    b = b.next
                elif not b:
                    ptr.next = a
                    a = a.next
                else:
                    if a.val <= b.val:
                        ptr.next = a
                        a = a.next
                    else:
                        ptr.next = b
                        b = b.next
                ptr = ptr.next
            return dummy.next

        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(mid)
        return merge(h1, h2)


h = toLinkedList([4, 2, 1, 3])
printLinkedList(Solution().sortList(h))
