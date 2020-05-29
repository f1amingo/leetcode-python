from typing import List


class Solution:
    # 超时
    # def jump(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     dp = [0] * n
    #     for i in range(n):
    #         end = False
    #         for j in range(i + 1, i + nums[i] + 1):
    #             if j < n and not dp[j]:
    #                 dp[j] = dp[i] + 1
    #                 if j == n - 1:
    #                     end = True
    #                     break
    #         if end:
    #             break
    #     return dp[-1]
    # my solution
    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n < 2:
    #         return 0
    #     right_most, jump_count = 0, 0
    #     idx = 0
    #     chosen_idx = 0
    #     while right_most < n - 1:
    #         right_most = chosen_idx + nums[chosen_idx]
    #         jump_count += 1
    #         max_right = 0
    #         right_bound = min(right_most + 1, n)
    #         for i in range(idx, right_bound):
    #             if max_right < i + nums[i]:
    #                 max_right = i + nums[i]
    #                 chosen_idx = i
    #         idx = right_bound - 1
    #     return jump_count

    # 官方题解
    def jump(self, nums: List[int]) -> int:
        maxPos, step, end = 0, 0, 0
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= len(nums) - 1:
                return step + 1
            if i == end:
                end = maxPos
                step += 1
        return step


assert Solution().jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]) == 2
assert Solution().jump([2, 3, 1, 1, 4]) == 2
assert Solution().jump([1, 1]) == 1
assert Solution().jump([1]) == 0
assert Solution().jump([]) == 0
assert Solution().jump([2, 1]) == 1
