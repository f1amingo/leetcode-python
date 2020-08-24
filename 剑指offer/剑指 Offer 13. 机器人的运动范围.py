class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k == 0:
            return 1

        def digit_sum(num):
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s

        dp = [[False] * n for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if digit_sum(i) + digit_sum(j) <= k:
                    # 边界
                    if i == 0 and j == 0:
                        dp[i][j] = True
                        res += 1
                    # 不能通过数位和大于k的点
                    elif (i == 0 and dp[i][j - 1]) or (j == 0 and dp[i - 1][j]) or dp[i - 1][j] or dp[i][j - 1]:
                        res += 1
                        dp[i][j] = True
        return res


print(Solution().movingCount(16, 8, 4))
