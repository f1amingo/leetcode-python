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

    # 前缀和
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     to_right, to_left = [0] * n, [0] * n
    #     this_max = float('-inf')
    #     for i in range(n):
    #         if i % k == 0:
    #             this_max = nums[i]
    #         else:
    #             this_max = max(this_max, nums[i])
    #         to_right[i] = this_max
    #     this_max = float('-inf')
    #     for i in range(n - 1, -1, -1):
    #         if (i + 1) % k == 0:
    #             this_max = nums[i]
    #         else:
    #             this_max = max(this_max, nums[i])
    #         to_left[i] = this_max
    #     ans = []
    #     for i in range(n - k + 1):
    #         ans.append(max(to_left[i], to_right[i + k - 1]))
    #     return ans

    # 更简洁的暴力
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]

    # 暴力超时
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     ans = []
    #     for i in range(len(nums) - k + 1):
    #         ans.append(max(nums[i:i + k]))
    #     return ans


assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert Solution().maxSlidingWindow([1], 1) == [1]
assert Solution().maxSlidingWindow([1, -1], 1) == [1, -1]
assert Solution().maxSlidingWindow([9, 11], 2) == [11]
assert Solution().maxSlidingWindow([4, -2], 2) == [4]
