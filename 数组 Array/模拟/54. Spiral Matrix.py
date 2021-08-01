class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = -1, m, -1, n
        i, j = 0, -1
        ans = []
        while True:
            while j < right - 1:
                j += 1
                ans.append(matrix[i][j])
            top += 1
            # 边界不能重合
            if top + 1 == bottom: break
            while i < bottom - 1:
                i += 1
                ans.append(matrix[i][j])
            right -= 1
            if left + 1 == right: break
            while j > left + 1:
                j -= 1
                ans.append(matrix[i][j])
            bottom -= 1
            if top + 1 == bottom: break
            while i > top + 1:
                i -= 1
                ans.append(matrix[i][j])
            left += 1
            if left + 1 == right: break
        return ans
