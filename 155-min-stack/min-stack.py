class MinStack:

    def __init__(self):
        self.minStack = []
        self.minValue = float('inf')

    def push(self, val: int) -> None:
        self.minValue = min(self.minValue, val)
        self.minStack.append([val, self.minValue])

    def pop(self) -> None:
        self.minStack.pop(-1)
        if self.minStack:
            self.minValue = self.minStack[-1][1]
        else:
            self.minValue = float('inf')    

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minValue


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()