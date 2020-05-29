class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        ptr2 = 0
        size = len(nums)
        while ptr2 < size:
            tmp = nums[ptr1]
            nums[ptr1] = nums[ptr2]
            nums[ptr2] = tmp
            while ptr1 < size:
                if nums[ptr1] == 0:
                    break
                ptr1 += 1
            ptr2 = ptr1
            while ptr2 < size:
                if nums[ptr2] != 0:
                    break
                ptr2 += 1


arr = [0, 1]
Solution().moveZeroes(arr)
print(arr)
