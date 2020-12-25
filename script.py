from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for a in range(n - 2):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            b, c = a + 1, n - 1
            while b < c:
                tmp = nums[a] + nums[b] + nums[c]
                if tmp == 0:
                    ans.append([nums[a], nums[b], nums[c]])
                if tmp >= 0:
                    c -= 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                if tmp <= 0:
                    b += 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
