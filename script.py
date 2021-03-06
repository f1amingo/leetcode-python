from typing import List


# 返回索引，可能没有，返回-1
# 不重复，某位置旋转，可能没旋转
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        lt, rt = 0, len(nums) - 1
        while lt < rt:
            mid = (lt + rt) // 2
            # 前半有序
            if nums[lt] <= nums[mid]:
                if nums[lt] <= target <= nums[mid]:
                    rt = mid
                else:
                    lt = mid + 1
            else:
                if nums[mid] < target <= nums[rt]:
                    lt = mid + 1
                else:
                    rt = mid
        return lt if nums[lt] == target else -1


assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
