class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.stk_min = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if self.stk_min:
            if self.stk_min[-1] >= x:
                self.stk_min.append(x)
        else:
            self.stk_min.append(x)

    def pop(self) -> None:
        if self.stk:
            if self.stk[-1] == self.stk_min[-1]:
                self.stk_min.pop()
            self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]
        return None

    def getMin(self) -> int:
        if self.stk_min:
            return self.stk_min[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
