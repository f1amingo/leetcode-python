class CQueue:

    def __init__(self):
        self.main_stk = []
        self.sub_stk = []  # 实现倒序，这样最先加入的元素，就会到栈顶

    def appendTail(self, value: int) -> None:
        self.main_stk.append(value)

    def deleteHead(self) -> int:
        if not self.main_stk and not self.sub_stk:
            return -1
        if not self.sub_stk:
            while self.main_stk:
                self.sub_stk.append(self.main_stk.pop())
        return self.sub_stk.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
