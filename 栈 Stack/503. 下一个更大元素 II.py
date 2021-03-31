from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk, ans = [], [-1] * n
        for i in range(2 * n - 1):
            idx = i % n
            while stk and nums[idx] > nums[stk[-1]]:
                tmp = stk.pop()
                if ans[tmp] == -1:
                    ans[tmp] = nums[idx]
            stk.append(idx)
        return ans


assert Solution().nextGreaterElements([1, 2, 1]) == [2, -1, 2]
