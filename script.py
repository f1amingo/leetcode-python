class DNode:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = DNode(-1, -1)
        self.tail = DNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            # 找到并删除
            node = self.map[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            # 添加到队首
            node.prev, node.next = self.head, self.head.next
            self.head.next.prev = node
            self.head.next = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key, None)
        # 没找到，新节点
        if not node:
            # 容量已满，删除队尾
            if self.size == self.capacity and self.size > 0:
                to_delete = self.tail.prev
                self.tail.prev = to_delete.prev
                to_delete.prev.next = self.tail
                # map中也要删
                del self.map[to_delete.key]
            else:
                self.size += 1
            node = DNode(key, value)
        else:
            # 找到并删除
            node = self.map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        self.map[key] = node
        # 添加到队首
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
assert obj.get(1) == 1
obj.put(3, 3)
assert obj.get(2) == -1
obj.put(4, 4)
assert obj.get(1) == -1
assert obj.get(3) == 3
assert obj.get(4) == 4
