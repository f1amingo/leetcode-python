from typing import List


class Solution:
    # DFS + 节点标记
    # flag[i] = 0: 未访问
    # flag[i] = 1: 访问中
    # flag[i] = 2: 已访问
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i: int) -> bool:
            if flag[i] == 1:
                return False
            if flag[i] == 2:
                return True
            flag[i] = 1
            for j in graph[i]:
                if not dfs(j):
                    return False
            flag[i] = 2
            return True

        graph = [[] for _ in range(numCourses)]
        flag = [0] * numCourses
        for cur, pre in prerequisites:
            graph[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    # 拓扑排序
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     graph = [[] for _ in range(numCourses)]
    #     indegree = [0] * numCourses
    #     queue = []
    #     # 建图，初始化入度表
    #     for cur, pre in prerequisites:
    #         graph[pre].append(cur)
    #         indegree[cur] += 1
    #     # 将入度为0的点加入队列
    #     for i in range(numCourses):
    #         if indegree[i] == 0:
    #             queue.append(i)
    #     # TopoSort
    #     while queue:
    #         v = queue.pop()
    #         numCourses -= 1
    #         for adj in graph[v]:
    #             indegree[adj] -= 1
    #             if indegree[adj] == 0:
    #                 queue.append(adj)
    #     return numCourses == 0


assert Solution().canFinish(2, [[1, 0]])
assert not Solution().canFinish(2, [[1, 0], [0, 1]])
