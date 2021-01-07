# push, pop, top都是原有的方法
# 关键在于getMin的设计
# 最朴素的想法，遍历一遍，O(n)，不满足题意
# 假设可以用更多的空间，入队时就将当前最小值一起入队
# 当前最小值会在之前的最小值和当前元素中产生
class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, x: int) -> None:
        if self.stk:
            self.stk.append((x, min(x, self.stk[-1][1])))
        else:
            self.stk.append((x, x))

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]

    def getMin(self) -> int:
        if self.stk:
            return self.stk[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
