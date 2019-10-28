# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 转换为数组比较
        # if not head:
        #     return True
        # _list = []
        # while head:
        #     _list.append(head.val)
        #     head = head.next
        # p1 = 0
        # p2 = len(_list) - 1
        # while p1 < p2:
        #     if _list[p1] != _list[p2]:
        #         return False
        #     p1 += 1
        #     p2 -= 1
        # return True

        # 转换为数组 极简代码
        _list = []
        while head:
            _list.append(head.val)
            head = head.next
        return _list == _list[::-1]


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4

print(Solution().isPalindrome(node1))
