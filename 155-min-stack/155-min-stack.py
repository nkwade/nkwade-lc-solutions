class MinStack:

    def __init__(self):
        self.lowest = dict()
        self.stack = []
        self.i = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.i += 1
        if self.i != 0:
            self.lowest[self.i] = min(self.lowest[self.i-1], val)
        else:
            self.lowest[self.i] = val
        
    def pop(self) -> None:
        self.stack.pop(-1)
        self.i -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.lowest[self.i]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()