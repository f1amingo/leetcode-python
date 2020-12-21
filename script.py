# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import *


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 寻找中点
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 断开链表
        head1 = slow.next
        slow.next = None
        # 分别排序
        ptr1 = self.sortList(head)
        ptr2 = self.sortList(head1)
        ptr = dummy = ListNode(-1)
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next
        if ptr1:
            ptr.next = ptr1
        if ptr2:
            ptr.next = ptr2
        return dummy.next


printLinkedList(Solution().sortList(toLinkedList([3, 2, 1])))
printLinkedList(Solution().sortList(toLinkedList([4, 3])))
printLinkedList(Solution().sortList(toLinkedList([4, 2, 1, 3])))
