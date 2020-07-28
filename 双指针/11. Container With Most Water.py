class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        index1, index2 = 0, len(height) - 1
        max_area = 0
        while index1 < index2:
            this_area = min(height[index1], height[index2]) * (index2 - index1)
            max_area = max(this_area, max_area)
            if height[index1] < height[index2]:
                index1 += 1
            else:
                index2 -= 1
        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
