from typing import List


# 思想类似动态规划，关键在于递推；
# 在上一步结果中，每一项的左边（或者右边）放一个1或0，都满足只有一位不同的要求；
# 证明：假设上一步结果中，连续两项abc、adc，变化后为abc0(abc1)、adc0(adc1)，显然变化后的连续两项只有一位不同；
# 如何将拼0和1的结果，组合起来呢？
# 关键在于连接处，我们可以将abc0和abc1放到一起，逆序就可以实现这一目的；
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res)):
                res[j] <<= 1
            rev = list(reversed(res))
            for j in range(len(rev)):
                rev[j] += 1
            res += rev
        return res


print(Solution().grayCode(1))
print(Solution().grayCode(2))
