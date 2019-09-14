n = 4
C = 10
V = [0, 2, 4, 3, 7]
W = [0, 2, 3, 5, 5]
dp = [[0 for _ in range(C + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, C + 1):
        if j < W[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - W[i]] + V[i], dp[i - 1][j])

for clist in dp:
    print(clist)
