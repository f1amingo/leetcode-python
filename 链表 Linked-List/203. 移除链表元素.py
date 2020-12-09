# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import ListNode


class Solution:
    # 单指针
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 删除头结点
        while head and head.val == val:
            head = head.next
        cur = head
        # 关键在于cur.next是要删除的点，从这个角度看问题
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    # dummy head
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     dummy = ListNode(-1)
    #     dummy.next = head
    #     cur = dummy
    #     while cur.next:
    #         if cur.next.val == val:
    #             cur.next = cur.next.next
    #         else:
    #             cur = cur.next
    #     return dummy.next
