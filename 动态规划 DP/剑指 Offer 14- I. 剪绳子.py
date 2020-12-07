class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        f = [0] * (n + 1)
        f[2], f[3] = 2, 3
        for i in range(4, n + 1):
            for k in range(2, i // 2 + 1):
                f[i] = max(f[i], f[i - k] * f[k])
        return f[-1]


assert Solution().cuttingRope(2) == 1
assert Solution().cuttingRope(10) == 36
