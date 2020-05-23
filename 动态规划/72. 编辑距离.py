class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        # dp[i][j] i是外层对应行 j是内层对应列
        dp = [[0] * (len1 + 1) for _ in range(len2 + 1)]
        for i in range(len1 + 1):
            dp[0][i] = i
        for i in range(len2 + 1):
            dp[i][0] = i

        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                # 减一偏移
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 经过dp[i - 1][j]次操作后，word1[:j]==word2[:i-1]，此时为word2添加一位，word1[:j]==word2[:i]
                    # dp[i][j - 1]对word1删除
                    # dp[i - 1][j - 1]替换
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]


w1 = 'horse'
w2 = 'ros'
print(Solution().minDistance(w1, w2))
