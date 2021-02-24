# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.List import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 头结点可能改变
        dummy = ListNode(-1)
        dummy.next = head
        pre, ptr = dummy, head
        while ptr and ptr.next:
            # 相等
            if ptr.val == ptr.next.val:
                while ptr.next and ptr.val == ptr.next.val:
                    ptr = ptr.next
                # 删除重复部分
                pre.next = ptr.next
            else:
                # 不等，该节点可以保留
                pre = pre.next
            ptr = ptr.next
        return dummy.next
