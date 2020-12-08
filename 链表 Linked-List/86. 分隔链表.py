# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import *


class Solution:

    # 官方题解，先放到before、after两个链表中，再将before、after连接
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_head, after_head = ListNode(-1), ListNode(-1)
        before, after = before_head, after_head
        ptr = head
        while ptr:
            if ptr.val < x:
                before.next = ptr
                before = ptr
            else:
                after.next = ptr
                after = ptr
            ptr = ptr.next
        before.next = after_head.next
        after.next = None
        return before_head.next

    # 在原链表上删除、插入
    # def partition(self, head: ListNode, x: int) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #     guard = dummy = ListNode(-1)
    #     dummy.next = head
    #     # guard：第一个大于等于x的结点的前一个结点
    #     while guard:
    #         if guard.next and guard.next.val >= x:
    #             break
    #         guard = guard.next
    #     # 都小于x，提前退出
    #     if not guard:
    #         return head
    #     soldier = guard
    #     while soldier.next:
    #         # 找到小于x的节点，从原位置删除，插入到guard之前
    #         if soldier.next.val < x:
    #             tmp = soldier.next
    #             soldier.next = tmp.next
    #             guard_next = guard.next
    #             guard.next = tmp
    #             tmp.next = guard_next
    #             guard = guard.next
    #         else:
    #             soldier = soldier.next
    #     return dummy.next


head = toLinkedList([3, 2])
res = Solution().partition(head, 3)
printLinkedList(res)
