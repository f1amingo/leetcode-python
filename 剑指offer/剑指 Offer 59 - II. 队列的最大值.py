import queue


class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        # 这里不能用self.queue
        if self.deque:
            tmp = self.queue.get()
            if tmp == self.deque[0]:
                self.deque.popleft()
            return tmp
        else:
            return -1


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
obj.pop_front()
obj.pop_front()
obj.pop_front()
obj.pop_front()
obj.pop_front()
obj.push_back(15)
obj.max_value()
obj.push_back(9)
obj.max_value()
