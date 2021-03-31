# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import *


class Solution:
    # 双指针
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m, n = 0, 0
        p, q = headA, headB
        while p:
            m += 1
            p = p.next
        while q:
            n += 1
            q = q.next
        if m < n:
            # 令A更长
            headA, headB = headB, headA
            m, n = n, m
        for i in range(m - n):
            headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None
