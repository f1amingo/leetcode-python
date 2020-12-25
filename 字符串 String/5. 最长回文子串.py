class Solution:
    # dp
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        lt, rt = 0, 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = j - i < 3 or dp[i + 1][j - 1]
                if dp[i][j] and j - i > rt - lt:
                    lt, rt = i, j
        return s[lt:rt + 1]

    # My solution
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if n < 2:
    #         return s
    #     start, end = 0, -1
    #
    #     def helper(i, j):
    #         while i >= 0 and j < n:
    #             if s[i] != s[j]:
    #                 break
    #             nonlocal start, end
    #             if j - i > end - start:
    #                 start, end = i, j
    #             i -= 1
    #             j += 1
    #
    #     for i in range(1, n):
    #         helper(i, i)
    #         helper(i - 1, i)
    #     return s[start: end + 1]

    # Official Solution: Center expanding
    # def longestPalindrome(self, s: str) -> str:
    #     def helper(left, right):
    #         # 注意这里的循环条件，跳出循环时，left和right可能下标越界
    #         while left >= 0 and right < len(s) and s[left] == s[right]:
    #             left, right = left - 1, right + 1
    #         nonlocal start, end
    #         # 这里要-2，因为跳出while后的下标都是不满足条件的，需要回退回去
    #         # 也可能根本没有进入循环，此时只可能是i, i+1的情况，说明当前回文串长度为1
    #         # if right - left - 2 > end - start:
    #         #     start, end = left + 1, right - 1
    #         # 另一种写法，保存的start, end是恰好不满足条件的那个边界
    #         if right - left > end - start:
    #             start, end = left, right
    #
    #     start, end = 0, 0
    #     for i in range(len(s)):
    #         helper(i, i)
    #         helper(i, i + 1)
    #     # return s[start: end + 1]
    #     # 另一种写法，注意这里的回退
    #     return s[start + 1: end]

    # using 2-D dp
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     dp = [[False] * n for _ in range(n)]
    #     start, end = 0, 0
    #     # 倒序dp[i][j]依赖dp[i+1][j-1] 左下方
    #     for i in range(n - 1, -1, -1):
    #         for j in range(i, n):
    #             # 长度为1
    #             if i == j:
    #                 dp[i][j] = True
    #             # 长度为2
    #             elif j - i + 1 == 2:
    #                 dp[i][j] = s[i] == s[j]
    #             # 长度为3
    #             else:
    #                 dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
    #             if dp[i][j] and j - i > end - start:
    #                 start, end = i, j
    #     return s[start:end + 1]

    # using 1-D dp
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     dp = [False] * n
    #     start, end = 0, 0
    #     # 倒序dp[i][j]依赖dp[i+1][j-1] 左下方
    #     for i in range(n - 1, -1, -1):
    #         for j in range(n - 1, i - 1, -1):
    #             # 长度为1
    #             if i == j:
    #                 dp[j] = True
    #             # 长度为2
    #             elif j - i + 1 == 2:
    #                 dp[j] = s[i] == s[j]
    #             # 长度为3
    #             else:
    #                 dp[j] = s[i] == s[j] and dp[j - 1]
    #             if dp[j] and j - i > end - start:
    #                 start, end = i, j
    #     return s[start:end + 1]


print(Solution().longestPalindrome('cbbd'))
print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome(''))
print(Solution().longestPalindrome('a'))
print(Solution().longestPalindrome('ac'))
print(Solution().longestPalindrome('aa'))
print(Solution().longestPalindrome('aaa'))
