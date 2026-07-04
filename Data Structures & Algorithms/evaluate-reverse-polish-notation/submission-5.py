class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                a = res.pop()
                b = res.pop()
                res.append(int(b + a))
            elif tokens[i] == "-":
                a = res.pop()
                b = res.pop()
                res.append(int(b - a))
            elif tokens[i] == "*":
                a = res.pop()
                b = res.pop()
                res.append(int(b * a))
            elif tokens[i] == "/":
                a = res.pop()
                b = res.pop()
                res.append(int(b / a))
            else:
                res.append(int(tokens[i]))
        return res [-1]