class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        head = 0
        tail = len(s) - 1
        while head <= tail:
            if not s[head].isalnum():
                head += 1
                continue
            if not s[tail].isalnum():
                tail -= 1
                continue
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True


print(Solution().isPalindrome(""))
