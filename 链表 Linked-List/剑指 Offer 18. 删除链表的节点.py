# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import ListNode


class Solution:
    # 单指针
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 删除头结点
        if head and head.val == val:
            return head.next
        cur = head
        # cur.next是要删除的节点
        while cur.next and cur.next.val != val:
            cur = cur.next
        # 要删除的节点是存在的，那么cur一定不为空
        if cur.next:
            cur.next = cur.next.next
        return head
    # dummy head
    # def deleteNode(self, head: ListNode, val: int) -> ListNode:
    #     if not head:
    #         return head
    #     dummy = ListNode(-1)
    #     dummy.next = head
    #     pre, cur = dummy, head
    #     while cur:
    #         if cur.val == val:
    #             break
    #         pre, cur = pre.next, cur.next  # 又漏了！
    #     if cur:
    #         pre.next = cur.next
    #         cur.next = None
    #     return dummy.next
