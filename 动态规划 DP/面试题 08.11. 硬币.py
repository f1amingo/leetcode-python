class Solution:
    def waysToChange(self, n: int) -> int:
        M = 1000000007
        # 优雅的写法
        dp = [1] + [0] * n
        coins = [1, 5, 10, 25]
        # 可选的硬币种类不断增加
        # 避免重复选择
        # 因为内循环中，每次只能选择当前面额的coin
        for coin in coins:
            for j in range(coin, n + 1):
                dp[j] += dp[j - coin]
        return dp[-1] % M


print(Solution().waysToChange(10))
print(Solution().waysToChange(5))
