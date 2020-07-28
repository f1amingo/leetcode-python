# -*- coding:utf-8 -*-

# 运行时间：371ms
# 占用内存：5732k
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         for clist in array:
#             for i in clist:
#                 if i == target:
#                     return True
#         return False


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        len1 = len(array[0])
        ptr1 = 0
        ptr2 = len1 - 1
        cindex = 0
        while ptr1 < ptr2:
            cindex = int((ptr1 + ptr2) / 2)
            if array[cindex][0] == target:
                return True
            elif array[cindex][len1 - 1] < target:
                ptr1 = cindex + 1
            elif array[cindex][0] > target:
                ptr2 = cindex - 1
        print(ptr1, ptr2)
        cindex = ptr1
        p1 = 0
        p2 = len1 - 1
        while p1 <= p2:
            c = int((p1 + p2) / 2)
            if array[cindex][c] == target:
                return True
            elif array[cindex][c] < target:
                p1 = c + 1
            elif array[cindex][c] > target:
                p2 = c - 1
        return False


if __name__ == '__main__':
    solution = Solution()
    array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = solution.Find(0, array_2d)
    print(res)
