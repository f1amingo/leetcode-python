from typing import List


# 小时和分钟的范围居然算错了！？
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def dfs(idx: int, k: int):
            if idx == 10:
                if k == 0:
                    tmp = format_time()
                    if tmp:
                        res.append(format_time())
                return
            times[idx] = 0
            dfs(idx + 1, k)
            times[idx] = 1
            dfs(idx + 1, k - 1)

        def format_time():
            hour, minute = 0, 0
            for i in range(4):
                hour = hour * 2 + times[i]
            if hour > 11:
                return False
            for j in range(4, 10):
                minute = minute * 2 + times[j]
            if minute > 59:
                return False
            minute = '0' + str(minute) if minute < 10 else str(minute)
            return '%s:%s' % (str(hour), minute)

        times = [0, 0, 0, 0] + [0, 0, 0, 0, 0, 0]
        res = []
        dfs(0, num)
        return res


print(Solution().readBinaryWatch(1))
print(Solution().readBinaryWatch(2))
