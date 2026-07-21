class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack= []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minStack[-1] if self.minStack else val) #to check which one is smaller current value or previously addes value
        self.minStack.append(val) #after checking append the min value in minStack

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
