# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util.List import *


# 典型的双指针问题，快慢指针
# 最后一个节点是倒数第1
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        # 需不需要dummy？链表头并不会改变
        # fast先走走几步？
        # 考虑只有一个节点，fast初始化为head，走一步成None；
        # fast必须往前挪一挪，slow和fast不可以指向同一个节点
        # 由题意，k最小为1，所以range(k)，而不是range(k-1)
        for _ in range(k):
            fast = fast.next  # 这里假设k是有意义的
        while fast:
            slow = slow.next
            fast = fast.next
        return slow


a = toLinkedList([1, 2, 3, 4, 5])
print(Solution().getKthFromEnd(a, 2).val)
