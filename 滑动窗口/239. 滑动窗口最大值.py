from typing import List


class Solution:
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

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        queue = []
        ans = []
        for i in range(n):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i < k - 1:
                continue
            while queue[0] < i - k + 1:
                queue.pop(0)
            ans.append(nums[queue[0]])
        return ans


nums = [7, 2, 4]
k = 2
print(Solution().maxSlidingWindow(nums, k))
