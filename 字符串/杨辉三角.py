class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(0, numRows):
            clist = []
            for j in range(0, i + 1):
                if i == 0:
                    clist.append(1)
                    break
                if j == 0 or j == i:
                    clist.append(1)
                else:
                    clist.append(res[-1][j - 1] + res[-1][j])
            res.append(clist)
        return res


print(Solution().generate(0))
