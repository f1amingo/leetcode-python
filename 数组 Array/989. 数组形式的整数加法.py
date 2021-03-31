from typing import List


# 返回A+K的数组形式
# 长度可能变化
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        i, n = 0, len(A)
        carry = 0
        while K or carry:
            if i == n:
                # 扩容
                A = [0] + A
                n += 1
            K, mod = divmod(K, 10)
            val = mod + A[n - i - 1] + carry
            carry, val = divmod(val, 10)
            A[n - i - 1] = val
            i += 1
        return A


assert Solution().addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]
assert Solution().addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert Solution().addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4]
