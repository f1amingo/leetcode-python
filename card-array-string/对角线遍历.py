class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        M = len(matrix) - 1
        if M == -1:
            return []
        N = len(matrix[0]) - 1
        if N == -1:
            return []
        up = True
        i = 0
        j = 0
        res = []
        while True:
            res.append(matrix[i][j])
            if i == M and j == N:
                break
            if up:
                if i == 0 or j == N:
                    if j == N:
                        i += 1
                    else:
                        j += 1
                    up = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == M or j == 0:
                    if i == M:
                        j += 1
                    else:
                        i += 1
                    up = True
                else:
                    i += 1
                    j -= 1
        return res


print(Solution().findDiagonalOrder([]))
