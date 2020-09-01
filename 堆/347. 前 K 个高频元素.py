import collections
import heapq
from typing import List


# python 堆根据指定的key生成堆
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = collections.Counter(nums)
        for num in counter:
            heapq.heappush(heap, (counter[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
