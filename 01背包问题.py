weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8


# 最优解10

def knapsack(w: list, v: list, C: int) -> int:
    N = len(w)
    dp = [0] * (C + 1)
    for i in range(N):
        for c in range(C, w[i] - 1, -1):
            dp[c] = max(dp[c], dp[c - w[i]] + v[i])
        print(dp)
    return dp[-1]


print(knapsack(weights, values, capacity))
