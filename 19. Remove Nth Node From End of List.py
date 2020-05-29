# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 两次遍历算法
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         if not head:
#             return head
#         dummy = ListNode(-1)
#         dummy.next = head
#         length = 0
#         while head:
#             length += 1
#             head = head.next
#         left_seq = length - n
#         ptr = dummy
#         for i in range(0, left_seq):
#             ptr = ptr.next
#         next_node = ptr.next
#         if next_node:
#             ptr.next = next_node.next
#         return dummy.next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        ptr1 = ptr2 = dummy
        for i in range(0, n):
            ptr2 = ptr2.next
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        next_node = ptr1.next
        if next_node:
            ptr1.next = next_node.next
        return dummy.next


def buildNodeList(arr):
    head_ptr = None
    last_ptr = None
    for i in arr:
        if head_ptr is None:
            head_ptr = ListNode(i)
            last_ptr = head_ptr
        else:
            last_ptr.next = ListNode(i)
            last_ptr = last_ptr.next
    return head_ptr


def printNodeList(node):
    ptr = node
    while ptr is not None:
        print(ptr.val)
        ptr = ptr.next


arr = buildNodeList([1])
res = Solution().removeNthFromEnd(arr, 1)
printNodeList(res)
