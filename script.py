from typing import List


class Solution:
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


print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(Solution().numberOfSubarrays([2, 4, 6], 1))
print(Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution().numberOfSubarrays([1], 1))
