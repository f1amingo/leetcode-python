import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 排序方法
        # nums.sort(reverse=True)
        # return nums[k - 1]

        # 使用堆
        return heapq.nlargest(k, nums)[-1]




print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
