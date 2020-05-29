from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        sum = 0
        for num in nums:
            sum ^= num
        flag = sum & (-sum)
        # flag = sum ^ (sum - 1) & sum
        res = [0, 0]
        for num in nums:
            if (num & flag) == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res


print(Solution().singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
