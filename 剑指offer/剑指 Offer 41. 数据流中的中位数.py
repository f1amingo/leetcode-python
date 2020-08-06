from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            if self.max_heap:
                return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            if self.max_heap:
                return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
finder = MedianFinder()
finder.addNum(2)
print(finder.findMedian())
finder.addNum(3)
print(finder.findMedian())
