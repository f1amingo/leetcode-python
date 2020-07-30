import math


class Solution:

    # 数学：
    # 1.若拆分的数量 a 确定，则各拆分数字相等时，乘积最大。
    # 2.将数字 n 尽可能以因子 3 等分时，乘积最大。
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

    # 动态规划
    # def integerBreak(self, n: int) -> int:
    #     if n == 2:
    #         return 1
    #     if n == 3:
    #         return 2
    #     dp = [0] * (n + 1)
    #     dp[2], dp[3] = 2, 3
    #     for i in range(3, n + 1):
    #         for j in range(2, i // 2 + 1):
    #             dp[i] = max(dp[i], dp[i - j] * dp[j])
    #     return dp[-1]


print(Solution().integerBreak(10))
