from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        pre = [0] * (n + 1)
        pre[1] = nums[0]
        for i in range(1, n):
            pre[i + 1] = pre[i] + nums[i]
            for j in range(i):
                p_sum = pre[i + 1] - pre[j]
                if k == 0:
                    if p_sum == 0:
                        return True
                elif p_sum % k == 0:
                    return True
        return False

    # 最初写法
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     n = len(nums)
    #     if n <= 1:
    #         return False
    #     pre = [0] * (n + 1)
    #     for i in range(n):
    #         pre[i + 1] = pre[i] + nums[i]
    #     for i in range(1, n):
    #         for j in range(i + 1, n + 1):
    #             p_sum = pre[j] - pre[i - 1]
    #             # 当使用%或者/时，小心0
    #             if k == 0:
    #                 if p_sum == 0:
    #                     return True
    #             elif p_sum % k == 0:
    #                 return True
    #     return False


print(Solution().checkSubarraySum([7, 6], 6))
