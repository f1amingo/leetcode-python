from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        N = len(edges)
        # 保存图
        graph = [[False] * (N + 1) for _ in range(N + 1)]
        visited = [[False] * (N + 1) for _ in range(N + 1)]
        for edge in edges:
            v1, v2 = edge
            graph[v1][v2] = graph[v2][v1] = True

        # 在图g中，从src出发到dst是否可达
        def dfs(src: int, dst: int) -> bool:
            if src == dst:
                return True
            for i in range(N + 1):
                if graph[src][i]:
                    if not visited[src][i]:
                        visited[src][i] = visited[i][src] = True
                        this_res = dfs(i, dst)
                        visited[src][i] = visited[i][src] = False
                        if this_res:
                            return True
            return False

        res = []
        for edge in edges[::-1]:
            v1, v2 = edge
            graph[v1][v2] = graph[v2][v1] = False  # 先移除这条边
            if dfs(v1, v2):
                res = edge
                break
            else:
                graph[v1][v2] = graph[v2][v1] = True  # 不冗余则恢复
        return res


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
