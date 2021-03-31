from typing import List


# 子数组，连续
# 比较符号翻转
# 1.长度为1，则返回1
# f[i]: 以A[i]结尾，最长湍流子数组长度
class Solution:
    # dp[i]只依赖于dp[i-1]，可将状态压缩到常数
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n < 2:
            return n
        # 对应dp[1]的初始化
        cur = 1 if A[0] == A[1] else 2
        res = cur
        for i in range(2, n):
            tmp = 1
            if A[i] != A[i - 1]:
                tmp = 2  # 至少[A[i-1], A[i]]是湍流子数组
                if A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]:
                    tmp = cur + 1
                    res = max(res, tmp)
            cur = tmp
        return res

    # def maxTurbulenceSize(self, A: List[int]) -> int:
    #     n = len(A)
    #     if n < 2:
    #         return n
    #     dp = [1] * n
    #     dp[1] = 1 if A[0] == A[1] else 2
    #     res = dp[1]  # 结果至少为dp[1]
    #     for i in range(2, n):
    #         if A[i] != A[i - 1]:
    #             dp[i] = 2  # 至少[A[i-1], A[i]]是湍流子数组
    #             if A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]:
    #                 dp[i] = dp[i - 1] + 1
    #                 res = max(res, dp[i])
    #         # dp[i]初始值就是1, 下面不需要了
    #         # else:
    #         #     dp[i] = 1
    #     return res


assert Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
assert Solution().maxTurbulenceSize([9, 9]) == 1
