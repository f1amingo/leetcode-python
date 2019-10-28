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
        # 快慢指针
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False

        # 使用map
        lookup = {}
        while head:
            if head in lookup:
                return True
            lookup[head] = 0
            head = head.next
        return False


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(Solution().hasCycle(node1))
