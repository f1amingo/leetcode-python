from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # python没有大根堆，负号+小根堆来实现
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))

    def findMedian(self) -> float:
        # 第一个元素会进入max_heap
        if self.max_heap:
            if len(self.max_heap) == len(self.min_heap):
                return (self.min_heap[0] - self.max_heap[0]) / 2
            else:
                return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
finder = MedianFinder()
finder.addNum(2)
print(finder.findMedian())
finder.addNum(3)
print(finder.findMedian())
