from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dict_dist, dict_parent = {}, {}

        def find(p: str) -> str:
            if dict_parent[p] != p:
                r_p = find(dict_parent[p])
                dict_parent[p], dict_dist[p] = r_p, dict_dist[p] * dict_dist[dict_parent[p]]
            return dict_parent[p]

        for (a, b), v in zip(equations, values):
            if a not in dict_parent:
                dict_parent[a] = a
                dict_dist[a] = 1
            if b not in dict_parent:
                dict_parent[b] = b
                dict_dist[b] = 1
            # aRoot接到b上
            aRoot = find(a)
            dict_parent[aRoot] = b
            dict_dist[aRoot] = v / dict_dist[a]

            # aRoot接到bRoot上
            # aRoot, bRoot = find(a), find(b)
            # dict_parent[aRoot] = bRoot
            # dict_dist[aRoot] = v / dict_dist[a] * dict_dist[b]

            # 下面这样写是不对的
            # 当有x1/x2, x1/x4时，会把x1/x2的关系覆盖掉
            # dict_parent[a] = b
            # dict_dist[a] = v

        res = []
        for x, y in queries:
            if x not in dict_parent or y not in dict_parent:
                res.append(-1.0)
                continue
            xRoot = find(x)
            yRoot = find(y)
            if xRoot == yRoot:
                res.append(dict_dist[x] / dict_dist[y])
            else:
                res.append(-1.0)
        return res


equations = [["x1", "x2"], ["x2", "x3"], ["x1", "x4"], ["x2", "x5"]]
values = [3.0, 0.5, 3.4, 5.6]
queries = [["x2", "x4"], ["x1", "x5"], ["x1", "x3"], ["x5", "x5"], ["x5", "x1"], ["x3", "x4"], ["x4", "x3"],
           ["x6", "x6"], ["x0", "x0"]]
print(Solution().calcEquation(equations, values, queries))

# equations = [["a", "b"], ["c", "d"]]
# values = [1.0, 1.0]
# queries = [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]
# print(Solution().calcEquation(equations, values, queries))

# equations = [["a", "b"], ["b", "c"]]
# values = [2.0, 3.0]
# queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
# print(Solution().calcEquation(equations, values, queries))
