# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # my solution
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    #     if not (head and head.next):
    #         return head
    #
    #     self.n = 0
    #     self.tail = None
    #
    #     def reverse(_head: ListNode, i: int):
    #         self.n = i + 1
    #         if not _head.next:
    #             self.tail = _head
    #             return _head
    #         re_node = reverse(_head.next, i + 1)
    #         if self.n - i <= self.n % k:
    #             return _head
    #         if (i + 1) % k == 0:
    #             _head.next = re_node
    #             self.tail = _head
    #             return _head
    #         else:
    #             _head.next = self.tail.next
    #             self.tail.next = _head
    #             self.tail = _head
    #             return re_node
    #
    #     return reverse(head, 0)

    # 官方题解
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(_head: ListNode, _tail: ListNode):
            # 这里与后面的部分拼接起来了
            _pre = _tail.next
            _cur = _head
            while _pre != tail:
                _nex = _cur.next
                _cur.next = _pre
                _pre = _cur
                _cur = _nex
            return _tail, _head

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            head, tail = reverse(pre.next, tail)
            # 接新头
            pre.next = head
            # 新一轮
            pre = tail

        return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
node = Solution().reverseKGroup(n1, 2)

while node:
    print(node.val)
    node = node.next
