import collections
from typing import List


class Solution:

    # 双端队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 保存下标，下标隐含了窗口大小，用来判断窗口越界
        queue = collections.deque()
        # 初始化
        for i in range(k - 1):
            # 等于不影响
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            # 当前元素一定在队列中
            queue.append(i)
        ans = []
        for i in range(k - 1, n):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            while queue and queue[0] <= i - k:
                queue.popleft()
            queue.append(i)
            ans.append(nums[queue[0]])
        return ans

    # 奇技淫巧 leftMax + rightMax
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     to_right, to_left = [0] * len(nums), [0] * len(nums)
    #     cur_max = float('-inf')
    #     for i in range(len(nums)):
    #         cur_max = nums[i] if i % k == 0 else max(cur_max, nums[i])
    #         to_right[i] = cur_max
    #     cur_max = float('-inf')
    #     for i in range(len(nums) - 1, -1, -1):
    #         cur_max = nums[i] if (i + 1) % k == 0 else max(cur_max, nums[i])
    #         to_left[i] = cur_max
    #     ans = [0] * (len(nums) - k + 1)
    #     for high in range(k - 1, len(nums)):
    #         low = high - k + 1
    #         ans[low] = max(to_right[high], to_left[low])
    #     return ans


nums = [7, 2, 4]
k = 2
print(Solution().maxSlidingWindow(nums, k))
