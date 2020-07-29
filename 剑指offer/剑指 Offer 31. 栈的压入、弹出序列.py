from typing import List


class Solution:

    # Krahets的写法，非常凝练
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk, i = [], 0
        for num in pushed:
            stk.append(num)
            while stk and stk[-1] == popped[i]:
                stk.pop()
                i += 1
        return not stk

    # my solution 辅助栈是必要的
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    #     n = len(pushed)
    #     right = 0
    #     stk = []
    #     for left in range(n):
    #         stk.append(pushed[left])
    #         while stk and stk[-1] == popped[right]:
    #             stk.pop()
    #             right += 1
    #     return len(stk) == 0


print(Solution().validateStackSequences([1, 2], [2, 1]))
