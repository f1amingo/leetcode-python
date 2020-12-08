# Definition for singly-linked list.
from util.List import *


class Solution:

    # 链表归并非递归空间只有O(1)
    def sortList(self, head: ListNode) -> ListNode:
        def cut(_head: ListNode) -> ListNode:
            if not _head:
                return None
            dummy = ListNode(-1)
            dummy.next = head
            slow, fast = dummy, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            tmp = slow.next
            slow.next = None
            return tmp

        def merge(h1, h2) -> ListNode:
            ptr = dummy = ListNode(-1)
            while h1 and h2:
                if h1.val <= h2.val:
                    ptr.next = h1
                    h1 = h1.next
                else:
                    ptr.next = h2
                    h2 = h2.next
                ptr = ptr.next
            ptr.next = h1 if h1 else h2
            return dummy.next

        if not head or not head.next:
            return head
        mid = cut(head)
        return merge(self.sortList(head), self.sortList(mid))

    # 快排超时
    # def sortList(self, head: ListNode) -> ListNode:
    #     A = []
    #     ptr = head
    #     while ptr:
    #         A.append(ptr)
    #         ptr = ptr.next
    #
    #     def partition(_A, _low, _high):
    #         pivot = _A[_high].val
    #         i = _low - 1
    #         for j in range(_low, _high):
    #             if A[j].val <= pivot:
    #                 i += 1
    #                 A[i], A[j] = A[j], A[i]
    #         A[i + 1], A[_high] = A[_high], A[i + 1]
    #         return i + 1
    #
    #     def quick_sort(_A, _low, _high):
    #         if _low < _high:
    #             p = partition(_A, _low, _high)
    #             quick_sort(_A, _low, p - 1)
    #             quick_sort(_A, p + 1, _high)
    #
    #     quick_sort(A, 0, len(A) - 1)
    #
    #     new_ptr = dummy = ListNode(-1)
    #     for node in A:
    #         new_ptr.next = node
    #         new_ptr = new_ptr.next
    #     new_ptr.next = None  # ！！收尾，否则会产生循环
    #     return dummy.next


head = toLinkedList([4, 2, 1, 3])
new_head = Solution().sortList(head)
printLinkedList(new_head)
