from typing import List


# 这类题思路怎么来？
# 你自己手写一遍，然后模拟，入口就是依次考虑各个字母打头
class Solution:
    def permutation(self, S: str) -> List[str]:
        if not S:
            return []

        def dfs(cur_list: List, idx: int):
            if idx == n:
                res.append(''.join(cur_list.copy()))
                return
            for i in range(idx, n):
                # 交换位置
                cur_list[idx], cur_list[i] = cur_list[i], cur_list[idx]
                dfs(cur_list, idx + 1)
                # 回溯，复原
                cur_list[idx], cur_list[i] = cur_list[i], cur_list[idx]

        n = len(S)
        res = []
        dfs(list(S), 0)
        return res


print(Solution().permutation('ab'))
print(Solution().permutation('qwe'))
