from typing import List


# 1.遍历，每碰到一个字母c，把原结果分别加上大写和小写的c；
# 2.递归，思路同上
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(start: int):
            if start == n:
                res.append(''.join(s_list))
                return
            # 无论如何，都要向下先走
            dfs(start + 1)
            # 如果是字母，向下多走一条路
            if s_list[start].isalpha():
                s_list[start] = s_list[start].lower() if s_list[start].isupper() else s_list[start].upper()
                dfs(start + 1)

        res = []
        n = len(S)
        s_list = list(S)
        dfs(0)
        return res

    # def letterCasePermutation(self, S: str) -> List[str]:
    #     res = ['']
    #     for c in S:
    #         if c.isalpha():
    #             tmp = []
    #             for r in res:
    #                 tmp.append(r + c.lower())
    #                 tmp.append(r + c.upper())
    #             res = tmp
    #         else:
    #             res = [r + c for r in res]
    #     return res


print(Solution().letterCasePermutation('123'))
print(Solution().letterCasePermutation('3z4'))
print(Solution().letterCasePermutation('a1b2'))
