from typing import List


class Solution:
    # 考虑每个位置可能的字符
    def permutation(self, s: str) -> List[str]:
        if not s:
            return []
        s_list = list(s)
        end = len(s_list)
        res = []

        def dfs(start):
            if start == end - 1:
                res.append(''.join(s_list))
                return
            # 这里只能使用set判断重复
            # 如果排序的话，每次一交换又没有顺序了
            dic = set()
            for i in range(start, end):
                if s_list[i] in dic:
                    continue
                dic.add(s_list[i])
                s_list[start], s_list[i] = s_list[i], s_list[start]
                dfs(start + 1)
                s_list[i], s_list[start] = s_list[start], s_list[i]

        dfs(0)
        return res


print(Solution().permutation("abb"))
