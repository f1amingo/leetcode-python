from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        size = n * n
        ans = [[0] * n for _ in range(n)]
        num = 1
        l, t, r, b = 0, 0, n - 1, n - 1
        while num <= size:
            for i in range(l, r + 1):
                ans[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):
                ans[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                ans[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):
                ans[i][l] = num
                num += 1
            l += 1
        return ans


print(Solution().generateMatrix(3))
