class MinStack:

    def __init__(self):
        self.stack=[]
        
        self.min=[]
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min.append(val)
        else:
            self.stack.append(val)
        
        if self.min[-1] > val or self.min[-1]==val :
            self.min.append(val)

    def pop(self) -> None:
        rm=self.stack.pop()
        if self.min[-1]== rm:
            self.min.pop()
    

    def top(self) -> int:
        
        return self.stack[-1]
    def getMin(self) -> int:
        # print(self.min)
        if not self.min:
            return None
        else:
            return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()