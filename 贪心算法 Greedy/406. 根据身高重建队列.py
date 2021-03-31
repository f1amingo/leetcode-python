from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        ans = [None] * n
        people.sort(key=lambda x: (x[0], -x[1]))
        for p in people:
            spaces = p[1] + 1
            for i in range(n):
                if ans[i] is None:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = p
                        break
        return ans


assert Solution().reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]) == [[4, 0], [5, 0], [2, 2], [3, 2],
                                                                                         [1, 4], [6, 0]]
assert Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]) == [[5, 0], [7, 0], [5, 2], [6, 1],
                                                                                         [4, 4], [7, 1]]
