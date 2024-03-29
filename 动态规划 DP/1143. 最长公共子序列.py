class Solution:
    # 二维dp，状态->递推式->初始化
    # dp[i][j]：A[i]和A[j]结尾的子串中，LCS的长度
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 多申请一位，作为初始值
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 偏移
                if text1[i - 1] == text2[j - 1]:
                    # 状态转移方程要想清楚
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 注意不等的情况
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    # 一维dp
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     if not text1 or not text2:
    #         return 0
    #     m, n = len(text1), len(text2)
    #     # dp[i][j]表示A[0..i]和B[0..j]中最长公子序列的长度
    #     dp = [0] * (n + 1)
    #     for c in text1:
    #         tmp = [0] * (n + 1)
    #         for j in range(1, n + 1):
    #             if c == text2[j - 1]:
    #                 tmp[j] = dp[j - 1] + 1
    #             else:
    #                 tmp[j] = max(dp[j], tmp[j - 1])
    #         dp = tmp
    #     return dp[-1]


assert Solution().longestCommonSubsequence("abcde", "ace") == 3
assert Solution().longestCommonSubsequence("abc", "abc") == 3
