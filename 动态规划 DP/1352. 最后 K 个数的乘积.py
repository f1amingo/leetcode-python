class ProductOfNumbers:

    def __init__(self):
        self.pre = [1]
        self.zeroIdx = -1

    # 另一种写法，碰到0清空数组
    def add(self, num: int) -> None:
        if self.pre[-1] == 0:
            self.pre.append(num)
        else:
            self.pre.append(self.pre[-1] * num)
        if num == 0:
            self.zeroIdx = len(self.pre) - 1

    def getProduct(self, k: int) -> int:
        n = len(self.pre)
        if n - k <= self.zeroIdx:
            return 0
        if self.pre[n - k - 1] == 0:
            return self.pre[-1]
        else:
            return self.pre[-1] // self.pre[n - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
assert obj.getProduct(2) == 20
assert obj.getProduct(3) == 40
assert obj.getProduct(4) == 0
obj.add(8)
assert obj.getProduct(2) == 32
