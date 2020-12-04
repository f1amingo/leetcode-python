from collections import Counter
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            counter = Counter(s)
            zero, one = counter.get('0', 0), counter.get('1', 0)
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        return dp[-1][-1]


assert Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4
