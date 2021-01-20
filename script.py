# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.List import *


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(h: ListNode) -> (ListNode, ListNode):
            cur, pre = h, None
            tail = h
            while cur:
                tmp = cur.next
                cur.next = pre
                cur, pre = tmp, cur
            return pre, tail

        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy
        while p1.next:
            flag = False
            for _ in range(k):
                if not p2.next:
                    flag = True
                    break
                p2 = p2.next
            if flag:
                break
            p2_next = p2.next
            p2.next = None
            this_head, this_tail = reverse(p1.next)
            p1.next = this_head
            this_tail.next = p2_next
            p1 = p2 = this_tail
        return dummy.next


printLinkedList(Solution().reverseKGroup(toLinkedList([1, 2, 3, 4, 5]), 3))
