# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.List import *


class Solution:
    # 直接在原链表上操作指针
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        guard, soldier = head, head.next
        while soldier and soldier.next:
            to_kill = soldier.next
            soldier.next = to_kill.next
            to_kill.next = guard.next
            guard.next = to_kill
            guard = guard.next
            soldier = soldier.next
        return head

    # 分两个链表处理
    # def oddEvenList(self, head: ListNode) -> ListNode:
    #     odd_head, even_head = ListNode(-1), ListNode(-1)
    #     odd, even = odd_head, even_head
    #     i = 1
    #     while head:
    #         if i % 2 == 1:
    #             odd.next = head
    #             odd = odd.next
    #         else:
    #             even.next = head
    #             even = even.next
    #         i += 1
    #         head = head.next
    #     odd.next = even_head.next
    #     even.next = None
    #     return odd_head.next


head = toLinkedList([1, 2, 3, 4, 5])
printLinkedList(Solution().oddEvenList(head))
