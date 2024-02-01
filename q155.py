class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minStk) == 0 or val < self.minStk[-1][0]: self.minStk.append((val, 1))
        elif val == self.minStk[-1][0]: 
            self.minStk[-1] = (self.minStk[-1][0], self.minStk[-1][1] + 1)

    def pop(self) -> None:
        if self.stk[-1] == self.minStk[-1][0]:
            if self.minStk[-1][1] == 1: self.minStk.pop()
            else: self.minStk[-1] = (self.minStk[-1][0], self.minStk[-1][1] - 1)

        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
