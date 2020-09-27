from collections import Counter

# 需要确定的一些问题：是否区分大小写；是否允许包含空格
# 长度相等是前提，提前判断长度，避免后面白用功
# 1.计数：dict通用；符号范围确定->数组/位向量；
# 2.排序，会修改字符串，当然可以复制一遍；
class Solution:
    # 一个很厉害的位运算写法
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        if len1 != len(s2):
            return False
        result = 0
        for i in range(len1):
            result += 1 << ord(s1[i])
            result -= 1 << ord(s2[i])
        return result == 0

    # 双向排序
    # def CheckPermutation(self, s1: str, s2: str) -> bool:
    #     len1, len2 = len(s1), len(s2)
    #     if len1 != len2:
    #         return False
    #     # 假设只有小写字母
    #     counter = [0] * 26
    #     for i in range(len1):
    #         counter[ord(s1[i]) - ord('a')] += 1
    #         counter[ord(s2[i]) - ord('a')] -= 1
    #     for c in counter:
    #         if c != 0:
    #             return False
    #     return True

    # def CheckPermutation(self, s1: str, s2: str) -> bool:
    #     return sorted(s1) == sorted(s2)

    # def CheckPermutation(self, s1: str, s2: str) -> bool:
    #     return Counter(s1) == Counter(s2)
