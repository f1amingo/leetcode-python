from typing import List


# 暴力：O(n^2)，O(n)内可以解决这个问题
# 没有重复元素
# nums1是nums2的子集
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk, greater = [], {}
        for num in nums2:
            while stk and stk[-1] < num:
                greater[stk.pop()] = num
            stk.append(num)
        # while stk:
        #     greater[stk.pop()] = -1
        # return [greater[k] for k in nums1]
        return [greater.get(k, -1) for k in nums1]


assert Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
