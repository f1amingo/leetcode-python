from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ans = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            lt, rt = i + 1, n - 1
            while lt < rt:
                this_sum = nums[i] + nums[lt] + nums[rt]
                if this_sum == 0:
                    ans.append([nums[i], nums[lt], nums[rt]])
                if this_sum <= 0:
                    lt += 1
                    while lt < rt and nums[lt] == nums[lt - 1]:
                        lt += 1
                if this_sum >= 0:
                    rt -= 1
                    while lt < rt and nums[rt] == nums[rt + 1]:
                        rt -= 1
        return ans
