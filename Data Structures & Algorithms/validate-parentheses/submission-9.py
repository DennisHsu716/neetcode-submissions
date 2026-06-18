class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if i == "{":
                res.append("}")
            elif i == "[":
                res.append("]")
            elif i == "(":
                res.append(")")
            else:
                if not res or i != res[-1]:
                    return False 
                res.pop()
        if len(res) != 0:
            return False
        else: 
            return True 
