class Solution:
    # 超时
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        way_count = 0

        def dfs(x, y, z):
            nonlocal way_count
            if x == 0 or x == m + 1:
                way_count += 1
                return
            if y == 0 or y == n + 1:
                way_count += 1
                return
            if z > 0:
                if x < m + 1:
                    dfs(x + 1, y, z - 1)
                if x > 0:
                    dfs(x - 1, y, z - 1)
                if y < n + 1:
                    dfs(x, y + 1, z - 1)
                if y > 0:
                    dfs(x, y - 1, z - 1)

        dfs(i + 1, j + 1, N)
        return way_count


print(Solution().findPaths(1, 3, 3, 0, 1))
print(Solution().findPaths(2, 2, 2, 0, 0))
