from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        if not S:
            return []
        s_list = list(S)
        s_list.sort()

        def dfs(i: int):
            if i == n:
                res.append(''.join(s_list.copy()))
                return
            for j in range(i, n):
                # s_list[j - 1] == s_list[j] 判断前一位是否被使用
                # s_list[i] == s_list[j] 交换过后，整体不再有序
                # 比如：aabc，c打头时，有caba，dfs(1)时，不能再交换两个相同的a

                # if j > i and (s_list[j - 1] == s_list[j]):
                if j > i and (s_list[j - 1] == s_list[j] or s_list[i] == s_list[j]):
                    continue
                s_list[i], s_list[j] = s_list[j], s_list[i]
                dfs(i + 1)
                s_list[i], s_list[j] = s_list[j], s_list[i]

        n = len(S)
        res = []
        dfs(0)
        return res


print(Solution().permutation('aabc'))
print(Solution().permutation('abbcd'))
# print(Solution().permutation("jawaLR"))
print(Solution().permutation('ab'))
