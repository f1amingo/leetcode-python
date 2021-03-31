from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = [False] * len(A)
        cur = 0
        for i in range(len(A)):
            cur = cur * 2 + A[i]
            ans[i] = cur % 5 == 0
        return ans


assert Solution().prefixesDivBy5([0, 1, 1]) == [True, False, False]
