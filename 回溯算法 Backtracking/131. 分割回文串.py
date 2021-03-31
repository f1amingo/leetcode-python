from typing import List


# 回溯部分基本没有变化余地，关键在于如何判断子串是否回文，两种方法：
# 1.常规方法，每次使用“两边夹”，O(n)
# 2.动态规划，提前算出结果，之后判断只用O(1)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # 根据依赖关系，倒序
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i + 1 < 4:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        def dfs(start: int, cur_list: List):
            if start == n:
                res.append(cur_list.copy())
                return
            for end in range(start + 1, n + 1):
                if dp[start][end - 1]:
                    cur_list.append(s[start:end])
                    dfs(end, cur_list)
                    cur_list.pop()

        n = len(s)
        res = []
        dfs(0, [])
        return res

    # def partition(self, s: str) -> List[List[str]]:
    #     # 在原字符串上判断，避免提前创建子串的额外开销
    #     def is_palindrome(_s: str, start: int, end: int) -> bool:
    #         while start < end and _s[start] == _s[end]:
    #             start += 1
    #             end -= 1
    #         return _s[start] == _s[end]
    #
    #     def dfs(start: int, cur_list: List):
    #         if start == n:
    #             res.append(cur_list.copy())
    #             return
    #         for end in range(start + 1, n + 1):
    #             if is_palindrome(s, start, end - 1):
    #                 cur_list.append(s[start:end])
    #                 dfs(end, cur_list)
    #                 cur_list.pop()
    #
    #     n = len(s)
    #     res = []
    #     dfs(0, [])
    #     return res


print(Solution().partition("abbab"))
# print(Solution().partition(''))
# print(Solution().partition('a'))
# print(Solution().partition('aa'))
# print(Solution().partition('aab'))
