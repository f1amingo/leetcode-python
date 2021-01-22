# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.List import *


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(h: ListNode):
            pre, cur = None, h
            while cur:
                tmp = cur.next
                cur.next = pre
                pre, cur = cur, tmp
            return pre

        dummy = ListNode(-1)
        dummy.next = head
        pre, post = dummy, dummy
        for _ in range(m - 1):
            pre = pre.next
        for _ in range(n):
            post = post.next
        # 断开链表
        tmp = post.next
        post.next = None
        post = tmp
        old_head = pre.next
        new_head = reverse(old_head)
        pre.next = new_head
        # 旧链表头反转后变成了尾
        old_head.next = post
        return dummy.next


h = toLinkedList([1, 2, 3, 4, 5])
printLinkedList(Solution().reverseBetween(h, 1, 5))
