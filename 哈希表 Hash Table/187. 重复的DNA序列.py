import collections
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        found = collections.defaultdict(int)
        ans = []
        for i in range(len(s) - 9):
            tmp = s[i:i + 10]
            found[tmp] += 1
            if found[tmp] == 2:
                ans.append(tmp)
        return ans


assert Solution().findRepeatedDnaSequences(
    "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ["AAAAACCCCC", "CCCCCAAAAA"]
