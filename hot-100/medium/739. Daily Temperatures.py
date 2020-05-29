import time


class Solution(object):
    # 直觉方法每次从当前元素往后计算一遍
    # 时间复杂度ln(O^2)
    def dailyTemperatures0(self, T):
        if not T:
            return T
        size = len(T)
        res = []
        for i in range(0, size):
            count = 0
            has_warmer = False
            for j in range(i + 1, size):
                count += 1
                if T[j] > T[i]:
                    has_warmer = True
                    break
            if has_warmer:
                res.append(count)
            else:
                res.append(0)
        return res

    # 直觉方法优化代码
    def dailyTemperatures1(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return T
        size = len(T)
        res = [0] * size
        for i in range(0, size):
            for j in range(i + 1, size):
                if T[j] > T[i]:
                    res[i] = j - i
                    break
        return res

    # 后序遍历
    def dailyTemperatures2(self, T):
        if not T:
            return []
        size = len(T)
        res = [0] * size
        for i in range(size - 2, -1, -1):
            j = i + 1
            while j < size:
                if T[j] > T[i]:
                    res[i] = j - i
                    break
                if res[j] == 0:
                    break
                j += res[j]
        return res

    # 使用栈倒序
    def dailyTemperatures3(self, T):
        if not T:
            return []
        n = len(T)
        stack = []
        res = [0] * n
        stack.append(n - 1)
        for i in range(n - 2, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

    # 使用栈正序
    # 出栈的时候做处理
    def dailyTemperatures4(self, T):
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                top_i = stack.pop()
                res[top_i] = i - top_i
            stack.append(i)
        return res


print(Solution().dailyTemperatures4([73, 74, 75, 71, 69, 72, 76, 73]))
