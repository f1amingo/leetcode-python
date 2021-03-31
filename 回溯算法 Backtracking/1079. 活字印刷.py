from typing import List


class Solution:
    # 下面是错的 状态不好 明天再想
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(start: int):
            if start == n:
                return
            for i in range(start, n):
                if i > start and (s_list[i] == s_list[i - 1] or s_list[i] == s_list[start]):
                    continue
                nonlocal res
                res += 1
                s_list[start], s_list[i] = s_list[i], s_list[start]
                dfs(start + 1)
                s_list[start], s_list[i] = s_list[i], s_list[start]

        n = len(tiles)
        s_list = list(tiles)
        s_list.sort()
        res = 0
        dfs(0)
        return res


print(Solution().numTilePossibilities("DACBAC"))
print(Solution().numTilePossibilities("XPYP"))
