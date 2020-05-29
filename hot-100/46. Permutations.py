class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def per(nums, list):
            if not nums:
                res.append(list)
            for (i, num) in enumerate(nums):
                per(nums[:i] + nums[i + 1:], list + [num])

        per(nums, [])
        return res


print(Solution().permute([1, 2, 3]))
