class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        num1 = 1
        num2 = 2
        num = 0
        for i in range(2, n):
            num = num1 + num2
            num1 = num2
            num2 = num
        return num
