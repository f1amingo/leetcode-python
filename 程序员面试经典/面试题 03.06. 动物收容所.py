from typing import List


class AnimalShelf:

    def __init__(self):
        from collections import deque
        self.zoo = [deque(), deque()]

    def enqueue(self, animal: List[int]) -> None:
        self.zoo[animal[1]].append(animal)

    def dequeueAny(self) -> List[int]:
        if not self.zoo[0] and not self.zoo[1]:
            return [-1, -1]
        if not self.zoo[0]:
            return self.zoo[1].popleft()
        if not self.zoo[1]:
            return self.zoo[0].popleft()
        if self.zoo[0][0] > self.zoo[1][0]:
            return self.zoo[1].popleft()
        else:
            return self.zoo[0].popleft()

    def dequeueDog(self) -> List[int]:
        return self.zoo[1].popleft() if self.zoo[1] else [-1, -1]

    def dequeueCat(self) -> List[int]:
        return self.zoo[0].popleft() if self.zoo[0] else [-1, -1]


# Your AnimalShelf object will be instantiated and called as such:
obj = AnimalShelf()
obj.enqueue([0, 0])
obj.enqueue([1, 1])
obj.enqueue([2, 0])
param_2 = obj.dequeueAny()
param_3 = obj.dequeueAny()
