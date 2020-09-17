from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []

        def find(p: int) -> int:
            # 两步一跳
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p: int, q: int):
            parent[find(q)] = find(p)

        N = len(edges)
        parent = [i for i in range(N + 1)]
        for u, v in edges:
            uRoot, vRoot = find(u), find(v)
            if uRoot == vRoot:
                return [u, v]
            union(u, v)
        return []


print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
