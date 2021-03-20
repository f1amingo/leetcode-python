# 字符串s是否匹配模式p
# . 匹配任意单字符
# * 匹配零或多个前面的那一个元素

# dp[i][j]: s[:i+1]能否匹配p[:j+1]
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True  # 空匹配空
        # 初始化：
        # 1.s, p均为空可以匹配
        # 2.s为空，p不空，可能匹配（a*b*c*）
        # 3.s不空，p为空，绝对不能匹配
        # p能否匹配掉空的s('')
        for j in range(1, m + 1):
            f[0][j] = p[j - 1] == '*' and f[0][j - 2]

        for i in range(1, n + 1):
            # 正则至少要有一个
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    # 'p[j-2]*'匹配零次
                    if f[i][j - 2]:
                        f[i][j] = True
                    # p[j-2]再匹配一次s[i-1]
                    elif s[i - 1] == p[j - 2] and f[i - 1][j]:
                        f[i][j] = True
                    # p[j-2]可匹配任意
                    elif p[j - 2] == '.' and f[i - 1][j]:
                        f[i][j] = True
                else:
                    # p[j-1]匹配掉s[i-1]
                    if s[i - 1] == p[j - 1] and f[i - 1][j - 1]:
                        f[i][j] = True
                    # p[j-1]可匹配任意，匹配掉s[i-1]
                    if p[j - 1] == '.' and f[i - 1][j - 1]:
                        f[i][j] = True
        return f[n][m]

    # def isMatch(self, s: str, p: str) -> bool:
    #     n, m = len(s), len(p)
    #     f = [[False] * (m + 1) for _ in range(n + 1)]
    #     f[0][0] = True  # 空匹配空
    #     for i in range(n + 1):
    #         # 正则至少要有一个
    #         for j in range(1, m + 1):
    #             if p[j - 1] == '*':
    #                 # 'p[j-2]*'匹配零次
    #                 if f[i][j - 2]:
    #                     f[i][j] = True
    #                 # 下标检查
    #                 # p[j-2]再匹配一次s[i-1]
    #                 elif i > 0 and s[i - 1] == p[j - 2] and f[i - 1][j]:
    #                     f[i][j] = True
    #                 # p[j-2]可匹配任意
    #                 elif p[j - 2] == '.' and f[i - 1][j]:
    #                     f[i][j] = True
    #             else:
    #                 # 下标检查
    #                 # p[j-1]匹配掉s[i-1]
    #                 if i > 0 and s[i - 1] == p[j - 1] and f[i - 1][j - 1]:
    #                     f[i][j] = True
    #                 # 下标检查
    #                 # p[j-1]可匹配任意，匹配掉s[i-1]
    #                 if i > 0 and p[j - 1] == '.' and f[i - 1][j - 1]:
    #                     f[i][j] = True
    #     return f[n][m]


assert not Solution().isMatch('', '.b*')
assert not Solution().isMatch('', '.')
assert Solution().isMatch('', '.*')
assert Solution().isMatch('ab', '.*')
assert Solution().isMatch('aa', 'a*')
assert not Solution().isMatch('aa', 'a')
