# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

from util.List import *


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stk = []
        res = []
        idx = -1
        while head:
            res.append(0)
            idx += 1
            while stk and head.val > stk[-1][1]:
                res[stk[-1][0]] = head.val
                stk.pop()
            stk.append((idx, head.val))
            head = head.next
        return res


assert Solution().nextLargerNodes(toLinkedList([2, 7, 4, 3, 5])) == [7, 0, 5, 5, 0]
assert Solution().nextLargerNodes(toLinkedList([2, 1, 5])) == [5, 5, 0]
