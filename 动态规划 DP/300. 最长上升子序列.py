from typing import List


class Solution:
    # 如果想尽可能长，那么上升的就要越慢
    # dp[i]：长度为i+1的LIS的末尾数字
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        ans = 0
        for num in nums:
            lo, hi = 0, ans  # 注意上界
            while lo < hi:
                mid = (lo + hi) // 2
                if dp[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            dp[lo] = num
            ans = max(ans, lo + 1)
        return ans

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     # python优美是第一位的
    #     return max(dp)


assert Solution().lengthOfLIS([]) == 0
assert Solution().lengthOfLIS([1]) == 1
assert Solution().lengthOfLIS([1, 2]) == 2
assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
