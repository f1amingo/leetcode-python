from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        found = {}
        for num in nums1:
            found[num] = found.get(num, 0) + 1
        res = []
        for num in nums2:
            if found.get(num) > 0:
                res.append(num)
                found[num] -= 1
        return res
