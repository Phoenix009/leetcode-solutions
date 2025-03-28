class ProductOfNumbers:

    def __init__(self):
        self.store = [1]

    def add(self, num: int) -> None:
        self.store.append(self.store[-1] * num)
        

    def getProduct(self, k: int) -> int:
        return self.store[-1] / self.store[len(self.store) - 1 - k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
