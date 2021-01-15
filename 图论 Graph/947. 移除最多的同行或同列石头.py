from typing import List
import collections


class Solution:
    # dfs 根据行列关系添加边
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i: int):
            if i not in visited:
                visited.add(i)
                for j in graph[i]:
                    if j not in visited:
                        dfs(j)

        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(stones):
            for j, (c, d) in enumerate(stones):
                if a == c or b == d:
                    graph[i].append(j)

        ans = 0
        visited = set()
        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                ans += 1
        return len(stones) - ans
