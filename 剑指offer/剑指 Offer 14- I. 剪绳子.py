class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        a, b = divmod(n, 3)
        if b == 0: return 3 ** a
        if b == 1: return 3 ** (a - 1) * 4
        if b == 2: return 3 ** a * 2

    # def cuttingRope(self, n: int) -> int:
    #     if n < 2:
    #         return 0
    #     # 长度为2、3时，不满足递推公式，特殊处理
    #     if n == 2:
    #         return 1
    #     if n == 3:
    #         return 2
    #     # 增加1，因此数组下标与绳子长度语义一致
    #     # 避免了数组下标与长度的转换
    #     dp = [0] * (n + 1)
    #     # 注意这里的值与上面的不一样
    #     # 这里并没有再对长度为2、3的绳子再切
    #     # 因为下面循环中，访问到dp[2]、dp[3]时，已经是切过后了
    #     dp[1], dp[2], dp[3] = 1, 2, 3
    #     # 为什么是从4开始呢？
    #     # 这里需要弄清楚，何时绳子切两半会比不切更大
    #     # 假设绳长为n, 不切时就为n
    #     # 切1出去，积为1*(n-1)永远比n小
    #     # 切2出去，积为2*(n-2)，当n==4时，n==2*(n-2)，
    #     # 递归公式适用的边界就在这里
    #     for i in range(4, n + 1):
    #         for j in range(1, i // 2 + 1):
    #             dp[i] = max(dp[i], dp[j] * dp[i - j])
    #     return dp[-1]


assert Solution().cuttingRope(2) == 1
assert Solution().cuttingRope(10) == 36
