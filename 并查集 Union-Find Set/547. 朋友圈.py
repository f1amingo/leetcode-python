from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = total = len(M)
        parent = [i for i in range(N)]

        # 路径压缩的迭代实现
        def find(p: int) -> int:
            # 当前节点不是根
            while p != parent[p]:
                # 修改当前节点的父亲为祖父
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p: int, q: int):
            pRoot, qRoot = find(p), find(q)
            if pRoot == qRoot:
                return
            parent[pRoot] = qRoot
            nonlocal total
            total -= 1

        for i in range(N):
            # 对称矩阵
            for j in range(i):
                if M[i][j] == 1:
                    union(i, j)
        return total

    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     if not M:
    #         return 0
    #     N = len(M)
    #     total = N
    #     size, parent = [1] * N, [i for i in range(N)]
    #
    #     def find(p: int) -> int:
    #         if p != parent[p]:
    #             # 路径压缩成两层
    #             parent[p] = find(parent[p])
    #         return parent[p]
    #
    #     def union(p: int, q: int):
    #         pRoot, qRoot = find(p), find(q)
    #         if pRoot == qRoot:
    #             return
    #         if size[pRoot] < size[qRoot]:
    #             parent[pRoot] = qRoot
    #             size[qRoot] += size[pRoot]
    #         else:
    #             parent[qRoot] = pRoot
    #             size[pRoot] += size[qRoot]
    #         nonlocal total
    #         total -= 1
    #
    #     for i in range(N):
    #         # 对称矩阵
    #         for j in range(i):
    #             if M[i][j] == 1:
    #                 union(i, j)
    #     return total


matrix = [[1, 1, 0],
          [1, 1, 1],
          [0, 1, 1]]
print(Solution().findCircleNum(matrix))
