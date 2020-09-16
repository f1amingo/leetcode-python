from collections import defaultdict
from typing import List


class Solution:

    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        def find(p: str) -> str:
            if dict_names[p] != p:
                dict_names[p] = find(dict_names[p])
            return dict_names[p]

        def union(p: str, q: str):
            pRoot, qRoot = find(p), find(q)
            if pRoot < qRoot:
                dict_names[qRoot] = pRoot
            else:
                dict_names[pRoot] = qRoot

        dict_names, dict_times = {}, {}
        for name_times in names:
            left_parentheses = name_times.index('(')
            name, times = name_times[:left_parentheses], int(name_times[left_parentheses + 1:-1])
            dict_names[name], dict_times[name] = name, times
        for synonym in synonyms:
            name1, name2 = synonym[1:-1].split(',')
            if name1 not in dict_names or name2 not in dict_names:
                continue
            union(name1, name2)
        res_map, res = defaultdict(int), []
        for name, freq in dict_times.items():
            res_map[find(name)] += freq
        return ['%s(%d)' % (k, v) for k, v in res_map.items() if v]

    # 顺序会影响结果，下面这种方法顺序不对
    # def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
    #     def find(p: str) -> str:
    #         if dict_names[p] != p:
    #             dict_names[p] = find(dict_names[p])
    #         return dict_names[p]
    #
    #     def union(p: str, q: str):
    #         pRoot, qRoot = find(p), find(q)
    #         if pRoot < qRoot:
    #             dict_names[qRoot] = pRoot
    #             dict_times[pRoot] += dict_times[qRoot]
    #             dict_times[qRoot] = 0
    #         else:
    #             dict_names[pRoot] = qRoot
    #             dict_times[qRoot] += dict_times[pRoot]
    #             dict_times[pRoot] = 0
    #
    #     dict_names, dict_times = {}, {}
    #     for name_times in names:
    #         left_parentheses = name_times.index('(')
    #         name, times = name_times[:left_parentheses], int(name_times[left_parentheses + 1:-1])
    #         dict_names[name], dict_times[name] = name, times
    #     for synonym in synonyms:
    #         name1, name2 = synonym[1:-1].split(',')
    #         if name1 not in dict_names or name2 not in dict_names:
    #             continue
    #         union(name1, name2)
    #
    #     return ['%s(%d)' % (k, v) for k, v in dict_times.items() if v]

    # 对于下面这样的输入，该方法会当成一个名字
    # ["Johnny(15)", "Jon(12)"]
    # ["(Jon,John)", "(John,Johnny)"]
    # def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
    #     def find(p: str) -> str:
    #         if dict_names[p] != p:
    #             dict_names[p] = find(dict_names[p])
    #         return dict_names[p]
    #
    #     def union(p: str, q: str):
    #         pRoot, qRoot = find(p), find(q)
    #         dict_names[qRoot] = pRoot
    #         dict_times[pRoot] += dict_times[qRoot]
    #         dict_times[qRoot] = 0
    #
    #     dict_names, dict_times = {}, {}
    #     for name_times in names:
    #         left_parentheses = name_times.index('(')
    #         name, times = name_times[:left_parentheses], int(name_times[left_parentheses + 1:-1])
    #         dict_names[name], dict_times[name] = name, times
    #     for synonym in synonyms:
    #         name1, name2 = synonym[1:-1].split(',')
    #         if name1 not in dict_names:
    #             dict_names[name1] = name1
    #             dict_times[name1] = 0
    #         if name2 not in dict_names:
    #             dict_names[name2] = name2
    #             dict_times[name2] = 0
    #         name1, name2 = min(name1, name2), max(name1, name2)
    #         union(name1, name2)
    #
    #     return ['%s(%d)' % (k, v) for k, v in dict_times.items() if v]


names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
print(Solution().trulyMostPopular(names, synonyms))
