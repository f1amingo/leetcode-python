from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [-1] * n
        dp[0] = 0
        for i in range(1, n):
            count = -1
            for coin in coins:
                pre_idx = i - coin
                if coin == i:
                    count = 1
                    break
                elif pre_idx > -1 and dp[pre_idx] != -1:
                    if count == -1 or dp[pre_idx] + 1 < count:
                        count = dp[pre_idx] + 1
            dp[i] = count
        return dp[-1]


coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))
