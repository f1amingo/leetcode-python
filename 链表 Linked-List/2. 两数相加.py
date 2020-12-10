# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.List import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        ptr = dummy
        carry = 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            ptr.next = ListNode(val)
            ptr = ptr.next
        # 最后一次进位，总是错！！！
        if carry:
            ptr.next = ListNode(1)
        return dummy.next
