# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 直接方法
# 108 ms	11.9 MB
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         str_num1 = ''
#         str_num2 = ''
#         ptr = l1
#         while ptr is not None:
#             str_num1 = str(ptr.val) + str_num1
#             ptr = ptr.next
#         ptr = l2
#         while ptr is not None:
#             str_num2 = str(ptr.val) + str_num2
#             ptr = ptr.next
#         int_sum = int(str_num1) + int(str_num2)
#         str_sum_reverse = str(int_sum)[::-1]
#         head_ptr = None
#         last_ptr = None
#         for i in str_sum_reverse:
#             if head_ptr is None:
#                 head_ptr = ListNode(i)
#                 last_ptr = head_ptr
#             else:
#                 last_ptr.next = ListNode(i)
#                 last_ptr = last_ptr.next
#         return head_ptr


# 直接从头加到尾
# 44 ms	11.7 MB
# 多运用/ %
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        carry = 0
        head_ptr = None
        tail_ptr = None
        while ptr1 or ptr2:
            val1 = 0
            if ptr1:
                val1 = ptr1.val
            val2 = 0
            if ptr2:
                val2 = ptr2.val
            this_sum = val1 + val2 + carry
            carry = this_sum / 10
            if head_ptr:
                tail_ptr.next = ListNode(this_sum % 10)
                tail_ptr = tail_ptr.next
            else:
                head_ptr = ListNode(this_sum % 10)
                tail_ptr = head_ptr
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        if carry:
            tail_ptr.next = ListNode(1)
        return head_ptr


def buildNodeList(arr):
    head_ptr = None
    last_ptr = None
    for i in arr:
        if head_ptr is None:
            head_ptr = ListNode(i)
            last_ptr = head_ptr
        else:
            last_ptr.next = ListNode(i)
            last_ptr = last_ptr.next
    return head_ptr


def printNodeList(node):
    ptr = node
    while ptr is not None:
        print(ptr.val)
        ptr = ptr.next


if __name__ == "__main__":
    solution = Solution()
    node1 = buildNodeList([3, 2, 1])
    node2 = buildNodeList([4])
    res_node = solution.addTwoNumbers(node1, node2)
    printNodeList(res_node)
