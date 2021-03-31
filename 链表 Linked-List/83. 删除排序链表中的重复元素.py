# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.List import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr = head
        # 相邻两两比较
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        # head不会改变
        return head
