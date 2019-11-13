class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 二维dp
        # n = len(s)
        # dp = [[0] * n for _ in range(n)]
        # start = 0
        # end = 0
        # # 倒序dp[i][j]依赖于dp[i+1][j-1]，在其左下方
        # for i in range(n - 1, -1, -1):
        #     dp[i][i] = True
        #     for j in range(i + 1, n):
        #         # 当长度为2 or 3，特殊处理
        #         if j - i > 2:
        #             dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        #         else:
        #             dp[i][j] = s[i] == s[j]
        #         if dp[i][j] and j - i > end - start:
        #             start = i
        #             end = j
        # return s[start: end + 1]

        # # 一维dp
        # n = len(s)
        # dp = [0] * n
        # start = 0
        # end = 0
        # # 倒序
        # for i in range(n - 1, -1, -1):
        #     dp[i] = True
        #     # 倒序
        #     for j in range(n - 1, i, -1):
        #         if j - i > 2:
        #             dp[j] = s[i] == s[j] and dp[j - 1]
        #         else:
        #             dp[j] = s[i] == s[j]
        #         if dp[j] and j - i > end - start:
        #             start = i
        #             end = j
        # return s[start:end + 1]

        # # 中心扩散
        # n = len(s)
        # start = 0
        # end = 0
        #
        # def helper(left, right):
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     nonlocal start, end
        #     if right - left > end - start:
        #         start = left
        #         end = right
        #
        # for i in range(n):
        #     helper(i, i)
        #     helper(i, i + 1)
        # return s[start + 1: end]


print(Solution().longestPalindrome("cbbd"))
