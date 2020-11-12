class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2 or n == 3:
            return n

        memo = [-1] * (n + 1)
        memo[1], memo[2], memo[3] = 0, 2, 3
        if n < 3:
            return memo[n]

        def dfs(i: int) -> int:
            # 没有初始化过
            if memo[i] == -1:
                min_step = i
                for j in range(2, i // 2 + 1):
                    div, mod = divmod(i, j)
                    # j是i的一个因子
                    if mod == 0:
                        min_step = min(min_step, dfs(j) + div)
                memo[i] = min_step
            return memo[i]

        return dfs(n)


assert Solution().minSteps(1) == 0
assert Solution().minSteps(2) == 2
assert Solution().minSteps(3) == 3
assert Solution().minSteps(4) == 4
assert Solution().minSteps(8) == 6
assert Solution().minSteps(9) == 6
assert Solution().minSteps(12) == 7
assert Solution().minSteps(16) == 8
