# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.ZList import ListNode


class Solution:
    # 加入pre，意味着节点会被保留
    # 通过判断等不等于下一个节点，采取不同的处理方式
    # 1.相等，需要全部移除，不加入pre，pre=ptr.next
    # 2.不等，需要保留，将ptr加入pre
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
                # 此时pre.next就是ptr，pre和ptr是连续的
                pre = pre.next
            ptr = ptr.next
        return dummy.next
