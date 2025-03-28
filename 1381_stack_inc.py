class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.acc = 0

    def push(self, x: int) -> None:
        if len(self.stack) >= self.maxSize:
            pass
        
        if self.stack: self.stack[-1][1] += self.acc
        self.acc = 0
        self.stack.append([x, 0])

        for ele in self.stack:
            print(ele, end=" ")
        print()

    def pop(self) -> int:
        res = -1
        if self.stack:
            val, ac = self.stack.pop()
            self.acc += ac
            res = val + self.acc

        if not self.stack:
            self.acc = 0

        for ele in self.stack:
            print(ele, end=" ")
        print()

        return res

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        if k > len(self.stack):
            self.stack[-1][1] += val
        else:
            self.stack[k-1][1] += val
        for ele in self.stack:
            print(ele, end=" ")
        print()



