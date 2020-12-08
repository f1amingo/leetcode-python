# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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


# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         dummy = tail_ptr = ListNode(-1)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail_ptr.next = l1
#                 l1 = l1.next
#             else:
#                 tail_ptr.next = l2
#                 l2 = l2.next
#             tail_ptr = tail_ptr.next
#         if l1:
#             tail_ptr.next = l1
#         if l2:
#             tail_ptr.next = l2
#         return dummy.next

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


list1 = buildNodeList([1, 2, 4])
list2 = buildNodeList([1, 3, 4])
res = Solution().mergeTwoLists(list1, list2)
printNodeList(res)
