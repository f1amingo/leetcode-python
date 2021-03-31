from typing import List


# 正整数
# 子数组 连续
class Solution:
    # 双指针
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        lt, rt = 0, 0
        this_sum = 0
        while rt < n:
            this_sum += nums[rt]
            while this_sum >= s and lt <= rt:
                ans = min(ans, rt - lt + 1)
                this_sum -= nums[lt]
                lt += 1
            rt += 1
        return 0 if ans == float('inf') else ans


assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert Solution().minSubArrayLen(0, [2, 3, 1, 2, 4, 3]) == 1
assert Solution().minSubArrayLen(1, [1]) == 1
