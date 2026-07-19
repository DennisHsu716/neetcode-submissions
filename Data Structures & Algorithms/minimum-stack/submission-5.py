class MinStack:

    def __init__(self):
        self.store = []

    def push(self, val: int) -> None:
        self.store.append(val)
        

    def pop(self) -> None:
        self.store.pop()
        

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        mini = self.store[-1]
        res = []

        while len(self.store):
            mini = min(mini, self.store[-1])
            res.append(self.store.pop())
        
        while len(res):
            self.store.append(res.pop())
        
        return mini
        
