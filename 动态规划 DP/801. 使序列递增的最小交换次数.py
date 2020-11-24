from typing import List


class Solution:
    # 错误解法
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        if n <= 1:
            return 0
        dp = [0] * n
        for i in range(1, n):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                dp[i] = dp[i - 1]
            else:
                A[i], B[i] = B[i], A[i]
                dp[i] = dp[i - 1] + 1
        return dp[-1]


assert Solution().minSwap([0, 4, 4, 5, 9], [0, 1, 6, 8, 10]) == 1
assert Solution().minSwap([1, 3, 5, 4], [1, 2, 3, 7]) == 1
assert Solution().minSwap([3, 3, 8, 9, 10], [1, 7, 4, 6, 8]) == 1
