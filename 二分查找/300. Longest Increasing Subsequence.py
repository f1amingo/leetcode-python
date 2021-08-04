from typing import List


# 子序列，不需要连续
class Solution:
    # 如果要最长，就要缓慢增长
    # dp[i] 长度为 (i+1) 的序列的末尾元素
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        ans = 0
        for num in nums:
            # 大于最后一位
            if num > dp[ans]:
                ans += 1
                dp[ans] = num
                continue
            lo, hi = 0, ans
            while lo < hi:
                mid = (lo + hi) // 2
                if dp[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            dp[lo] = min(dp[lo], num)
        return ans + 1

    # dp[i]: 以A[i]结尾的LIS长度
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         for j in range(i - 1, -1, -1):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)


assert Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
