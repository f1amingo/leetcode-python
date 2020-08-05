from typing import List
import heapq


class Solution:
    # 方法一：排序
    # def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    #     return sorted(arr)[:k]

    # 方法二：堆排序
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        return [-x for x in hp]


print(Solution().getLeastNumbers([0, 1, 2, 1], 1))
