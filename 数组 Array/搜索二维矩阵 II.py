class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for clist in matrix:
            left = 0
            right = len(clist)
            while left < right:
                mid = (left + right) // 2
                if clist[mid] == target:
                    return True
                elif clist[mid] > target:
                    right = mid
                else:
                    left = mid + 1
        return False


