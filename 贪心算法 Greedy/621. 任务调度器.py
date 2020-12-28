from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_freq, max_freq_times = 0, 0
        for v in counter.values():
            if v > max_freq:
                max_freq = v
                max_freq_times = 1
            elif v == max_freq:
                max_freq_times += 1
        return max((max_freq - 1) * (n + 1) + max_freq_times, len(tasks))


assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
assert Solution().leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
