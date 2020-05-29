from typing import List


class Solution:
    # my solution
    # def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    #     n = len(days) + 1
    #     dp = [0] * n
    #     for i in range(1, n):
    #         cost0 = dp[i - 1] + costs[0]
    #         day_idx_i = i - 1
    #         day_idx_j = day_idx_i - 1
    #         while day_idx_j >= 0 and days[day_idx_i] - days[day_idx_j] < 7:
    #             day_idx_j -= 1
    #         cost1 = dp[day_idx_j + 1] + costs[1]
    #         day_idx_j = day_idx_i - 1
    #         while day_idx_j >= 0 and days[day_idx_i] - days[day_idx_j] < 30:
    #             day_idx_j -= 1
    #         cost2 = dp[day_idx_j + 1] + costs[2]
    #         dp[i] = min(cost0, cost1, cost2)
    #     return dp[-1]

    # def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    #     if not days:
    #         return 0
    #     dp = [0] * (days[-1] + 1)
    #     for i in range(1, len(dp)):
    #         if i in days:
    #             cost0 = dp[i - 1] + costs[0]
    #             cost1 = costs[1] if i < 7 else costs[1] + dp[i - 7]
    #             cost2 = costs[2] if i < 30 else costs[2] + dp[i - 30]
    #             dp[i] = min(cost0, cost1, cost2)
    #         else:
    #             dp[i] = dp[i - 1]
    #     return dp[-1]

    # 熊猫刷题
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        days_idx = 0
        for i in range(1, len(dp)):
            if i == days[days_idx]:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


assert Solution().mincostTickets([1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 16, 17, 19, 21, 24, 26, 27, 28, 29],
                                 [3, 14, 50]) == 50
assert Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
assert Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17
