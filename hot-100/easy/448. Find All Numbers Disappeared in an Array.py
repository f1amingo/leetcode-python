class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # using counter
        # count = [0] * len(nums)
        # for i in nums:
        #     count[i - 1] += 1
        # res = []
        # for i in range(len(nums)):
        #     if count[i] == 0:
        #         res.append(i + 1)
        # return res

        # 鸽巢做法
        # def swap(nums, i1, i2):
        #     nums[i1] = nums[i1] ^ nums[i2]
        #     nums[i2] = nums[i1] ^ nums[i2]
        #     nums[i1] = nums[i1] ^ nums[i2]
        #
        # n = len(nums)
        #
        # for i in range(n):
        #     while nums[nums[i] - 1] != nums[i]:
        #         swap(nums, i, nums[i] - 1)
        # return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]

        # 数字做下标反号
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
