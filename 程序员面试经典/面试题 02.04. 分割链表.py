# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from util.List import *


# 1.放到数组里排序，O(n+nlogn+n)
# 2.分成left, right两个链表，小入left，大入right，然后拼接，O(n)

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        lt_head, rt_head = ListNode(-1), ListNode(-1)
        lt, rt = lt_head, rt_head
        while head:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                rt.next = head
                rt = rt.next
            # head, head.next = head.next, None # 先算右边，这是错的
            # 一定要置空，否则会成环
            # head.next, head = None, head.next
            head = head.next
        lt.next = rt_head.next
        rt.next = None  # 只有rt的尾巴可能成环
        return lt_head.next


A = toLinkedList([3, 5, 8, 5, 10, 2, 1])
printLinkedList(Solution().partition(A, 5))
