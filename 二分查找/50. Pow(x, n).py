class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(_n):
            if _n == 0:
                return 1
            y = helper(_n // 2)
            return y * y * x if _n & 1 else y * y

        return helper(n) if n >= 0 else 1 / helper(-n)


print(Solution().myPow(2.0000, -2))
