# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 使用堆
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     heap = []
    #     heapq.heapify(heap)
    #     dummy = ListNode(-1)
    #     last = dummy
    #     for i in range(len(lists)):
    #         node = lists[i]
    #         if node:
    #             heapq.heappush(heap, (node.val, i))
    #     while heap:
    #         smallest = heapq.heappop(heap)
    #         cur_node = lists[smallest[1]]
    #         last.next = cur_node
    #         last = cur_node
    #         if cur_node.next:
    #             heapq.heappush(heap, (cur_node.next.val, smallest[1]))
    #             lists[smallest[1]] = cur_node.next
    #     return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(a: ListNode, b: ListNode):
            last = dummy = ListNode(-1)
            ptr1, ptr2 = a, b
            while ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    last.next = ptr1
                    ptr1 = ptr1.next
                else:
                    last.next = ptr2
                    ptr2 = ptr2.next
                last = last.next
            last.next = ptr1 if ptr1 else ptr2
            return dummy.next

        def partition(low, high):
            if low < high:
                mid = (low + high) >> 1
                return mergeTwoLists(partition(low, mid), partition(mid + 1, high))
            return lists[low]

        if not lists:
            return None
        return partition(0, len(lists) - 1)


node11 = ListNode(1)
node12 = ListNode(4)
node13 = ListNode(5)
node11.next = node12
node12.next = node13

node21 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)
node21.next = node22
node22.next = node23

node31 = ListNode(2)
node32 = ListNode(6)
node31.next = node32

res = Solution().mergeKLists([node11, node21, node31])
while res:
    print(res.val)
    res = res.next
