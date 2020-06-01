# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        def merge(low, high):
            list1, list2 = lists[low], lists[high]
            dummy = ListNode(-1)
            ptr1, ptr2, ptr3 = list1, list2, dummy
            while ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    ptr3.next = ptr1
                    ptr1 = ptr1.next
                else:
                    ptr3.next = ptr2
                    ptr2 = ptr2.next
                ptr3 = ptr3.next
            ptr3.next = ptr1 if ptr1 else ptr2
            lists[low] = dummy.next

        def partition(low, high):
            if low < high:
                mid = (low + high) // 2
                partition(low, mid)
                partition(mid + 1, high)
                merge(low, mid + 1)

        partition(0, len(lists) - 1)

        return lists[0]


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a1.next = a2
a2.next = a3
b1 = ListNode(4)
b2 = ListNode(5)
b3 = ListNode(6)
b4 = ListNode(7)
b1.next = b2
b2.next = b3
b3.next = b4

node = Solution().mergeKLists([a1, b1])
pri = []
while node:
    pri.append(node.val)
    node = node.next
print(pri)
