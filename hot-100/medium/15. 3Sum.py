class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        n = len(nums)
        sorted_nums = sorted(nums)
        for i in range(0, n):
            if i != 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if j != i + 1 and sorted_nums[j] == sorted_nums[j - 1]:
                    j += 1
                    continue
                if k != n - 1 and sorted_nums[k] == sorted_nums[k + 1]:
                    k -= 1
                    continue
                this_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if this_sum == 0:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                elif this_sum < 0:
                    j += 1
                else:
                    k -= 1
        return res


print(Solution().threeSum([1, -1, -1, 0]))
