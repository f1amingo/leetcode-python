# 最长回文子串，要连续
# 1. 找出所有回文串
# 2. 找到其中最长的
# 某一子串可记为：S[i:j]，长度为j-i
# 枚举所有(i, j), 找到其中是回文串，并且最长的


class Solution:
    # 中心扩散
    def longestPalindrome(self, s: str) -> str:
        def helper(lo: int, hi: int):
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            nonlocal lt, rt
            if hi - lo > rt - lt:
                lt, rt = lo, hi

        n = len(s)
        lt, rt = -1, 1
        for i in range(n - 1):
            helper(i, i)
            helper(i, i + 1)
        return s[lt + 1:rt]

    # 一维动态规划
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     lt = rt = 0
    #     dp = [False] * n
    #     for i in range(n - 1, -1, -1):
    #         for j in range(n - 1, i, -1):  # 逆序
    #             dp[j] = s[i] == s[j]
    #             if j - i >= 3:
    #                 dp[j] = dp[j] and dp[j - 1]
    #             if dp[j] and j - i > rt - lt:
    #                 lt, rt = i, j
    #     return s[lt:rt + 1]

    # 二维动态规划
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     lt = rt = 0
    #     dp = [[False] * n for _ in range(n)]
    #     for i in range(n - 1, -1, -1):
    #         dp[i][i] = True
    #         for j in range(i + 1, n):
    #             dp[i][j] = s[i] == s[j]
    #             if j - i >= 3:
    #                 dp[i][j] = dp[i][j] and dp[i + 1][j - 1]
    #             if dp[i][j] and j - i > rt - lt:
    #                 lt, rt = i, j
    #     return s[lt:rt + 1]

    # 记忆化递归
    # def longestPalindrome(self, s: str) -> str:
    #     def isPalindrome(i: int, j: int, memo: list):
    #         if memo[i][j] is None:
    #             # 注意长度为2，老是错(1,2)(2,1)是不一样的
    #             if j - i < 3:
    #                 memo[i][j] = s[i] == s[j]
    #             else:
    #                 memo[i][j] = s[i] == s[j] and isPalindrome(i + 1, j - 1, memo)
    #         return memo[i][j]
    #
    #     n = len(s)
    #     lt = rt = 0
    #     memo = [[None] * n for _ in range(n)]
    #     for i in range(n):
    #         memo[i][i] = True
    #         for j in range(i + 1, n):
    #             if isPalindrome(i, j, memo):
    #                 if j - i > rt - lt:
    #                     lt, rt = i, j
    #     return s[lt:rt + 1]

    # 暴力，超时
    # 为什么慢？假设输入为"aabbaa"
    # "bb"会在检查子串"aabb""aabba""aabbaa""abba""abbaa""bba""bbaa"的过程中重复被检查
    # def longestPalindrome(self, s: str) -> str:
    #     def isPalindrome(i: int, j: int):
    #         while i < j:
    #             if s[i] != s[j]:
    #                 return False
    #             i += 1
    #             j -= 1
    #         return True
    #
    #     n = len(s)
    #     lt = rt = 0
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if isPalindrome(i, j):
    #                 if j - i > rt - lt:
    #                     lt, rt = i, j
    #
    #     return s[lt:rt + 1]


assert Solution().longestPalindrome("babad") == "bab"
assert Solution().longestPalindrome("cbbd") == "bb"
