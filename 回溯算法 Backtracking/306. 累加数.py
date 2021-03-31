class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(a: int, b: int, c: int) -> bool:
            # 递归边界
            if c == n:
                return True
            num1 = int(num[a:b])
            num2 = int(num[b:c])
            # 如果考虑大数问题，换成字符串加
            the_sum = str(num1 + num2)
            len_sum = len(the_sum)
            # 先比长度
            if c + len_sum > n:
                return False
            # 逐位比较
            for i in range(len_sum):
                if num[c + i] != the_sum[i]:
                    return False
            # 比较下一位数
            return dfs(b, c, c + len_sum)

        n = len(num)
        if n < 3:
            return False
        for b in range(1, n - 1):
            # 第一个数前导零
            if b > 1 and num[0] == '0':
                break
            for c in range(b + 1, n):
                # 第二个数前导零
                if c > b + 1 and num[b] == '0':
                    break
                if dfs(0, b, c):
                    return True
        return False


print(Solution().isAdditiveNumber("0123"))
print(Solution().isAdditiveNumber("1023"))
print(Solution().isAdditiveNumber("112358"))
print(Solution().isAdditiveNumber("199100199"))
