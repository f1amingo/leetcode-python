class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stk = []
        self.pop_stk = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stk.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 1.如果pop_stk不为空，push_stk绝对不可以压入数据
        if not self.pop_stk:
            # 2.push_stk如果要将数据压入pop_stk，必须一次压完
            while self.push_stk:
                self.pop_stk.append(self.push_stk.pop())
        if self.pop_stk:
            return self.pop_stk.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.pop_stk:
            return self.pop_stk[-1]
        elif self.push_stk:
            return self.push_stk[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.push_stk and not self.pop_stk

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
