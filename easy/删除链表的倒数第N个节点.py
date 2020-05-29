# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        ptr1 = dummy
        ptr2 = head
        for i in range(n):
            ptr2 = ptr2.next
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr1.next.next
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

Solution().removeNthFromEnd(node1, 5)

a = 1
