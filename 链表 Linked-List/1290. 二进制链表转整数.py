# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import *


class Solution:
    # 似乎不用先获取长度。。
    # 直接迭代
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = 2 * res + head.val
            head = head.next
        return res

    # 先获取长度，然后迭代
    # def getDecimalValue(self, head: ListNode) -> int:
    #     cur = head
    #     digit = -1
    #     while cur:
    #         digit += 1
    #         cur = cur.next
    #     res = 0
    #     while head:
    #         res += 2 ** digit * head.val
    #         head = head.next
    #         digit -= 1
    #     return res
    # 递归
    # def getDecimalValue(self, head: ListNode) -> int:
    #     if not head:
    #         return 0
    #
    #     def dfs(h: ListNode) -> (int, int):
    #         if not h.next:
    #             return 0, h.val
    #         level, val = dfs(h.next)
    #         return level + 1, 2 ** (level + 1) * h.val + val
    #
    #     return dfs(head)[-1]


assert Solution().getDecimalValue(toLinkedList([1, 0, 1])) == 5
assert Solution().getDecimalValue(toLinkedList([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) == 18880
