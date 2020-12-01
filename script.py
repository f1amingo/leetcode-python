from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[max(i - coin, 0)] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]


assert Solution().coinChange([1, 2, 5], 11) == 3
assert Solution().coinChange([2], 3) == -1
assert Solution().coinChange([1], 0) == 0
assert Solution().coinChange([1], 1) == 1
assert Solution().coinChange([1], 2) == 2
