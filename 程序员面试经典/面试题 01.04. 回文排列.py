class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        found = {}
        odd_count = 0
        for ch in s:
            tmp = found.get(ch, 0)
            if tmp % 2 == 0:
                odd_count += 1
            else:
                odd_count -= 1
            found[ch] = tmp + 1
        return odd_count < 2


print(Solution().canPermutePalindrome('tactcoa'))
