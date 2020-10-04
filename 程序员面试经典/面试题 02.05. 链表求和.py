# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from util.List import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr = dummy = ListNode(-1)
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, val = divmod(val1 + val2 + carry, 10)
            ptr.next = ListNode(val)
            ptr = ptr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # 最后一次进位
        if carry:
            ptr.next = ListNode(1)
        return dummy.next


num1 = toLinkedList([7])
num2 = toLinkedList([5])
printLinkedList(Solution().addTwoNumbers(num1, num2))
