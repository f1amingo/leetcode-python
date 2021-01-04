from typing import List
import heapq


class Solution:
    # 二分查找
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 数组中小于
        def smallerCount(num: int) -> int:
            i, j = n - 1, 0
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] > num:
                    i -= 1
                else:
                    count += i + 1
                    j += 1
            return count

        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            # 如果count大于k，说明mid过大了，需要减小
            if smallerCount(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

    # 使用heap
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     if not matrix or not matrix[0]:
    #         return -1
    #     # 第k小，就是第N-k+1大
    #     n_largest = len(matrix) ** 2 - k + 1
    #     heap = []
    #     for row in matrix:
    #         for ele in row:
    #             heapq.heappush(heap, ele)
    #             if len(heap) > n_largest:
    #                 heapq.heappop(heap)
    #     return heap[0]


matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
print(Solution().kthSmallest(matrix, 8))
