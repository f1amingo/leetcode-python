class Solution(object):
    # 思路：判断是在上中下左中的哪一边，然后进行相应操作
    # 错误：左上点、右下点，与行号、列号的对应关系出错
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        size_m = len(matrix)
        if size_m == 0:
            return []
        size_n = len(matrix[0])
        if size_n == 0:
            return []
        for_times = size_m * size_n
        action_index = 0
        top_left = [0, 0]
        bottom_right = [size_m - 1, size_n - 1]
        i = j = 0
        res = []
        for time in range(0, for_times):
            res.append(matrix[i][j])
            mod = action_index % 4
            # 上
            if mod == 0:
                if j < bottom_right[1]:
                    j += 1
                elif j == bottom_right[1]:
                    action_index += 1
                    top_left[0] += 1
                    i += 1
            # 右
            elif mod == 1:
                if i < bottom_right[0]:
                    i += 1
                elif i == bottom_right[0]:
                    action_index += 1
                    bottom_right[1] -= 1
                    j -= 1
            # 下
            elif mod == 2:
                if j > top_left[1]:
                    j -= 1
                elif j == top_left[1]:
                    action_index += 1
                    bottom_right[0] -= 1
                    i -= 1
            # 左
            elif mod == 3:
                if i > top_left[0]:
                    i -= 1
                elif i == top_left[0]:
                    action_index += 1
                    top_left[1] += 1
                    j += 1
        return res


print(Solution().spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]))
