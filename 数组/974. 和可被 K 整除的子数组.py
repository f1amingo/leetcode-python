from typing import List


class Solution:
    # 暴力超时
    # def subarraysDivByK(self, A: List[int], K: int) -> int:
    #     pre = [0] * len(A)
    #     cur_sum = 0
    #     res = 0
    #     for i in range(len(pre)):
    #         cur_sum += A[i]
    #         pre[i] = cur_sum
    #         if pre[i] % K == 0:
    #             res += 1
    #         for j in range(i):
    #             if (pre[i] - pre[j]) % K == 0:
    #                 res += 1
    #     return res

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        pre = {0: 1}  # mod 0 为 1
        cur_sum = 0
        res = 0
        for num in A:
            cur_sum += num
            mod = cur_sum % K
            res += pre.get(mod, 0)
            pre[mod] = pre.get(mod, 0) + 1
        return res


print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
