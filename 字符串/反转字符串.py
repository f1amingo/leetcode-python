class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s)-1)

    def reverse(self, s, begin, end):
        if begin >= end:
            return
        s[begin], s[end] = s[end], s[begin]
        self.reverse(s, begin + 1, end - 1)


arr = []
Solution().reverseString(arr)
print(arr)
