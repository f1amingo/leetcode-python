from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 有正负数的时候，一定要拿负数测试用例
        res, seq_sum = -float('inf'), 0
        for num in nums:
            seq_sum = max(0, seq_sum) + num
            res = max(res, seq_sum)
        return res


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([-1]))
