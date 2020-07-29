class MinStack:

    # 思路：
    # 1. 普通栈，取最小值时遍历一遍，但是需要O(1)，时间、空间是可以互换的，自然想到多使用一些空间。
    # 2. 使用一个变量，每次push保存当前的最小值，但是如果当前最小值pop()出去之后，寻找下一个最小值时，又需要遍历。
    # 3. 使用一个辅助栈，每次push的同时，将当前最小值push到辅助栈内，完美解决问题。
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_stk = []

    def push(self, x: int) -> None:
        cur_min = min(x, self.min_stk[-1]) if self.min_stk else x
        self.stk.append(x)
        self.min_stk.append(cur_min)

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()
            self.min_stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]

    def min(self) -> int:
        if self.min_stk:
            return self.min_stk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
