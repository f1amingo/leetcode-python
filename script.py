import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        sorted_strs = [''] * n
        for i in range(n):
            sorted_strs[i] = ''.join(sorted(strs[i]))
        ans_dict = collections.defaultdict(list)
        for i in range(n):
            ans_dict[sorted_strs[i]].append(strs[i])
        return list(ans_dict.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
