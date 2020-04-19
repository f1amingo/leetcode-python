from typing import List


class Solution:
    # 奇技淫巧 leftMax + rightMax
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        rightMax = [0] * n
        cur_max = nums[-1]
        for i in range(n - 1, -1, -1):
            cur_max = nums[i] if (i + 1) % k == 0 else max(cur_max, nums[i])
            rightMax[i] = cur_max
        leftMax = [0] * n
        cur_max = nums[0]
        for i in range(n):
            cur_max = nums[i] if i % k == 0 else max(cur_max, nums[i])
            leftMax[i] = cur_max
        ans = [0] * (n - k + 1)
        for i in range(n - k + 1):
            ans[i] = max(rightMax[i], leftMax[i + k - 1])
        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
