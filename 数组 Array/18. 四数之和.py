from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lt, rt = j + 1, n - 1
                while lt < rt:
                    this_sum = nums[i] + nums[j] + nums[lt] + nums[rt]
                    if this_sum == target:
                        res.append([nums[i], nums[j], nums[lt], nums[rt]])
                        while lt < rt and nums[lt] == nums[lt + 1]:
                            lt += 1
                        while lt < rt and nums[rt] == nums[rt - 1]:
                            rt -= 1
                        lt += 1
                        rt -= 1
                    elif this_sum < target:
                        lt += 1
                    else:
                        rt -= 1
        return res


print(Solution().fourSum([0, 0, 0, 0], 0))
# print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
