# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

from util.List import *


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        origin_len = 0
        ptr = root
        while ptr:
            origin_len += 1
            ptr = ptr.next
        base_count = origin_len // k
        addition = origin_len % k
        res = []
        for i in range(k):
            this_count = base_count + 1 if i < addition else base_count
            if this_count == 0:
                res.append(None)
            else:
                ptr = root
                for j in range(1, this_count):
                    ptr = ptr.next
                res.append(root)
                root = ptr.next
                ptr.next = None  # 断开链表
        return res


root = toLinkedList([1, 2, 3, 4])
k = 5
res = Solution().splitListToParts(root, k)
for lst in res:
    printLinkedList(lst)
