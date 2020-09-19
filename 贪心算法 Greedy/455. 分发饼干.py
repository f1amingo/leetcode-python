from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = j = 0
        m, n = len(g), len(s)
        res = 0
        while i < m and j < n:
            if g[i] <= s[j]:
                i += 1
                j += 1
                res += 1
            else:
                i += 1
        return res


print(Solution().findContentChildren([1, 2], [1, 2, 3]))
print(Solution().findContentChildren([1, 2, 3], [1, 1]))
