class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history_list = [self.homepage]
        self.pointer = 0
        

    def visit(self, url: str) -> None:
        print("before Visit: ",self.history_list,"url: ",url," pointer: ",self.pointer)
        self.history_list = self.history_list[0:self.pointer+1]
        self.history_list.append(url)
        self.pointer+=1
        print("after Visit: ",self.history_list,"url: ",url," pointer:",self.pointer)        

    def back(self, steps: int) -> str:
        if self.pointer-steps>0:
            self.pointer -=steps
        else:
            self.pointer = 0
        print("back ",self.history_list[self.pointer], "pointer: ",self.pointer)
        return self.history_list[self.pointer]
        
        

    def forward(self, steps: int) -> str:
        if steps+self.pointer<len(self.history_list)-1:
            self.pointer +=steps
        else:
            self.pointer = len(self.history_list)-1
        return self.history_list[self.pointer]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)