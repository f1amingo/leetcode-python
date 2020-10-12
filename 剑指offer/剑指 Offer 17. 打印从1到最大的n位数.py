from typing import List


# 考虑大数问题，这将是一个不easy的问题
# 1.不考虑大数，一个for循环解决；
# 2.字符串加法；
# 3.数字全排列；
class Solution:

    def printNumbers(self, n: int) -> List[int]:
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        cur = []
        res = []

        def dfs(idx: int):
            if idx == 0:
                res.append(int(''.join(cur)))
                return
            for digit in digits:
                cur.append(digit)
                dfs(idx - 1)
                cur.pop()

        dfs(n)
        # 把0剔除
        return res[1:]

    # 方法一
    # def printNumbers(self, n: int) -> List[int]:
    #     return [x for x in range(1, 10 ** n)]


print(Solution().printNumbers(1))
print(Solution().printNumbers(2))
