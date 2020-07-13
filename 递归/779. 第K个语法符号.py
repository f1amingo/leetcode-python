class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # 超时
        # if N <= 2:
        #     return [0, 1][K - 1]
        # s = [0] * (2 ** (N - 1))
        # s[1] = 1
        # n = 2
        # for i in range(2, N):
        #     n *= 2
        #     for j in range(n // 2, n, 2):
        #         if s[j // 2] == 1:
        #             s[j], s[j + 1] = 1, 0
        #         else:
        #             s[j], s[j + 1] = 0, 1
        # return s[K - 1]

        def helper(n, k):
            if n == 1:
                return 0
            return [[0, 1], [1, 0]][helper(n - 1, k // 2)][k % 2]

        return helper(N, K - 1)


print(Solution().kthGrammar(4, 5))
