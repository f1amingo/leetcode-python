from typing import List


class Solution:
    # 从[1, n]中猜一个数，再遍历一遍原数组
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        lt, rt = 1, n
        while lt < rt:
            mid = (lt + rt) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                rt = mid
            else:
                lt = mid + 1
        return lt


assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2
assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3
