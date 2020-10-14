class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(k: int) -> float:
            if k == 0:
                return 1
            div, mod = divmod(k, 2)
            _res = dfs(div)
            _res *= _res
            if mod == 1:
                _res *= x
            return _res

        return dfs(n) if n > 0 else 1 / dfs(-n)


print(Solution().myPow(2, 10))
print(Solution().myPow(2.1, 3))
print(Solution().myPow(2, -2))
