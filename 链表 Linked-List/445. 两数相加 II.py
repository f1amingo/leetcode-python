# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import ListNode


class Solution:
    # 栈，头插
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stk1, stk2 = [], []
        # 放入栈中
        while l1 or l2:
            if l1:
                stk1.append(l1.val)
                l1 = l1.next
            if l2:
                stk2.append(l2.val)
                l2 = l2.next
        dummy = ListNode(-1)
        carry = 0
        # 对栈中元素进行相加
        while stk1 or stk2:
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            carry, val = divmod(val, 10)
            # 头插
            node = ListNode(val)
            node.next = dummy.next
            dummy.next = node
        # 处理最后一次进位
        if carry:
            node = ListNode(1)
            node.next = dummy.next
            dummy.next = node
        return dummy.next

    # 栈，逆序
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     stk1, stk2 = [], []
    #     # 放入栈中
    #     while l1 or l2:
    #         if l1:
    #             stk1.append(l1.val)
    #             l1 = l1.next
    #         if l2:
    #             stk2.append(l2.val)
    #             l2 = l2.next
    #     ptr = dummy = ListNode(-1)
    #     carry = 0
    #     # 对栈中元素进行相加
    #     while stk1 or stk2:
    #         val = carry
    #         if stk1:
    #             val += stk1.pop()
    #         if stk2:
    #             val += stk2.pop()
    #         carry, val = divmod(val, 10)
    #         ptr.next = ListNode(val)
    #         ptr = ptr.next
    #     # 处理最后一次进位
    #     if carry:
    #         ptr.next = ListNode(1)
    #     # 反转链表，高位在前
    #     pre, cur = None, dummy.next
    #     while cur:
    #         tmp = cur.next
    #         cur.next = pre
    #         pre, cur = cur, tmp
    #     return pre
