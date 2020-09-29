class Solution:
    # 本质：寻找一个切割点，使得两个字符串分别为xy和yx的形式
    # 拼接自身这个操作好好学学！
    # 凡是字符串，考虑空串！！！
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True
        n = len(s1)
        if n != len(s2):
            return False
        double_s1 = s1 + s1
        for i in range(n):
            if double_s1[i:i + n] == s2:
                return True
        return False


print(Solution().isFlipedString('', ''))
print(Solution().isFlipedString('waterbottle', 'erbottlewat'))
