class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        back = nums[:]
        for i in range(0, n):
            nums[(i + k) % n] = back[i]
        return nums


arr = [1, 2, 3, 4, 5, 6, 7, ]
k = 8
Solution().rotate(arr, k)
print(arr)
