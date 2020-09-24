class Solution:
    # 类似切片，不过使用一个list
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        # 求余简化代码
        for i in range(n, len(s) + n):
            res.append(s[i % len(s)])
        return ''.join(res)

    # 原地 局部反转+整体反转
    # 对于非字符串常量，可以原地进行
    # def reverseLeftWords(self, s: str, n: int) -> str:
    #     return (s[:n][::-1] + s[n:][::-1])[::-1]

    # my solution
    # 切片
    # def reverseLeftWords(self, s: str, n: int) -> str:
    #     # n = n % len(s)  # 题目说1<=k<len(s)
    #     return s[n:] + s[:n]


print(Solution().reverseLeftWords('abcdefg', 2))
