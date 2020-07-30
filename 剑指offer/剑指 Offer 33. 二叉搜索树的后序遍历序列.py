from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def verify(i: int, j: int) -> bool:
            # >代表上一级没有左右子树的情况
            if i >= j:
                return True
            # m可不可能没有赋值（没有进入循环）
            # 不可能，走到这里说明一定有 i<j
            for m in range(i, j + 1):
                if postorder[m] > postorder[j]:
                    break
            # 同上，这个循环是否一定会进入
            # 上一步中m一定被赋值，并且m的最大值为j
            # 所以这里至少会循环一次
            for k in range(m, j + 1):
                if postorder[k] <= postorder[j]:
                    break
            return k == j and verify(i, m - 1) and verify(m, j - 1)

        return verify(0, len(postorder) - 1)


print(Solution().verifyPostorder([1, 6, 3, 2, 5]))
