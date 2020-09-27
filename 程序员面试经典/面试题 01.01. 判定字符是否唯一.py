# 一些常识：26个英文字母，128个ASCII字符，256个扩展ASCII字符
# 字符类型：ASCII字符串还是Unicode字符串
# 方法：
# 1.使用bool数组/dict/set；
# 2.bit vector；
# 3.双重循环；
# 4.排序后比较相邻字符（会修改字符串）；
class Solution:
    # 位运算，使用一个int来存储
    # 面试时，需要确定字符范围
    def isUnique(self, astr: str) -> bool:
        # !!!增加一个优化
        # 这步很加分
        if len(astr) > 26:
            return False
        flag = 0
        for c in astr:
            move_bit = ord(c) - ord('a')
            moved = 1 << move_bit
            if flag & moved > 0:
                return False
            flag = flag | moved
        return True

        # 常规思路，使用散列表
    # def isUnique(self, astr: str) -> bool:
    #     dic = {}
    #     for c in astr:
    #         if c in dic:
    #             return False
    #         dic[c] = 1
    #     return True


assert not Solution().isUnique('leetcode')
assert Solution().isUnique('abc')
assert Solution().isUnique('')
assert Solution().isUnique('a')
