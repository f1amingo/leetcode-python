class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        size = len(digits)
        flag = 1
        for i in range(size - 1, -1, -1):
            digits[i] += flag
            flag = digits[i] // 10
            digits[i] = digits[i] % 10
            if flag == 0:
                break
        if flag == 1:
            digits.insert(0, 1)
        return digits


print(Solution().plusOne([]))
print(Solution().plusOne([9, 9, 9, 9]))
