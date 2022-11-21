import heapq
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val >= val:
            self.min_.append(val)
            self.min_val = val

    def pop(self) -> None:
        last = self.stack.pop()
        if self.min_val == last:
            self.min_.pop()
            if self.min_:
                self.min_val = self.min_[-1]
            else:
                self.min_val = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()