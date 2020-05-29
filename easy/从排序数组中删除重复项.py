class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        p1 = 1
        while p1 < n:
            if nums[p1] == nums[p1 - 1]:
                break
            p1 += 1
        p2 = p1 + 1
        while p2 < n:
            if nums[p2] == nums[p1 - 1]:
                p2 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
        return p1


arr = [1, 2]
arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(arr))
print(arr)
