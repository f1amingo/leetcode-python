from typing import List


# nums[i]应该放到nums[nums[i]-1]，
# 如果nums[nums[i]-1]已经是nums[i]了，则重复
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            # 每个数放到属于自己的位置
            while nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        ans = []
        # 每个位置上的数，不属于这个位置，那么它是多的
        for i in range(size):
            if i + 1 != nums[i]:
                ans.append(nums[i])
        return ans


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
