# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        dummy = ListNode(-1)
        p3 = dummy
        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

n1 = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(4)

node1.next = node2
node2.next = node3

n1.next = n2
n2.next = n3

res = Solution().mergeTwoLists(None, None)

a = 1
