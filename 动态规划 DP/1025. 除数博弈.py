class Solution:
    def divisorGame(self, N: int) -> bool:
        # dp[i]：当数字为时，先手是否能取胜
        dp = [False] * (N + 1)
        dp[1] = False
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True
                    break
        return dp[-1]

print(Solution().divisorGame(2))
print(Solution().divisorGame(3))
print(Solution().divisorGame(4))
print(Solution().divisorGame(45))
