class Solution:
    # 丑数 = 某较小的丑数 * 系数 (2, 3, 5)
    # 对于各个系数而言，它们对应的丑数一定是递增的
    def nthUglyNumber(self, n: int) -> int:
        a = b = c = 0
        dp = [1] * n
        for i in range(1, n):
            n2, n3, n5 = 2 * dp[a], 3 * dp[b], 5 * dp[c]
            dp[i] = min(n2, n3, n5)
            # 三个平行的if，因为可能相等
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]


assert Solution().nthUglyNumber(10) == 12
assert Solution().nthUglyNumber(1) == 1
