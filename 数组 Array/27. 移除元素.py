from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        lt = rt = 0
        n = len(nums)
        while lt < n and rt < n:
            if nums[lt] == val:
                rt = lt
                while rt < n and nums[rt] == val:
                    rt += 1
                if rt == n:
                    return lt
                nums[lt], nums[rt] = nums[rt], nums[lt]
            lt += 1

        return lt if lt == len(nums) else lt - 1
        # 头尾双指针
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     size = len(nums)
    #     while left <= right:
    #         if nums[left] == val:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             right -= 1
    #             size -= 1
    #         else:
    #             left += 1
    #     return size


assert Solution().removeElement([2], 3) == 1
assert Solution().removeElement([3], 3) == 0
assert Solution().removeElement([3, 2, 2, 3], 3) == 2
assert Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
