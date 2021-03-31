from collections import Counter
from typing import List


class Solution:
    # 01背包，二维代价
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            counter = Counter(s)
            zero, one = counter.get('0', 0), counter.get('1', 0)
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        return dp[-1][-1]

    # 动态规划
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     if not strs:
    #         return 0
    #     N = len(strs)
    #     cost = [[0] * 2 for _ in range(N)]
    #     dp = [[0] * (n + 1) for _ in range(m + 1)]
    #     for i in range(N):
    #         for c in strs[i]:
    #             cost[i][ord(c) - ord('0')] += 1
    #     for i in range(N):
    #         for j in range(m, cost[i][0] - 1, -1):
    #             for k in range(n, cost[i][1] - 1, -1):
    #                 dp[j][k] = max(dp[j][k], 1 + dp[j - cost[i][0]][k - cost[i][1]])
    #     return dp[-1][-1]

    # 递归 超时
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     if not strs:
    #         return 0
    #     max_len = 0
    #     total = len(strs)
    #     zero_count = [0] * total
    #     one_count = [0] * total
    #     for i in range(total):
    #         for c in strs[i]:
    #             if c == '0':
    #                 zero_count[i] += 1
    #             else:
    #                 one_count[i] += 1
    #
    #     def dfs(start: int, cur_list: List, this_m: int, this_n: int):
    #         if this_m < 0 or this_n < 0:
    #             return
    #         nonlocal max_len
    #         max_len = max(max_len, len(cur_list))
    #         for i in range(start, total):
    #             cur_list.append(strs[i])
    #             dfs(i + 1, cur_list, this_m - zero_count[i], this_n - one_count[i])
    #             cur_list.pop()
    #
    #     dfs(0, [], m, n)
    #     return max_len


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
print(Solution().findMaxForm(["10", "0", "1"], 1, 1))
