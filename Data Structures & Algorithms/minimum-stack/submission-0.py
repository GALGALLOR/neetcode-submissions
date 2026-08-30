class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_count=0
        self.minVal = 0
        

    def push(self, val: int) -> None:
        mystack = self.stack        
        mystack.append(val)
        self.stack_count+=1
        self.minVal = min(self.minVal,val)

    def pop(self) -> None:
        #remove from stack   
        self.stack_count -=1
        self.stack = self.stack[:self.stack_count]
        

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        
