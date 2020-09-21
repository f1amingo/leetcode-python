class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        if size == 0:
            return [-1, -1]
        left = 0
        right = size - 1
        center = -1
        while left <= right:
            center = int((left + right) / 2)
            if nums[center] < target:
                left = center + 1
            elif nums[center] > target:
                right = center - 1
            else:
                break
        l1, r1, l2, r2 = left, center, center, right
        if left <= right:
            while l1 <= r1:
                ci = int((l1 + r1) / 2)
                if nums[ci] < target:
                    l1 = ci + 1
                elif nums[ci] == target:
                    r1 = ci - 1
            while l2 <= r2:
                ci = int((l2 + r2) / 2)
                if nums[ci] > target:
                    r2 = ci - 1
                elif nums[ci] == target:
                    l2 = ci + 1
            return [l1, r2]
        else:
            return [-1, -1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
