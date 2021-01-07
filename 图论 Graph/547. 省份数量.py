from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)

        n = len(isConnected)
        ans = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans


assert Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
assert Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
