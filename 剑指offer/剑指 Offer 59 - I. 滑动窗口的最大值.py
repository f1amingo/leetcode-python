from collections import deque
from typing import List


# 三种方法：
# 1.暴力
# 2.单调队列
# 3.双端扫描
class Solution:
    # 3.双端扫描
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k < 2:
            return nums
        n = len(nums)
        to_right, to_left = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                to_right[i] = nums[i]
            else:
                to_right[i] = max(nums[i], to_right[i - 1])
        for i in range(n - 1, -1, -1):
            if (i + 1) % k == 0 or i == n - 1:
                to_left[i] = nums[i]
            else:
                to_left[i] = max(nums[i], to_left[i + 1])
        res = [0] * (n - k + 1)
        for i in range(n - k + 1):
            res[i] = max(to_left[i], to_right[i + k - 1])
        return res

    # 2.单调队列
    # 时间复杂度：O(2*n)；空间复杂度：O(k)
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     queue = deque()
    #     # for i in range(k - 1):
    #     #     # 相等的时候，不用把队尾pop()
    #     #     while queue and nums[queue[-1]] < nums[i]:
    #     #         queue.pop()
    #     #     # 注意这里要入队数组下标
    #     #     queue.append(i)
    #     res = []
    #     for i in range(len(nums)):
    #         # 加入当前元素后，队列保持递减，把所有小于当前元素的值弹出
    #         # 是否可以等于？
    #         # 等于对结果无影响
    #         while queue and nums[queue[-1]] <= nums[i]:
    #             queue.pop()
    #         # 当前元素，一定是在队列中的
    #         queue.append(i)
    #         # 合并初始化过程
    #         if i < k - 1:
    #             continue
    #         # 队首可能不再是窗口内元素
    #         if queue[0] < i - k + 1:
    #             queue.popleft()
    #         res.append(nums[queue[0]])
    #     return res

    # 1.暴力，时间复杂度O((n-k-1)*k)
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if not nums:
    #         return []
    #     return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


assert Solution().maxSlidingWindow([], 0) == []
assert Solution().maxSlidingWindow([1, 3, -1], 3) == [3]
assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
