# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        n, ptr = 0, head
        while ptr:
            n += 1
            ptr = ptr.next
        mod_k = k % n  # k可能大于数组长度
        if mod_k == 0:
            return head
        A = B = head
        for i in range(mod_k):
            if not B:
                return None
            B = B.next
        while B and B.next:
            A = A.next
            B = B.next
        new_head, B.next, A.next = A.next, head, None
        return new_head


node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
# node3.next = node4
# node4.next = node5
node = Solution().rotateRight(node1, 4)

a = 1
