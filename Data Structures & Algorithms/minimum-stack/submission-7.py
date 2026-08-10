class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        mini = self.stack[-1]
        tep = []
        while len(self.stack):
            mini = min(mini, self.stack[-1]) 
            tep.append(self.stack.pop())
        	#因為要把值印回stack, 所以要開一個stack 做準備
        while len(tep):
            self.stack.append(tep.pop())
		#把所有值印回去stack 
        
        return mini