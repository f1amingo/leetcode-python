import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = collections.Counter(J)
        count = 0
        for s in S:
            if s in jewels:
                count += 1
        return count

