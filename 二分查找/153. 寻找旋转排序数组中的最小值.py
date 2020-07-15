from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 此时说明整体有序
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # [mid, right]有序，mid是后半部分最小的元素，是一个候选值
            if nums[mid] < nums[right]:
                right = mid
            # [mid, right]无序，那么最小值一定在无序部分
            # 因为数组的无序是因为，最小值处有一个转折导致的
            else:
                left = mid + 1
        return nums[left]


print(Solution().findMin( [4,5,6,7,0,1,2]))
