# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.ZList import ListNode


# 每个节点右移k，k>=0
# 1. k<N; k==N; k>N
# 找到连接点，断开，重连
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        N, ptr = 0, head
        while ptr:
            N += 1
            ptr = ptr.next
        k = k % N
        if k == 0:
            return head
        # 头结点会变
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(k):
            fast = fast.next
        while slow and fast.next:
            slow = slow.next
            fast = fast.next
        dummy.next = slow.next
        slow.next = None
        fast.next = head
        return dummy.next
