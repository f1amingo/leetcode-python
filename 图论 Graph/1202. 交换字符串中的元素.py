from typing import List


class Solution:
    # DFS
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i: int):
            visited.add(i)
            connected_nodes.append(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j)

        n = len(s)
        s_list = list(s)
        # 建图 邻接矩阵
        graph = [[] for _ in range(n)]
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        for i in range(n):
            if i in visited:
                continue
            connected_nodes = []
            dfs(i)
            connected_nodes.sort()
            char_list = sorted(s_list[i] for i in connected_nodes)
            for i, ch in zip(connected_nodes, char_list):
                s_list[i] = ch
        return ''.join(s_list)


assert Solution().smallestStringWithSwaps('dcab', [[0, 3], [1, 2], [0, 2]]) == "abcd"
assert Solution().smallestStringWithSwaps('dcab', [[0, 3], [1, 2]]) == 'bacd'
