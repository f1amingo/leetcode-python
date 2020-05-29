class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划
        # dp = [i for i in range(n + 1)]
        # for i in range(1, n + 1):
        #     j = 1
        #     while j * j <= i:
        #         dp[i] = min(dp[i], dp[i - j * j] + 1)
        #         j += 1
        # return dp[-1]

        # BFS
        if n == 0:
            return 0
        queue = [n]
        step = 0
        visited = set()
        while queue:
            step += 1
            length = len(queue)
            for _ in range(length):
                tmp = queue.pop()
                for i in range(1, int(tmp ** 0.5) + 1):
                    diff = tmp - i ** 2
                    if diff == 0:
                        return step
                    if diff not in visited:
                        visited.add(diff)
                        queue.insert(0, diff)
        return step


print(Solution().numSquares(12))
