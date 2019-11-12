class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in res:
                res[sorted_str].append(string)
            else:
                res[sorted_str] = [string]
        return [res[key] for key in res]


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
