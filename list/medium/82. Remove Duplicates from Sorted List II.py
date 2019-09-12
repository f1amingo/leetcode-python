# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                while ptr.next and ptr.val == ptr.next.val:
                    ptr = ptr.next
                pre.next = ptr.next
            else:
                pre = ptr
            ptr = ptr.next
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

Solution().deleteDuplicates(node1)

a = 1
