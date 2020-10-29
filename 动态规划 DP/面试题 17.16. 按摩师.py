from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            a, b = b, max(a + num, b)
        return b


print(Solution().massage([1, 2, 3, 1]))
print(Solution().massage([]))
print(Solution().massage([2, 7, 9, 3, 1]))
print(Solution().massage([2, 1, 4, 5, 3, 1, 1, 3]))
