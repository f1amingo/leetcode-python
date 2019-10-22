class Solution(object):
    # 暴力
    def intersect0(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for n1 in nums1:
            if n1 in nums2:
                res.append(n1)
                nums2.remove(n1)
        return res

    # 为优using map
    def intersect1(self, nums1, nums2):
        lookup = {}
        for num in nums1:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        res = []
        for num in nums2:
            if num in lookup:
                res.append(num)
                lookup[num] -= 1
                if not lookup[num]:
                    lookup.pop(num)
        return res

    # 为优using map get() with default value
    def intersect2(self, nums1, nums2):
        lookup = {}
        for num in nums1:
            lookup[num] = lookup.get(num, 0) + 1
        res = []
        for num in nums2:
            if lookup.get(num, 0):
                res.append(num)
                lookup[num] -= 1
        return res

    # 为优sort two pointer
    def intersect3(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res


print(Solution().intersect3([1, 2, 2, 1], [2, 2]))
