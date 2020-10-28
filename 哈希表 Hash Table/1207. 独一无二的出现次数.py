import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_dict, freq_dict = {}, {}
        for num in arr:
            num_dict[num] = num_dict.get(num, 0) + 1
        for num, freq in num_dict.items():
            if freq in freq_dict:
                return False
            freq_dict[freq] = num
        return True


print(Solution().uniqueOccurrences([1, 2]))
print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
