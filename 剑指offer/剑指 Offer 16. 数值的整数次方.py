class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        return res

    # 自己review时的写法
    # def myPow(self, x: float, n: int) -> float:
    #     def dfs(k: int) -> float:
    #         if k == 0:
    #             return 1
    #         div, mod = divmod(k, 2)
    #         _res = dfs(div)
    #         _res *= _res
    #         if mod == 1:
    #             _res *= x
    #         return _res
    #
    #     return dfs(n) if n > 0 else 1 / dfs(-n)

    # weiwei的递归写法
    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     if x == 0 or x == 1:
    #         return x
    #     if n < 0:
    #         return 1 / self.myPow(x, -n)
    #     if n & 1:
    #         return x * self.myPow(x, n - 1)
    #     # 注意这里x*x的写法，脑子一根筋就写不出来
    #     return self.myPow(x * x, n // 2)

    # My Solution
    # 有点冗长，helper()其实不是太有必要，判断都是一样的
    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     # python float为什么可以直接比大小
    #     if x == 0 or x == 1:
    #         return x
    #
    #     def helper(x: float, n: int) -> float:
    #         if n == 1:
    #             return x
    #         res = helper(x, n // 2)
    #         res *= res
    #         if n & 1:
    #             res *= x
    #         return res
    #
    #     result = helper(x, abs(n))
    #     if n < 0:
    #         result = 1 / result
    #     return result


print(Solution().myPow(2, -2))
