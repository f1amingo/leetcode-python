from typing import List


class Solution:
    # 之前
    # def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     odd_list = []
    #     for i in range(n):
    #         if nums[i] & 1 == 1:
    #             odd_list.append(i)
    #     odd_n = len(odd_list)
    #     ans = 0
    #     for right in range(k - 1, odd_n):
    #         left = right - k + 1
    #         left_count = odd_list[left] + 1 if left == 0 else odd_list[left] - odd_list[left - 1]
    #         right_count = n - odd_list[right] if right == odd_n - 1 else odd_list[right + 1] - odd_list[right]
    #         ans += left_count * right_count
    #     return ans

    # 重做
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 保存奇数下标
        # 快速访问left-1和right+1
        # 左边界初始为-1
        odds = [-1]
        for i, num in enumerate(nums):
            if num % 2 == 1:
                odds.append(i)
        # 右边界初始为len(nums)
        odds.append(len(nums))
        left = right = 1
        ans = 0
        while right < len(odds) - 1:
            if k == right - left + 1:
                ans += (odds[left] - odds[left - 1]) * (odds[right + 1] - odds[right])
                left += 1
            right += 1
        return ans


print(Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
