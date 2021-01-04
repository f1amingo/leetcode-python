class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        half, mod = divmod(n, 2)
        ans = self.myPow(x, half)
        ans = ans * ans
        if mod == 1:
            ans *= x
        return ans


assert Solution().myPow(2, 10) == 1024
