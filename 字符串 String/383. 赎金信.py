from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = Counter(ransomNote)
        dict2 = Counter(magazine)
        for k, v in dict1.items():
            if dict2.get(k, 0) < v:
                return False
        return True


assert not Solution().canConstruct('a', 'b')
assert not Solution().canConstruct('aa', 'ab')
assert Solution().canConstruct('aa', 'aab')
