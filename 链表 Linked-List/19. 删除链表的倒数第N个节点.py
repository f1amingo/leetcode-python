# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.List import ListNode


# 倒数第n个节点，从1开始
# n是否一定有效？是
# 头结点可能被修改
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        # slow.next即为被删节点，不为None
        slow.next = slow.next.next
        return dummy.next
