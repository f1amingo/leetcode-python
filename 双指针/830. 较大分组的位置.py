from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n, ans = len(s), []
        lt, rt = 0, 0
        while rt < n:
            rt += 1
            while rt < n and s[rt] == s[rt - 1]:
                rt += 1
            if rt - lt >= 3:
                ans.append([lt, rt - 1])
            lt = rt
        return ans


assert Solution().largeGroupPositions('abbxxxxzzy') == [[3, 6]]
