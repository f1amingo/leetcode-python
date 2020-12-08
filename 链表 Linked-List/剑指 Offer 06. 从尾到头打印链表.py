# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

from util.List import ListNode


class Solution:
    # 按序进，逆序
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.reverse()
        return res

    # 递归
    # def reversePrint(self, head: ListNode) -> List[int]:
    #     res = []
    #
    #     def recurPrint(h: ListNode):
    #         if h:
    #             recurPrint(h.next)
    #             res.append(h.val)
    #
    #     recurPrint(head)
    #     return res
