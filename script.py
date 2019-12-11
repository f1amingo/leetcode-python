class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        end = 0

        def helper(left, right):
            nonlocal start, end
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left > end - start:
                start = left
                end = right

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return s[start + 1:end]
