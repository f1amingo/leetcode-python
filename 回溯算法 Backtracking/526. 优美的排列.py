class Solution:
    # 暴力-回溯，依次设置每个位置
    def countArrangement(self, N: int) -> int:
        def dfs(idx: int):
            if idx == N:
                nonlocal res
                res += 1
                return
            for num in range(1, N + 1):
                if not visited[num - 1] and (num % (idx + 1) == 0 or (idx + 1) % num == 0):
                    visited[num - 1] = True
                    dfs(idx + 1)
                    visited[num - 1] = False

        visited = [False] * N
        res = 0
        dfs(0)
        return res


print(Solution().countArrangement(1))
print(Solution().countArrangement(2))
print(Solution().countArrangement(15))
