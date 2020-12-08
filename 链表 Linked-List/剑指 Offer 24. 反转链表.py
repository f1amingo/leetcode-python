# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import ListNode


class Solution:
    # 递归
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 先递归，reverse head.next开头的链表，返回了将来的头结点
        # head.next在这个过程中，没有被修改
        node = self.reverseList(head.next)
        # 这里才真正reverse
        head.next.next = head
        head.next = None
        return node

    # 迭代
    # def reverseList(self, head: ListNode) -> ListNode:
    #     pre, cur = None, head
    #     while cur:
    #         tmp = cur.next
    #         cur.next = pre
    #         pre, cur = cur, tmp
    #     return pre
