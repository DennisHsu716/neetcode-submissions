class MinStack:

    def __init__(self):
        self.store = []
        self.minstore = []
        

    def push(self, val: int) -> None:
        self.store.append(val)

        if not self.minstore:
            self.minstore.append(val)
        else:
            self.minstore.append(min(val, self.minstore[-1]))

        

    def pop(self) -> None:
        self.store.pop()
        self.minstore.pop()

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        return self.minstore[-1]
        
