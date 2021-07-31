from typing import List


class Solution:
    # 前缀和 O(n^2)
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     n = len(nums)
    #     ans = n + 1
    #     pre = [0] * (n + 1)
    #     for i in range(1, n + 1):
    #         pre[i] = pre[i - 1] + nums[i - 1]
    #     for i in range(n + 1):
    #         no_greater = True
    #         for j in range(i + 1, n + 1):
    #             if pre[j] - pre[i] >= target:
    #                 ans = min(ans, j - i)
    #                 no_greater = False
    #                 break
    #         if no_greater:
    #             break
    #     return 0 if ans == n + 1 else ans

    # 滑动窗口
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        lo, hi = 0, 0
        cur_sum = 0
        while hi < n:
            cur_sum += nums[hi]
            hi += 1
            while cur_sum >= target:
                ans = min(ans, hi - lo)
                cur_sum -= nums[lo]
                lo += 1
        return 0 if ans == n + 1 else ans


assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1
assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
