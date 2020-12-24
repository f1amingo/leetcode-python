from typing import List


class Solution:
    def search(self, A: List[int], target: int) -> int:
        if not A:
            return -1
        lt, rt = 0, len(A) - 1
        while lt < rt:
            mid = (lt + rt) // 2
            if A[lt] <= A[mid]:
                if A[lt] <= target <= A[mid]:
                    rt = mid
                else:
                    lt = mid + 1
            else:
                if A[mid] <= target <= A[rt]:
                    lt = mid
                else:
                    rt = mid - 1

        return lt if A[lt] == target else -1


assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert Solution().search([1], 0) == -1
assert Solution().search([5, 1, 3], 1) == 1
