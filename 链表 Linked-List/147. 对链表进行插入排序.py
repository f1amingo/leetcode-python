# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import *


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        head = head.next
        dummy.next.next = None
        while head:
            pre, cnt = dummy, dummy.next
            while cnt:
                if cnt.val > head.val:
                    break
                # 注意指针移动
                pre, cnt = cnt, cnt.next
            next_to_sort = head.next
            head.next = pre.next
            pre.next = head
            head = next_to_sort
        return dummy.next


h = toLinkedList([4, 2, 1, 3])
h = Solution().insertionSortList(h)
printLinkedList(h)
