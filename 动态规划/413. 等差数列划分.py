from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # # 该方法较慢，大量冗余计算，O(n^2)
        # n = len(A)
        # if n < 3:
        #     return 0
        # # dp[i][j]：子数组[i, j]是否是等差数列
        # dp = [[False] * n for _ in range(n)]
        # res = 0
        # for i in range(n - 2):
        #     for j in range(i + 2, n):
        #         if j - i == 2:
        #             dp[i][j] = A[j] - A[j - 1] == A[j - 1] - A[j - 2]
        #         else:
        #             dp[i][j] = A[j] - A[j - 1] == A[j - 1] - A[j - 2] and dp[i][j - 1]
        #         if dp[i][j]:
        #             res += 1
        # return res

        # dp[i]表示以A[i]结尾的子数组中等差数列的数目
        n = len(A)
        if n < 3:
            return 0
        dp = [0] * n
        res = 0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
                res += dp[i]
        return res


print(Solution().numberOfArithmeticSlices([1, 2, 3, 6, 9]))
# print(Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5]))
