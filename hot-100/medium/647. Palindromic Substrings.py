class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i > 2:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                else:
                    dp[i][j] = s[i] == s[j]
                if dp[i][j]:
                    result += 1
        return result


# print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"))
