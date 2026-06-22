class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        
        for i in tokens:
        #+
            if i == "+":
                a = res.pop()
                b = res.pop()
                res.append(int(b + a))
        #-
            elif i == "-":
                a = res.pop()
                b = res.pop()
                res.append(int(b - a))
        #*
            elif i == "*":
                a = res.pop()
                b = res.pop()
                res.append(int(b * a))
        #/
            elif i == "/":
                a = res.pop()
                b = res.pop()
                res.append(int(b / a))
        #res.append
            else:
                res.append(int(i))
        return res[-1]