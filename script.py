from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        pre = [0] * (n + 1)
        pre[1] = nums[0]
        for i in range(1, n):
            pre[i + 1] = pre[i] + nums[i]
            for j in range(i):
                if k == 0:
                    if pre[i + 1] - pre[j] == 0:
                        return True
                elif (pre[i + 1] - pre[j]) % k == 0:
                    return True
        return False


print(Solution().checkSubarraySum([0, 0], 0))
