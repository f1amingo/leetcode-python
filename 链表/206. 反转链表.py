# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 递归
    # def reverseList(self, head: ListNode) -> ListNode:
    #     pre = None
    #     cur = head
    #     while cur:
    #         tmp = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = tmp
    #     return pre

    # 迭代
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        re_node = self.reverseList(head.next)
        # 这里不可以写re_node.next = head
        # 注意re_node是原链表的尾结点，新链表的头结点
        head.next.next = head
        head.next = None
        return re_node


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node = Solution().reverseList(node1)

while node:
    print(node.val)
    node = node.next
