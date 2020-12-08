# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        next_node = head.next
        next_next = next_node.next
        next_node.next = head
        head.next = self.swapPairs(next_next)
        return next_node


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4

res = Solution().swapPairs(node1)
a = 1
