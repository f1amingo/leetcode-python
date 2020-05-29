class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        reverse_num = 0
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x = int(x / 10)
        return x == reverse_num or x == int(reverse_num / 10)


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
