class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        i = j = 0
        n = len(S)
        res = ''
        while i < n and j < n:
            if S[i] != S[j]:
                res += S[i] + str((j - i))
                i = j
            j += 1
        res += S[i] + str((j - i))
        if len(res) < len(S):
            return res
        return S


print(Solution().compressString("abbccd"))
