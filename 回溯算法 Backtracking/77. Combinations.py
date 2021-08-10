from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i: int, j: int, cur_list: List):
            if i == k:
                ans.append(cur_list.copy())
                return
            for p in range(j, n + 1):
                cur_list[i] = p
                dfs(i + 1, p + 1, cur_list)

        ans = []
        dfs(0, 1, [0] * k)
        return ans


print(Solution().combine(1, 1))
print(Solution().combine(4, 2))
