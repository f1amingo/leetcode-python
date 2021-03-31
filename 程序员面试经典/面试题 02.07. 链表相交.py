# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from util.List import *


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptr1, ptr2 = headA, headB
        len1 = len2 = 0
        while ptr1:
            len1 += 1
            ptr1 = ptr1.next
        while ptr2:
            len2 += 1
            ptr2 = ptr2.next
        if len1 < len2:
            # 令A更长
            headA, headB = headB, headA
        diff = abs(len1 - len2)
        for i in range(diff):
            headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

prev_a  = ListNode(5)
a = ListNode(1)
b = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(4)
prev_a.next = a
a.next = node2
node2.next = node3
b.next = node2
printLinkedList(Solution().getIntersectionNode(a, b))
