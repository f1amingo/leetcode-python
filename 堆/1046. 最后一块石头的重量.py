import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a, b = -heapq.heappop(heap), -heapq.heappop(heap)
            c = a - b
            if c > 0:
                heapq.heappush(heap, -c)
        # 只要出现形如A[0]，要意识到是否可能越界
        return -heap[0] if heap else 0


assert Solution().lastStoneWeight([2, 2]) == 0
assert Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
