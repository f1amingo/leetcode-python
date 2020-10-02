# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import *


class Solution:
    # 不使用额外空间，时间O(n^2)
    # def removeDuplicateNodes(self, head: ListNode) -> ListNode:
    #     slow = head
    #     while slow:
    #         fast = slow
    #         while fast.next:
    #             if fast.next.val == slow.val:
    #                 fast.next = fast.next.next
    #             else:
    #                 fast = fast.next
    #         slow = slow.next
    #     return head

    # 使用hash table
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        found = {}
        ptr = head
        while ptr:
            found[ptr.val] = True
            while ptr.next and ptr.next.val in found:
                ptr.next = ptr.next.next
            ptr = ptr.next
        # 头结点不会被改变
        return head


printLinkedList(Solution().removeDuplicateNodes(toLinkedList([1, 2, 3, 3, 2, 1])))
printLinkedList(Solution().removeDuplicateNodes(toLinkedList([1, 1])))
printLinkedList(Solution().removeDuplicateNodes(toLinkedList([1])))
