from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd_list = []
        for i in range(n):
            if nums[i] & 1 == 1:
                odd_list.append(i)
        odd_n = len(odd_list)
        ans = 0
        for right in range(k - 1, odd_n):
            left = right - k + 1
            left_count = odd_list[left] + 1 if left == 0 else odd_list[left] - odd_list[left - 1]
            right_count = n - odd_list[right] if right == odd_n - 1 else odd_list[right + 1] - odd_list[right]
            ans += left_count * right_count
        return ans


print(Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
