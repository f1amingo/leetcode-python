class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 递归
        # if n == 1:
        #     return 0
        # else:
        #     x = self.lastRemaining(n - 1, m)
        #     return (x + m) % n
        res = 0
        for i in range(2, n + 1):
            res = (res + m) % i
        return res


print(Solution().lastRemaining(5, 3))
