# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    # 先遍历获取长度
    # 长链表先走长度差
    # def getIntersectionNode(self, headA, headB):
    #     if not (headA and headB):
    #         return None
    #
    #     def list_size(head):
    #         size = 0
    #         while head:
    #             size += 1
    #             head = head.next
    #         return size
    #
    #     size1, size2 = list_size(headA), list_size(headB)
    #     ptr1, ptr2 = headA, headB
    #     if size1 > size2:
    #         for i in range(size1 - size2):
    #             ptr1 = ptr1.next
    #     elif size2 > size1:
    #         for i in range(size2 - size1):
    #             ptr2 = ptr2.next
    #     while ptr1 and ptr2:
    #         if ptr1 == ptr2:
    #             return ptr1
    #         ptr1 = ptr1.next
    #         ptr2 = ptr2.next
    #     return None

    def getIntersectionNode(self, headA, headB):
        if not headA and not headB:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
