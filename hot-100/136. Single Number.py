class Solution(object):
    # using map
    # 160 ms	14.2 MB
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     dic = {}
    #     for num in nums:
    #         if num in dic:
    #             dic.pop(num)
    #         else:
    #             dic[num] = 0
    #     for key in dic:
    #         return key

    # math method
    # 160ms 14MB
    # def singleNumber(self, nums):
    #     return 2 * sum(set(nums)) - sum(nums)

    # using XOR
    # 84 ms	13.6 MB
    def singleNumber(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a


print(Solution().singleNumber([4, 1, 2, 1, 2]))
