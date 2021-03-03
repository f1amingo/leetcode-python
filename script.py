from typing import List


# 出现次数超过一半
# 1. 排序 O(NlogN)
# 2. hash计数 O(N), O(N)
# 3. 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, count = 0, 0
        for num in nums:
            if count == 0:
                ans = num
                count += 1
            else:
                if num == ans:
                    count += 1
                else:
                    count -= 1
        return ans


assert Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]) == 2
