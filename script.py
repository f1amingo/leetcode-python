# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.ZList import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 头结点可能改变，使用dummy简化问题
        dummy = ListNode(-1)
        dummy.next = head
        pre, ptr = dummy, head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                while ptr.next and ptr.val == ptr.next.val:
                    ptr = ptr.next
                ptr = ptr.next
                pre.next = ptr
            else:
                pre = ptr
                ptr = ptr.next
        return dummy.next
