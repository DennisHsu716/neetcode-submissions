class MinStack:

    def __init__(self):
        self.store = []
        self.ministore = []
        

    def push(self, val: int) -> None:
        self.store.append(val)

        if not self.ministore:
            self.ministore.append(val)
        else:
            self.ministore.append(min(val, self.ministore[-1]))
            
        

    def pop(self) -> None:
        self.store.pop()
        self.ministore.pop()
        

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        return self.ministore[-1]
        
