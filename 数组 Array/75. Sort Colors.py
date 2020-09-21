class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # cur右侧交换时不能cur+=1
        if not nums:
            return
        size = len(nums)
        p0 = 0
        p2 = size - 1
        cur = 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1


arr = [1, 2, 0]
Solution().sortColors(arr)
print(arr)
