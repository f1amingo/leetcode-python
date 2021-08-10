from typing import List


# 最大的数，整个数组降序排列
# 降序大，升序小
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 倒序第一段升序左端点
        m = n - 2
        while m >= 0 and nums[m] >= nums[m + 1]:
            m -= 1
        if m != -1:
            # 交换，倒序第一个大于A[m]的值
            k = n - 1
            while k > m and nums[k] <= nums[m]:
                k -= 1
            nums[k], nums[m] = nums[m], nums[k]
        lt, rt = m + 1, n - 1
        while lt < rt:
            nums[lt], nums[rt] = nums[rt], nums[lt]
            lt += 1
            rt -= 1
        print(nums)


Solution().nextPermutation([5, 1, 1])
Solution().nextPermutation([1, 5, 1])
