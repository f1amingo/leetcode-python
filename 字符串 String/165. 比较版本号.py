class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i = j = 0
        while i < m or j < n:
            i_start, j_start = i, j
            # 找到下一个dot
            while i < m:
                if version1[i] == '.':
                    break
                i += 1
            while j < n:
                if version2[j] == '.':
                    break
                j += 1
            # 去除前导零
            while i_start < i and version1[i_start] == '0':
                i_start += 1
            while j_start < j and version2[j_start] == '0':
                j_start += 1
            # 先比长度，再比大小
            i_len, j_len = i - i_start, j - j_start
            if i_len > j_len or (i_len == j_len and version1[i_start:i] > version2[j_start:j]):
                return 1
            if i_len < j_len or (i_len == j_len and version1[i_start:i] < version2[j_start:j]):
                return -1
            i += 1
            j += 1

        # 二者长度不同时，如果长的那个剩余部分中含有非零，则更大
        for k in range(i, m):
            if version1[k] == '.' or version1[k] == '0':
                continue
            else:
                return 1
        for k in range(j, n):
            if version1[k] == '.' or version1[k] == '0':
                continue
            else:
                return -1
        return 0


assert Solution().compareVersion("1.01", "1.001") == 0
assert Solution().compareVersion("7.5.2.4", "7.5.3") == -1
assert Solution().compareVersion("0.1", "1.1") == -1
assert Solution().compareVersion("1.0.1", "1") == 1
