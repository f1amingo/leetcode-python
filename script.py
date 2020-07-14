from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        dp = [0] * n
        res = 0
        for i in range(2, n):
            if A[i] + A[i - 2] == 2 * A[i - 1]:
                dp[i] = dp[i - 1] + 1
                res += dp[i]
        return res


print(Solution().numberOfArithmeticSlices([1, 2, 3, 6, 9]))
