from typing import List


class Solution:
    # 奇技淫巧 leftMax + rightMax
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     if n * k == 0:
    #         return []
    #     if k == 1:
    #         return nums
    #
    #     rightMax = [0] * n
    #     cur_max = nums[-1]
    #     for i in range(n - 1, -1, -1):
    #         cur_max = nums[i] if (i + 1) % k == 0 else max(cur_max, nums[i])
    #         rightMax[i] = cur_max
    #     leftMax = [0] * n
    #     cur_max = nums[0]
    #     for i in range(n):
    #         cur_max = nums[i] if i % k == 0 else max(cur_max, nums[i])
    #         leftMax[i] = cur_max
    #     ans = [0] * (n - k + 1)
    #     for i in range(n - k + 1):
    #         ans[i] = max(rightMax[i], leftMax[i + k - 1])
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
