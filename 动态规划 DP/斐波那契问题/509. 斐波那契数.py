class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        return b


assert Solution().fib(2) == 1
assert Solution().fib(3) == 2
assert Solution().fib(4) == 3
