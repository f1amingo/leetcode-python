# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import ListNode


class Solution(object):
    # 迭代
    def reverseList0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        ptr = head
        while ptr:
            _next = ptr.next
            ptr.next = pre
            pre = ptr
            ptr = _next
        return pre

    # 递归
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return p

    # 头插
    def reverseList2(self, head):
        dummy = ListNode(-1)
        while head:
            _next = head.next
            head.next = dummy.next
            dummy.next = head
            head = _next
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

node = Solution().reverseList(node1)

a = 1
