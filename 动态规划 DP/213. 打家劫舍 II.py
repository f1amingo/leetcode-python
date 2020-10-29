from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 3:
            return max(nums)

        def helper(left, right):
            pre, cnt = 0, 0
            for i in range(left, right):
                pre, cnt = cnt, max(cnt, pre + nums[i])
            return cnt

        return max(helper(1, n), helper(0, n - 1))


print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 3, 2]))
