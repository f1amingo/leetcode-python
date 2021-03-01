from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            # nums[i]这个数应该在nums[nums[i] - 1]这个位置
            # 每个数有自己的位置，每个位置不一定有自己的数
            while nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        ans = []
        for i in range(size):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans


assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
