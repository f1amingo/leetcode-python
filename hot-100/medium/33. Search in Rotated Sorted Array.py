class Solution(object):
    # 直觉办法 先找pivot
    def search0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if target == nums[0]:
            return 0
        pivot = -1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                pivot = i
                break
        if pivot == -1:
            lo = 0
            hi = len(nums) - 1
        elif target > nums[0]:
            lo = 0
            hi = pivot - 1
        else:
            lo = pivot
            hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def search(self, nums, target):
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[l] < nums[m]:
                if nums[l] < target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


print(Solution().search([3, 1], 1))
