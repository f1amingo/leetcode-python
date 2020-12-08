# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 递归解法
    # def deleteDuplicates(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head or not head.next:
    #         return head
    #     if head.val == head.next.val:
    #         return self.deleteDuplicates(head.next)
    #     else:
    #         head.next = self.deleteDuplicates(head.next)
    #     return head
    def deleteDuplicates(self, head):
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node1.next = node2
node2.next = node3

Solution().deleteDuplicates(node1)
a = 1
