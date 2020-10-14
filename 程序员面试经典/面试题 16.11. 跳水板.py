from typing import List


class Solution:
    # 两种边界情况
    # 1.k==0
    # 2.shorter==longer
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        res = []
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        for i in range(k + 1):
            res.append(shorter * (k - i) + longer * i)
        return res

    # 超时 O(2^n)
    # def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
    #     if k == 0:
    #         return []
    #
    #     def dfs(down_k: int, cur_len: int):
    #         if down_k == 0:
    #             res.add(cur_len)
    #             return
    #         dfs(down_k - 1, cur_len + shorter)
    #         dfs(down_k - 1, cur_len + longer)
    #
    #     res = set()
    #     dfs(k, 0)
    #     return list(res)


print(Solution().divingBoard(1, 1, 100000))
print(Solution().divingBoard(1, 2, 3))
print(Solution().divingBoard(1, 2, 0))
