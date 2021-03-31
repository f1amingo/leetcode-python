# f(n) n阶楼梯的不同爬法，确定了就不会变了
# f(n) = f(n-1)+f(n-2)
# 到第n阶有两种可能：1.从n-1阶爬1级；2.从n-2阶爬2级；
# n-2 >= 0 -> n>=2，递归边界f(2)=f(1)+f(0)
class Solution:
    # 记忆化递归，自顶向下
    def climbStairs(self, n: int) -> int:
        def dfs(i: int, memo) -> int:
            if i == 0 or i == 1:
                return 1
            if memo[i] == -1:
                memo[i] = dfs(i - 1, memo) + dfs(i - 2, memo)
            return memo[i]

        # memo: [-1] * (n - 1)
        # -1 表示没有计算过，最大索引为 n，因此数组大小需要 n + 1
        return dfs(n, [-1] * (n + 1))


# f(n)只依赖于f(n-1)和f(n-2)，只需要两项就足够了
# def climbStairs(self, n: int) -> int:
#     a = b = 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b

# 一维dp，自底向上
# def climbStairs(self, n: int) -> int:
#     dp = [0] * (n + 1)
#     dp[0] = dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[-1]

# 暴力深搜
# def climbStairs(self, n: int) -> int:
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

Solution().climbStairs(2)
