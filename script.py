from typing import List

import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = collections.Counter(nums)
        array_freq = [(freq, num) for num, freq in counter_nums.items()]
        array_freq.sort(key=lambda x: -x[0])
        return [num for freq, num in array_freq[:k]]


assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert Solution().topKFrequent([1], 1) == [1]
