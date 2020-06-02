from typing import List


class Solution:
    # My solution
    # def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    #     m = max(candies)
    #     ans = [False] * len(candies)
    #     for i, ca in enumerate(candies):
    #         if m - ca <= extraCandies:
    #             ans[i] = True
    #     return ans

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [candy + extraCandies >= m for candy in candies]


print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))
print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))
