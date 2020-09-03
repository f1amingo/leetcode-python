# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 头插法
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m >= n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        guard = dummy  # guard就是头
        for i in range(m - 1):
            guard = guard.next
        # soldier初始化为需要倒序的第一个node
        soldier = guard.next
        for i in range(m, n):
            # soldier会把自己的next干掉
            to_kill = soldier.next
            soldier.next = to_kill.next
            to_kill.next = guard.next
            # soldier干掉next的方式，就是把它的人头挂到guard后面
            guard.next = to_kill
        return dummy.next

    # 使用stack倒序
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    #     if m >= n:
    #         return head
    #     dummy = ListNode(-1)
    #     dummy.next = head
    #     ptr1 = dummy
    #     for i in range(m - 1):
    #         ptr1 = ptr1.next
    #     ptr2 = ptr1.next
    #     stk = []
    #     for i in range(m, n + 1):
    #         stk.append(ptr2)
    #         ptr2 = ptr2.next
    #     while stk:
    #         ptr1.next = stk.pop()
    #         ptr1 = ptr1.next
    #     ptr1.next = ptr2
    #     return dummy.next
