import collections
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        mapAB = collections.Counter(a + b for a in A for b in B)
        ans = 0
        for c in C:
            for d in D:
                if -c - d in mapAB:
                    ans += mapAB[-c - d]
        return ans

