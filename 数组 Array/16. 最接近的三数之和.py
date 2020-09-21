from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0
        # 必须是一个存在的数
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lt, rt = i + 1, n - 1
            while lt < rt:
                this_sum = nums[i] + nums[lt] + nums[rt]
                if abs(this_sum - target) < abs(res - target):
                    res = this_sum
                if this_sum > target:
                    rt -= 1
                    while lt < rt and nums[rt] == nums[rt + 1]:
                        rt -= 1
                elif this_sum < target:
                    lt += 1
                    while lt < rt and nums[lt] == nums[lt - 1]:
                        lt += 1
                else:
                    return res
        return res


assert Solution().threeSumClosest([-3, -2, -5, 3, -4], -1) == -2
assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
assert Solution().threeSumClosest([0, 2, 1, -3], 1) == 0
