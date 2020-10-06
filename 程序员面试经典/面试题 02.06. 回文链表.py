# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from util.List import *


# 1.转为数组，判断数组是否回文，但是完全没有利用链表的性质；
# 2.快慢指针找中点，中点以前的值入栈，过中点后一边出栈，一边和右半结点比；
# 3.找中点，翻转任一一侧，变成两个半长链表，逐位比较；
class Solution:
    # 方法三 别人的方法
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next  # fast先走，否则slow就翻转了
            slow.next, slow, prev = prev, slow.next, slow
        if fast:  # odd
            slow = slow.next
        while prev and prev.val == slow.val:
            prev, slow = prev.next, slow.next
        # 最后这里避免了输入为空的判断
        return prev is None

    # 方法2
    # def isPalindrome(self, head: ListNode) -> bool:
    #     # 节点为空，或者只有一个节点
    #     if not head or not head.next:
    #         return True
    #     stk = []
    #     slow = fast = head
    #     isOdd = False
    #     # slow最终位置：
    #     # 1.长度奇数时，slow落在中间节点的下一个；
    #     # 2.长度偶数时，slow落在右半链表头；
    #     # 所以有一个问题，长度奇数时会把中间节点入栈，后面比较却不用它参与
    #     while fast:
    #         stk.append(slow.val)
    #         slow = slow.next
    #         fast = fast.next
    #         # 画图可以发现，fast移动规律，单次循环结束，落在奇数节点
    #         if not fast:
    #             isOdd = True
    #             break
    #         fast = fast.next
    #     if isOdd:
    #         stk.pop()
    #     while slow:
    #         if slow.val != stk.pop():
    #             return False
    #         slow = slow.next
    #     return True


assert Solution().isPalindrome(toLinkedList([1, 0, 1]))
assert Solution().isPalindrome(toLinkedList([1]))
assert Solution().isPalindrome(toLinkedList([1, 2, 2, 1]))
assert Solution().isPalindrome(toLinkedList([1, 1]))
assert not Solution().isPalindrome(toLinkedList([1, 2]))
