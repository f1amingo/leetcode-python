from typing import List


# m x n，是否存在目标值
# 从左到右升序
# 每行第一个数大于前一行最后一个整数
class Solution:
    # 二分法，将矩阵flatten为一个一位数组
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            # 矩阵索引i, j和一维数组索引间的对应关系
            i, j = divmod(mid, n)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False

    # 右上角作为BST的根
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     if not matrix or not matrix[0]:
    #         return False
    #     m, n = len(matrix), len(matrix[0])
    #     i, j = 0, n - 1
    #     while i < m and j > -1:
    #         if target == matrix[i][j]:
    #             return True
    #         elif target < matrix[i][j]:
    #             j -= 1
    #         else:
    #             i += 1
    #     return False


assert not Solution().searchMatrix([
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 13)
