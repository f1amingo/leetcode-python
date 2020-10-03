# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from util.List import *


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        slow = fast = head
        for i in range(k):
            fast = fast.next  # k有效，这里不做空判断
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val


arr = toLinkedList([1, 2, 3, 4, 5])
print(Solution().kthToLast(arr, 2))
