class MinStack:

    def __init__(self):
        self.mystack = []
        self.count = 0
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.mystack.append(val)
        if len(self.min_stack)>0:
            self.min_stack.append(min(val,self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.mystack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.mystack[-1]        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
