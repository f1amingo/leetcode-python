import heapq
from typing import List

import collections


class Solution:
    # 前k大，最小堆
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = collections.Counter(nums)
        heap = []
        for num, freq in counter_nums.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
                continue
            heapq.heappush(heap, (freq, num))
            while len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]

    # 统计频率，按频率排序
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter_nums = collections.Counter(nums)
    #     array_freq = [(freq, num) for num, freq in counter_nums.items()]
    #     array_freq.sort(key=lambda x: -x[0])
    #     return [num for freq, num in array_freq[:k]]


assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [2, 1]
assert Solution().topKFrequent([1], 1) == [1]
