from typing import List


class Solution:
    def constructArr(self, A: List[int]) -> List[int]:
        n = len(A)
        to_right, to_left = [0] * n, [0] * n
        ans = [0] * n
        for i in range(n):
            if i == 0:
                to_right[i] = 1
            else:
                to_right[i] = to_right[i - 1] * A[i - 1]
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                to_left[i] = 1
            else:
                to_left[i] = to_left[i + 1] * A[i + 1]
        for i in range(n):
            ans[i] = to_left[i] * to_right[i]
        return ans


assert Solution().constructArr([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
