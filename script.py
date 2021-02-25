from typing import List


# 所有三元组，并且不重复
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ans = []
        for i in range(n - 2):
            # 优化
            if nums[i] > 0:
                break
            # 避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lt, rt = i + 1, n - 1
            while lt < rt:
                this_sum = nums[i] + nums[lt] + nums[rt]
                if this_sum == 0:
                    ans.append([nums[i], nums[lt], nums[rt]])
                if this_sum <= 0:
                    # 小了，lt右移
                    while lt < rt and nums[lt] == nums[lt + 1]:
                        lt += 1
                    lt += 1
                if this_sum >= 0:
                    while lt < rt and nums[rt] == nums[rt - 1]:
                        rt -= 1
                    rt -= 1
        return ans


assert Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert Solution().threeSum([]) == []
assert Solution().threeSum([0]) == []
