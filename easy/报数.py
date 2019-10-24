class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        if n == 1:
            return res
        for _ in range(n - 1):
            tmp = ''
            count = 1
            for i in range(1, len(res)):
                if res[i] != res[i - 1]:
                    tmp += str(count) + res[i - 1]
                    count = 1
                else:
                    count += 1
            tmp += str(count) + res[-1]
            res = tmp
        return res


print(Solution().countAndSay(1))
print(Solution().countAndSay(2))
print(Solution().countAndSay(3))
print(Solution().countAndSay(4))
print(Solution().countAndSay(5))
