from typing import List


class Solution:
    # my solution
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # 增加左右边界 避免if
    #     to_right = [0] * (len(nums) + 2)
    #     to_left = [0] * (len(nums) + 2)
    #     ans = [0] * len(nums)
    #     to_left[0] = to_right[0] = to_left[-1] = to_right[-1] = 1
    #     for i in range(len(nums)):
    #         to_right[i + 1] = to_right[i] * nums[i]
    #     for i in range(len(nums) - 1, -1, -1):
    #         to_left[i + 1] = to_left[i + 2] * nums[i]
    #     for i in range(len(nums)):
    #         ans[i] = to_right[i] * to_left[i + 2]
    #     return ans

    # 官方题解 空间O(2n)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     to_right, to_left, ans = [0] * n, [0] * n, [0] * n
    #     to_right[0] = 1
    #     for i in range(1, n):
    #         to_right[i] = to_right[i - 1] * nums[i - 1]
    #     to_left[-1] = 1
    #     for i in range(n - 2, -1, -1):
    #         to_left[i] = to_left[i + 1] * nums[i + 1]
    #     print(to_right)
    #     print(to_left)
    #     for i in range(n):
    #         ans[i] = to_left[i] * to_right[i]
    #     return ans

    # 空间O(1) 输出空间不计
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[-1] = 1
        for i in range(n - 2, -1, -1):
            ans[i] = ans[i + 1] * nums[i + 1]
        to_right = 1
        for i in range(n):
            ans[i] = ans[i] * to_right
            to_right *= nums[i]
        return ans


print(Solution().productExceptSelf([1, 2, 3, 4]))
