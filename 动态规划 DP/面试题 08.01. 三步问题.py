class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        a, b, c = 1, 2, 4
        for i in range(4, n + 1):
            t = (a + b + c) % 1000000007
            a, b, c = b, c, t
        return c


print(Solution().waysToStep(1))
print(Solution().waysToStep(2))
print(Solution().waysToStep(3))
print(Solution().waysToStep(900750))
