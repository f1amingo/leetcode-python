s = 'abc'
i = 2
j = 2
n = 3

dp = [[0] * n for _ in range(n)]

dp[i][j] = s[i] == s[j]

print(dp)
