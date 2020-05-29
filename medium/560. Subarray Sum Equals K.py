from typing import List


class Solution:
    # 暴力 超时
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     ans = 0
    #     for i in range(len(nums)):
    #         cur_sum = 0
    #         for j in range(i, len(nums)):
    #             cur_sum += nums[j]
    #             if cur_sum == k:
    #                 ans += 1
    #     return ans

    # 保存每次前i项的和的数目
    def subarraySum(self, nums: List[int], k: int) -> int:
        look_up = {0: 1}
        pre = 0
        count = 0
        for num in nums:
            pre += num
            count += look_up.get(pre - k, 0)
            look_up[pre] = look_up.get(pre, 0) + 1
        return count


nums = [1, 2, 1, 2, 1]
k = 3
print(Solution().subarraySum(nums, k))
