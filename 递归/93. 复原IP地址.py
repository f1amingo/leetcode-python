from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        res = []

        def dfs(segments: List, seg_start):
            if len(segments) == 4:
                if seg_start == n:
                    res.append('.'.join(segments))
                else:
                    return
            # 这里要小心越界
            for i in range(seg_start, min(seg_start + 3, n)):
                seg = s[seg_start: i + 1]
                # 如果以0开头，那么只能是0
                if seg[0] == '0' and len(seg) > 1:
                    break
                if len(seg) == 3 and int(seg) > 255:
                    return
                segments.append(seg)
                dfs(segments, i + 1)
                segments.pop()

        dfs([], 0)
        return res


print(
    Solution().restoreIpAddresses("255255111")
)
