class MinStack:

    def __init__(self):
        self.store = []
        self.mini = []
        

    def push(self, val: int) -> None:
        self.store.append(val)

        if not self.mini:
            self.mini.append(val)
        else:
            self.mini.append(min(val, self.mini[-1]))

    def pop(self) -> None:
        self.store.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
