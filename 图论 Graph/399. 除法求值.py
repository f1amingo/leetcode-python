import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        weight = collections.defaultdict()
        # 建图
        for (a, b), v in zip(equations, values):
            graph[a].append(b)
            graph[b].append(a)
            weight[(a, b)] = v
            weight[(b, a)] = 1 / v

        def dfs(s, t) -> float:
            if s not in graph or t not in graph:
                return -1
            if s == t:
                return 1
            for node in graph[s]:
                if node == t:
                    return weight[(s, node)]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t)
                    if v != -1:
                        return weight[(s, node)] * v
            return -1

        ans = []
        for a, b in queries:
            visited = set()
            ans.append(dfs(a, b))
        return ans


Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
