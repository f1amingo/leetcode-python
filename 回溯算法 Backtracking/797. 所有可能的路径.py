from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []

        def dfs(vertex: int, cur_path: List):
            if cur_path and cur_path[-1] == n - 1:
                res.append(cur_path.copy())
                return
            for to in graph[vertex]:
                cur_path.append(to)
                dfs(to, cur_path)
                cur_path.pop()

        dfs(0, [0])
        return res


print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))
print(Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
print(Solution().allPathsSourceTarget([[1], []]))
print(Solution().allPathsSourceTarget([[1, 2, 3], [2], [3], []]))
print(Solution().allPathsSourceTarget([[1, 3], [2], [3], []]))
print(Solution().allPathsSourceTarget([[2], [2], []]))
