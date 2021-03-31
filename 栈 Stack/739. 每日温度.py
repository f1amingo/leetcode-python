from typing import List


class Solution:
    # 单调栈
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans = [0] * n
        stk = []
        for i in range(n):
            while stk and T[i] > T[stk[-1]]:
                top_i = stk.pop()
                ans[top_i] = i - top_i
            stk.append(i)
        return ans


assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
