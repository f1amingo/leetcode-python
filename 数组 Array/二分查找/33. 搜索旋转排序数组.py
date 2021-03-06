from typing import List


class Solution:
    # 必定有一半有序
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            # [low, mid]有序
            if nums[low] < nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            # [mid+1, high]有序
            else:
                if nums[mid + 1] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid
        return -1 if nums[low] != target else low


nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
print(Solution().search(nums, target))
