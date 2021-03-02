# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.ZList import *


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        size = 0
        ptr = head
        while ptr:
            size += 1
            ptr = ptr.next
        k = k % size
        if k == 0:
            return head
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head


A = toLinkedList([1, 2, 3, 4, 5])
printLinkedList(Solution().rotateRight(A, 2))
