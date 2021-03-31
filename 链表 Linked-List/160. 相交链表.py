# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.ZList import ListNode


# 腾讯CSIG挂！
# A的长度：a + c; B的长度：b + c
# a + c + b + c = b + c + a +c
# 如果两个链表不相交：a + b = b + a，相交为None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA.next else headB
            pB = pB.next if pB.next else headA
        return pA
