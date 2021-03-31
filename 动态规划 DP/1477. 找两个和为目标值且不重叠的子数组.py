from typing import List


class Solution:
    # dp[i]，[0,i]中符合要求的子数组最小长度
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left, window, res = 0, 0, n + 1
        dp = [n + 1] * n
        for i, num in enumerate(arr):
            window += num
            while window > target:
                window -= arr[left]
                left += 1
            if window == target:
                window_len = i - left + 1
                res = min(res, window_len + dp[left - 1])
                dp[i] = min(window_len, dp[i - 1])
            else:
                dp[i] = dp[i - 1]
        return res if res <= n else -1

    # 错误方法
    # def minSumOfLengths(self, arr: List[int], target: int) -> int:
    #     n = len(arr)
    #     dp = [0] * n
    #     lt = rt = 0
    #     thisWin = 0
    #     while rt < n:
    #         thisWin += arr[rt]
    #         if thisWin == target:
    #             dp[rt] = rt - lt + 1
    #             lt += 1
    #             rt = lt
    #             thisWin = 0
    #         elif thisWin > target:
    #             lt += 1
    #             rt = lt
    #             thisWin = 0
    #         else:
    #             rt += 1
    #
    #     res = float('inf')
    #     minL = None
    #     idx = 0
    #     for i in range(n):
    #         if dp[i] == 0:
    #             continue
    #         if minL is None:
    #             minL = dp[i]
    #             idx = i
    #             continue
    #         if idx < i - dp[i] + 1:
    #             res = min(res, minL + dp[i])
    #         if dp[i] < minL:
    #             minL = dp[i]
    #             idx = i
    #     return -1 if res == float('inf') else res

    # 暴力，超时
    # def minSumOfLengths(self, arr: List[int], target: int) -> int:
    #     n = len(arr)
    #     dp = [0] * (n + 1)
    #     for i in range(n):
    #         dp[i + 1] = dp[i] + arr[i]
    #     res = float('inf')
    #     # 分成两段[p,q] [i,j]，枚举这两段可能的情况
    #     for q in range(n):
    #         for p in range(q, n):
    #             sum1 = dp[p + 1] - dp[q]
    #             if sum1 > target:
    #                 break
    #             if sum1 == target:
    #                 for i in range(p + 1, n):
    #                     for j in range(i, n):
    #                         sum2 = dp[j + 1] - dp[i]
    #                         if sum2 > target:
    #                             break
    #                         if sum2 == target:
    #                             res = min(res, p - q + 1 + j - i + 1)
    #     return -1 if res == float('inf') else res


assert Solution().minSumOfLengths([1, 1, 1, 2, 2, 2, 4, 4], 6) == 6
assert Solution().minSumOfLengths([1, 6, 1], 7) == -1
assert Solution().minSumOfLengths([3, 2, 2, 4, 3], 3) == 2
assert Solution().minSumOfLengths([7, 3, 4, 7], 7) == 2
assert Solution().minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6) == -1
assert Solution().minSumOfLengths([5, 5, 4, 4, 5], 3) == -1
assert Solution().minSumOfLengths([3, 1, 1, 1, 5, 1, 2, 1], 3) == 3
