from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.lookup.move_to_end(key)
            return self.lookup[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup.pop(key)
        self.lookup[key] = value
        if len(self.lookup) > self.capacity:
            self.lookup.popitem(False)


# Your LRUCache object will be instantiated and called as such:

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
