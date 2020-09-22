from typing import List


class Solution:
    # O(n^2) 暴力
    # def canThreePartsEqualSum(self, A: List[int]) -> bool:
    #     n = len(A)
    #     if n < 3:
    #         return False
    #     total = sum(A)
    #     left = 0
    #     for i in range(0, n - 2):
    #         # 先加A[i]再用，如果先用再加，
    #         # 就要到下一轮再能被处理，
    #         # 这样最后一个数需要到循环外处理
    #         left += A[i]
    #         right = 0
    #         for j in range(n - 1, i + 1, -1):
    #             right += A[j]
    #             if total - left - right == left == right:
    #                 return True
    #     return False

    # 一个关键信息：三等分，那么每一份就是1/3
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        target, m = divmod(sum(A), 3)
        if m != 0:
            return False
        lt_sum = 0
        for i in range(n):
            lt_sum += A[i]
            if lt_sum == target:
                break
        if lt_sum != target:
            return False
        rt_sum = 0
        for j in range(n - 1, i + 1, -1):
            rt_sum += A[j]
            if rt_sum == target:
                return True
        return False


assert Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
assert not Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])
assert Solution().canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4])
