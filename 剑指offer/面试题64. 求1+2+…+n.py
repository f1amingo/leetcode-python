class Solution:
    def __init__(self):
        self._sum = 0

    def sumNums(self, n: int) -> int:
        self._sum += n
        n and self.sumNums(n - 1)
        return self._sum


print(Solution().sumNums(3))
print(Solution().sumNums(9))
