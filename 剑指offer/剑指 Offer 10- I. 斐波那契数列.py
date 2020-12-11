class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        pre, cur = 0, 1
        for i in range(n - 1):
            pre, cur = cur, pre + cur
        return cur % 1000000007


assert Solution().fib(2) == 1
assert Solution().fib(5) == 5
