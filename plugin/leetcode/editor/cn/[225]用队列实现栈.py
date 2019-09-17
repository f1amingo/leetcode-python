# 使用队列实现栈的下列操作：
#
# 
# push(x) -- 元素 x 入栈 
# pop() -- 移除栈顶元素 
# top() -- 获取栈顶元素 
# empty() -- 返回栈是否为空 
# 
#
# 注意: 
#
# 
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。 
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。 
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。 
# 
# Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.top_ele = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.top_ele = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.queue:
            return
        for i in range(0, len(self.queue) - 1):
            tmp = self.queue.pop(0)
            self.queue.append(tmp)
            if i == len(self.queue) - 2:
                self.top_ele = tmp
        if len(self.queue) == 1:
            self.top_ele = None
        return self.queue.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_ele

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)

obj = MyStack()
obj.push(1)
tmp = obj.top()
obj.push(2)
obj.pop()
obj.pop()
tmp = obj.empty()
obj.pop()
