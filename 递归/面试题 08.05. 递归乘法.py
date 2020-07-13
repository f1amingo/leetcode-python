from typing import List


class Solution:
    def multiply(self, A: int, B: int) -> int:
        # # 无记忆递归
        # # 大量重复计算，相当慢
        # if not A or not B:
        #     return 0
        # if A == 1:
        #     return B
        # if B == 1:
        #     return A
        # if A < B:
        #     return self.multiply(A // 2, B) + self.multiply(A - A // 2, B)
        # else:
        #     return self.multiply(A, B // 2) + self.multiply(A, B - B // 2)

        # 记忆化递归，不知道为什么还是很慢T_T
        # if not A or not B:
        #     return 0
        #
        # def helper(A: int, B: int, memo: List) -> int:
        #     if A == 1:
        #         return B
        #     if B == 1:
        #         return A
        #     a = A // 2
        #     b = A - a
        #     if not memo[a]:
        #         memo[a] = helper(a, B, memo)
        #     if not memo[b]:
        #         memo[b] = helper(b, B, memo)
        #     return memo[a] + memo[b]
        #
        # if A <= B:
        #     return helper(A, B, [0] * (A // 2 + 2))
        # else:
        #     return helper(B, A, [0] * (B // 2 + 2))

        # 看着别人的改写的，怎么还是很慢
        # if not A or not B:
        #     return 0
        # if A >= B:
        #     return A + self.multiply(A, B - 1)
        # else:
        #     return B + self.multiply(A - 1, B)

        # 别人的为什么很快。。
        if A < B: A, B = B, A
        return 0 if B <= 0 else (A + self.multiply(A, B - 1))


print(Solution().multiply(4, 1))
