from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post = [0] * n, [0] * n
        tmp = 1
        for i in range(n):
            tmp *= nums[i]
            pre[i] = tmp
        tmp = 1
        for i in range(n - 1, -1, -1):
            tmp *= nums[i]
            post[i] = tmp
        ans = [0] * n
        for i in range(n):
            ans[i] = (pre[i - 1] if i != 0 else 1) * (post[i + 1] if i != n - 1 else 1)
        return ans


assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
