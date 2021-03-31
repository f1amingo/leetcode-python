class Solution:
    # 自上而下
    # 记忆化递归
    # def waysToStep(self, n: int) -> int:
    #     def f(i: int) -> int:
    #         if memo[i] == 0:
    #             memo[i] = f(i - 1) + f(i - 2) + f(i - 3)
    #         return memo[i]
    #
    #     if n < 4:
    #         return [1, 2, 4][n - 1]
    #     memo = [0] * (n + 1)
    #     memo[1] = 1
    #     memo[2] = 2
    #     memo[3] = 4
    #     return f(n) % 1000000007

    # 自下而上
    # 动态规划
    def waysToStep(self, n: int) -> int:
        if n < 4:
            return [1, 2, 4][n - 1]
        a, b, c = 4, 2, 1
        for i in range(4, n + 1):
            a, b, c = (a + b + c) % 1000000007, a, b
        return a


assert Solution().waysToStep(5) == 13
assert Solution().waysToStep(3) == 4
print(Solution().waysToStep(900750))