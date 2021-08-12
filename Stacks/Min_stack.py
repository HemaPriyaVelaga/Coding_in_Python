class MinStack:

    min_ele = float('inf')
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min=float('inf')
        self.stk = []
        

    def push(self, val: int) -> None:
        
        if val<=self.min:
            self.stk.append(self.min)
            self.min  = val
        self.stk.append(val)
        #print('Stack: ', self.stk)

    def pop(self) -> None:
        t = self.stk[-1]
        
        self.stk.pop(-1)
        
        if t==self.min:
            self.min = self.stk[-1]
            self.stk.pop()
        
        #print('Stack: ', self.stk)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
