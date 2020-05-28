from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        to_right, to_left = [0] * len(nums), [0] * len(nums)
        cur_max = float('-inf')
        for i in range(len(nums)):
            cur_max = nums[i] if i % k == 0 else max(cur_max, nums[i])
            to_right[i] = cur_max
        cur_max = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            cur_max = nums[i] if (i + 1) % k == 0 else max(cur_max, nums[i])
            to_left[i] = cur_max
        ans = [0] * (len(nums) - k + 1)
        for high in range(k - 1, len(nums)):
            low = high - k + 1
            ans[low] = max(to_right[high], to_left[low])
        return ans


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
