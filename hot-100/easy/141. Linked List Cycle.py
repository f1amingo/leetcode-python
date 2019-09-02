# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        ptr1 = ptr2 = head
        while ptr1 and ptr2:
            ptr1 = ptr1.next
            if not ptr2.next:
                break
            ptr2 = ptr2.next.next
            if ptr1 == ptr2:
                return True
        return False


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(Solution().hasCycle(node1))
