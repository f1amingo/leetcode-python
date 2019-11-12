class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 字符排序确定异位词
        # res = {}
        # for string in strs:
        #     sorted_str = ''.join(sorted(string))
        #     if sorted_str in res:
        #         res[sorted_str].append(string)
        #     else:
        #         res[sorted_str] = [string]
        # return [res[key] for key in res]

        # 统计出现次数确定异位词
        # res = {}
        # for string in strs:
        #     statis = [0] * 26
        #     for ch in string:
        #         statis[ord(ch) - ord('a')] += 1
        #     tuple_key = tuple(statis)
        #     if tuple_key in res:
        #         res[tuple_key].append(string)
        #     else:
        #         res[tuple_key] = [string]
        # return [val for key, val in res.items()]

        # 官方题解
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            ans[tuple(counts)].append(s)
        return ans.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
