import collections
from typing import List


class Solution:
    # 哈希计数
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 判断可优化
        def satisfy(found) -> bool:
            for k, v in found.items():
                if v != 0:
                    return False
            return True

        m, n = len(s), len(p)
        ans = []
        found = collections.defaultdict(int)
        for c in p:
            found[c] += 1
        lt, rt = 0, 0
        while rt < m:
            found[s[rt]] -= 1
            rt += 1
            if rt - lt < n:
                continue
            if satisfy(found):
                ans.append(lt)
            found[s[lt]] += 1
            lt += 1
        return ans

    # 排序，通过，离谱！
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     p = sorted(p)
    #     ans = []
    #     len_s, len_p = len(s), len(p)
    #     for i in range(len_s - len_p + 1):
    #         if sorted(s[i:i + len_p]) == p:
    #             ans.append(i)
    #     return ans


assert Solution().findAnagrams('cbaebabacd', 'abc') == [0, 6]
assert Solution().findAnagrams('abab', 'ab') == [0, 1, 2]
