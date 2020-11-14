from typing import List


class Solution:
    # 滑动窗口
    # 明显的区间求和问题
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if not cardPoints or k == 0:
            return 0
        n = len(cardPoints)
        total = sum(cardPoints)
        if k >= n:  # 全选
            return total
        # 初始化
        left, right = 0, n - k - 1
        minWindow = windowSum = sum(cardPoints[left:right + 1])
        for right in range(n - k, n):
            windowSum -= cardPoints[left]
            windowSum += cardPoints[right]
            minWindow = min(minWindow, windowSum)
            left += 1  # left, right同时移动
        return total - minWindow

    # 动态规划，超时
    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     if not cardPoints or k == 0:
    #         return 0
    #     n = len(cardPoints)
    #     # 全选
    #     if k >= n:
    #         return sum(cardPoints)
    #     dp = [[0] * n for _ in range(n)]
    #     for thisK in range(k):
    #         for i in range(n):
    #             for j in range(n - 1, i, -1):
    #                 dp[i][j] = max(cardPoints[i] + dp[i + 1][j], cardPoints[j] + dp[i][j - 1])
    #     return dp[0][-1]

    # 记忆化递归，超时
    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     if not cardPoints or k == 0:
    #         return 0
    #     n = len(cardPoints)
    #     # 全选
    #     if k >= n:
    #         return sum(cardPoints)
    #     memo = [[[-1] * n for _ in range(n)] for _ in range(k + 1)]
    #
    #     # [i,j]区间内选thisK次，可获得的最大点数
    #     def dfs(i: int, j: int, thisK: int):
    #         if thisK == 0:
    #             return 0
    #         if i == j:
    #             return cardPoints[i]
    #         if memo[k][i][j] == -1:
    #             pickI = cardPoints[i] + dfs(i + 1, j, thisK - 1)
    #             pickJ = cardPoints[j] + dfs(i, j - 1, thisK - 1)
    #             memo[k][i][j] = max(pickI, pickJ)
    #         return memo[k][i][j]
    #
    #     return dfs(0, n - 1, k)

    # 递归，超时
    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     if not cardPoints or k == 0:
    #         return 0
    #
    #     # [i,j]区间内选thisK次，可获得的最大点数
    #     def dfs(i: int, j: int, thisK: int):
    #         if thisK == 0:
    #             return 0
    #         if i == j:
    #             return cardPoints[i]
    #         pickI = cardPoints[i] + dfs(i + 1, j, thisK - 1)
    #         pickJ = cardPoints[j] + dfs(i, j - 1, thisK - 1)
    #         return max(pickI, pickJ)
    #
    #     return dfs(0, len(cardPoints) - 1, k)


assert Solution().maxScore([100, 40, 17, 9, 73, 75], 3) == 248
assert Solution().maxScore([2, 2, 2], 2) == 4
print(Solution().maxScore(
    [30, 88, 33, 37, 18, 77, 54, 73, 31, 88, 93, 25, 18, 31, 71, 8, 97, 20, 98, 16, 65, 40, 18, 25, 13, 51, 59], 26))
assert Solution().maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
assert Solution().maxScore([1, 1000, 1], 1) == 1
assert Solution().maxScore([1, 79, 80, 1, 1, 1, 200, 1], 3) == 202
assert Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
