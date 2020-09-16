from typing import List


class Solution:
    # 1. 英文字母可以用数组处理，因为只有26位
    # 2.
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(p: str) -> str:
            if equal_set[p] != p:
                equal_set[p] = find(equal_set[p])
            return equal_set[p]

        def union(p: str, q: str):
            pRoot, qRoot = find(p), find(q)
            # 这里其实可以不要
            # if pRoot == qRoot:
            #     return
            equal_set[pRoot] = qRoot

        equal_set = {}
        non_equal_set = {}

        # 数组元素是数组，可以直接解构赋值
        for p, a, b, q in equations:
            # p, a, b, q = eq
            if p not in equal_set:
                equal_set[p] = p
            if q not in equal_set:
                equal_set[q] = q
            if a == '!':
                li = non_equal_set.get(p, [])
                li.append(q)
                non_equal_set[p] = li
            else:
                union(p, q)

        for _key in non_equal_set:
            for _ele in non_equal_set[_key]:
                pRoot, qRoot = find(_key), find(_ele)
                if pRoot == qRoot:
                    return False
        return True


print(Solution().equationsPossible(["c==c", "b==d", "x!=z"]))
assert not Solution().equationsPossible(["a==b", "b!=a"])
assert Solution().equationsPossible(["b==a", "a==b"])
assert Solution().equationsPossible(["a==b", "b==c", "a==c"])
assert not Solution().equationsPossible(["a==b", "b!=c", "c==a"])
