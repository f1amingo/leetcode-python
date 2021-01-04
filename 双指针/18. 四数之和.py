from typing import List


class Solution:
    # review
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 3):
            # 跳过重复的a
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # 跳过重复的b
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, n - 1
                while lo < hi:
                    tmp = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if tmp == target:
                        ans.append([nums[i], nums[j], nums[lo], nums[hi]])
                    # 偏大要减小
                    if tmp >= target:
                        hi -= 1
                        # 跳过重复的hi
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                    # 偏小要增大
                    if tmp <= target:
                        lo += 1
                        # 跳过重复的lo
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
        return ans

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     n = len(nums)
    #     if n < 4:
    #         return []
    #     nums.sort()
    #     res = []
    #     for i in range(n - 3):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         for j in range(i + 1, n - 2):
    #             if j > i + 1 and nums[j] == nums[j - 1]:
    #                 continue
    #             lt, rt = j + 1, n - 1
    #             while lt < rt:
    #                 this_sum = nums[i] + nums[j] + nums[lt] + nums[rt]
    #                 if this_sum == target:
    #                     res.append([nums[i], nums[j], nums[lt], nums[rt]])
    #                     while lt < rt and nums[lt] == nums[lt + 1]:
    #                         lt += 1
    #                     while lt < rt and nums[rt] == nums[rt - 1]:
    #                         rt -= 1
    #                     lt += 1
    #                     rt -= 1
    #                 elif this_sum < target:
    #                     lt += 1
    #                 else:
    #                     rt -= 1
    #     return res


print(Solution().fourSum([0, 0, 0, 0], 0))
# print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
