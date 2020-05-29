class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 动态规划
        # result = 0
        # n = len(s)
        # dp = [[0] * n for _ in range(n)]
        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         if j - i > 2:
        #             dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        #         else:
        #             dp[i][j] = s[i] == s[j]
        #         if dp[i][j]:
        #             result += 1
        # return result

        # 中心扩散
        res = 0

        def helper(left, right):
            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1

        for i in range(len(s)):
            # 以s[i]为中心的字符串是否是回文串，奇数
            helper(i, i)
            # 以s[i]，s[i+1]为中心的字符串是否是回文串，偶数
            helper(i, i + 1)
        return res


# print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"))
