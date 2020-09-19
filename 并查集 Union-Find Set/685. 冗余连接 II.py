from typing import List


class Solution:
    # 这是错误的
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(p: int) -> int:
            if p != f[p]:
                f[p] = find(f[p])
            return f[p]

        def union(p: int, q: int):
            f[find(q)] = find(p)

        f = [i for i in range(len(edges) + 1)]
        for a, b in edges:
            aRoot, bRoot = find(a), find(b)
            if aRoot == bRoot:
                return [a, b]
            union(a, b)
        return []


assert Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
assert Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1]
