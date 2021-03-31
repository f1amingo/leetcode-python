import math


class Solution:
    # 贪心枚举
    def numSquares(self, n: int) -> int:
        def can_decompose(n, count):
            if count == 1:
                return n in square_nums
            for k in square_nums:
                if can_decompose(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])
        for count in range(1, n + 1):
            if can_decompose(n, count):
                return count

    # 时间：O(n * sqrt(n))
    # def numSquares(self, n: int) -> int:
    #     C = int(math.sqrt(n))
    #     dp = [0] + [float('inf')] * n
    #     for i in range(1, C + 1):
    #         v = i * i
    #         for j in range(v, n + 1):
    #             dp[j] = min(dp[j], dp[j - v] + 1)
    #     return dp[-1]


assert Solution().numSquares(12) == 3
assert Solution().numSquares(13) == 2
