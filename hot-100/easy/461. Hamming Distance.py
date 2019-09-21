class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = bin(x ^ y)[2:]
        count = 0
        for char in res:
            if char == '1':
                count += 1
        return count


print(Solution().hammingDistance(4, 2))
