from typing import List


class Solution:
    # 双指针，都是正数，所以是递增
    # 保证窗口满足条件的前提下，每次新来一个数X，形成类似ABCX形式
    # 对于ABCX，新增加的子数组为X, CX, BCX, ABCX，正好等于窗口长度
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod, res, lt = 1, 0, 0
        for rt, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[lt]
                lt += 1
            res += rt - lt + 1
        return res


assert Solution().numSubarrayProductLessThanK([1, 2, 3], 0) == 0
assert Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
