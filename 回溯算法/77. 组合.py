from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cnt_list: List):
            if len(cnt_list) == k:
                res.append(cnt_list.copy())
                return
            if i > n:
                return
            for j in range(i, n + 1):
                cnt_list.append(j)
                dfs(j + 1, cnt_list)
                cnt_list.pop()

        dfs(1, [])
        return res


print(Solution().combine(4, 2))
