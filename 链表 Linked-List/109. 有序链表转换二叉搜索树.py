# Definition for singly-linked list.
from util.List import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # fast, slow寻找中点
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, head
        # slow最终左中位节点的前一个
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_node = slow.next
        slow.next = None
        root = TreeNode(mid_node.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid_node.next)
        return root

    # 转化成数组处理
    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    #     A = []
    #     while head:
    #         A.append(head.val)
    #         head = head.next
    #
    #     def list_to_BST(A, lt, rt) -> TreeNode:
    #         if lt < rt:
    #             # mid = (rt - lt) // 2 你是憨憨吗？
    #             mid = (rt + lt) // 2  # 计算左中位数
    #             root = TreeNode(A[mid])
    #             root.left = list_to_BST(A, lt, mid)
    #             root.right = list_to_BST(A, mid + 1, rt)
    #             return root
    #
    #     return list_to_BST(A, 0, len(A))


lst = toLinkedList([-10, -3, 0, 5, 9])
root = Solution().sortedListToBST(lst)
a = 1
