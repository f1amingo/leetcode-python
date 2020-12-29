from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacent_edge = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        visited = [False] * numCourses
        for pre in prerequisites:
            adjacent_edge[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                visited[i] = True
        ans = []
        while queue:
            top = queue.pop(0)
            ans.append(top)
            for i in adjacent_edge[top]:
                in_degree[i] -= 1
                if in_degree[i] == 0 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return ans if len(ans) == numCourses else []


n = 3
pre_list = [[1, 0], [0, 1], [0, 2]]
print(Solution().findOrder(n, pre_list))
